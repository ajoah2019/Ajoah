#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
First, a few callback functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Example of a bot-user conversation using ConversationHandler.
Send /start to initiate the conversation.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
import firebase_admin
import telegram

from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)
from firebase_admin import credentials
from firebase_admin import firestore

from datetime import datetime

cred = credentials.Certificate('../firebase/ajoah_key.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

MAINMENU, RESERVATION, LOCATION, PASSWD, NOTICE, CANCEL, REGISTRATION = range(7)

def start(update, context):
    reply_keyboard = [['비었니', '예약해줘'], ['누구인가', '할말이있어']]

    chatId = str(update.message.chat.id)
    users_ref = db.collection('users').where('telegram_id', '==', chatId).stream()

    user_cnt = 0
    for user in users_ref:
        user_cnt = user_cnt + 1

    if(user_cnt == 0):
        update.message.reply_text(
            'Ajoah 서비스 미등록 사용자입니다.\n'
            '저를 만들어주신 훌륭한 세 분의 중간글자 이름을 입력하세요!\n'
            '(힌트: 송*수, 윤*민, 정*현)')
            #reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
        return PASSWD
    else:
        update.message.reply_text(
            '환영합니다,  즐거운 Ajoah 서비스입니다.\n'
            '아래 메뉴를 선택해주세요~',
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
        return MAINMENU


def mainmenu(update, context):
    user = update.message.from_user
    logger.info("Question: %s", update.message.text)
    
    reply_keyboard = [['비었니', '예약해줘'], ['누구인가', '할말이있어']]
    position_keyboard = [['연호8층', '연호7층']]    
    
    if update.message.text == '비었니':
        update.message.reply_text('어느 화장실이 비어있는지 보고 싶나요?',
                                  reply_markup=ReplyKeyboardMarkup(position_keyboard, one_time_keyboard=True))
        return LOCATION
    elif update.message.text == '예약해줘':
        update.message.reply_text('어느 화장실을 예약하시겠습니까?',
                                  reply_markup=ReplyKeyboardMarkup(position_keyboard, one_time_keyboard=True))
        
        return RESERVATION
    elif update.message.text == '누구인가':
        update.message.reply_text('저는 Ajoah이고 태어난지 얼마 안됐어요.\n'
                                  '저를 낳아주신 분은 기관개발부 송준수/윤경민/정종현입니다.\n'
                                  'Ajoah는 Another joy Of Ah!로써 또다른 \'아~\' 즐거움을 드리려 도와주고 있습니다.',
                                  reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
        return MAINMENU
    elif update.message.text == '할말이있어':
        update.message.reply_text('모두에게 하고 싶은 말을 외쳐보세요!')
        return NOTICE
    else:
        update.message.reply_text(update.message.text)

    return ConversationHandler.END


def notice(update, context):
    reply_keyboard = [['비었니', '예약해줘'], ['누구인가', '할말이있어']]
    
    bot = telegram.Bot(token='855826758:AAGhShCtFGHPelo4tgNGM3id3M81Ijy-luQ')
    nickname = ''
    nick_obj = db.collection('users').where('telegram_id', '==', str(update.message.chat.id)).stream()
    for nick in nick_obj:
        nickname = nick.to_dict()['nickname']
    
    user_obj = db.collection('users').stream()
    
    send_msg = nickname + '님이 모두에게 외칩니다: \n' + update.message.text

    for user in user_obj:
        if user.to_dict()['noti_req_channel'] == 'Telegram':
            bot.sendMessage(chat_id=user.to_dict()['telegram_id'], text=send_msg)
            doc_noti = db.collection('noties')
            doc_noti.add({
                'users_fid': user.to_dict()['telegram_id'],
                'send_type': '전체알림',
                'nickname': user.to_dict()['nickname'],
                'channel': 'Telegram',
                'telegram_chatid': user.to_dict()['telegram_id'],
                'send_datetime': getSysDt(),
                'send_message': send_msg
            })
        #if user.to_dict['telegram_id'] != str(update.message.chat.id):
        #    bot.sendMessage(chat_id=user.to_dict['telegram_id'], text=send_msg)

    update.message.reply_text('모두에게 알려줬어요!', reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    return MAINMENU


def reservation(update, context):
    user = update.message.from_user
    
    reply_keyboard = [['비었니', '예약해줘'], ['누구인가', '할말이있어']]
    cancel_yn_keyboard = [['YES', 'NO']]
    result = 0
    count = 0

    global temp_resv_location
    global location

    # 비어있는 화장실이 있다면 예약 없이 달려가라고 안내해줍니다.
    if update.message.text == '연호8층':
        location = 'Y8.M'

        y8_m_01_open_yn = not db.collection('current').document('Y8.M.01').get().to_dict()['using']
        y8_m_02_open_yn = not db.collection('current').document('Y8.M.02').get().to_dict()['using']

        if y8_m_01_open_yn or y8_m_02_open_yn:
            reply_txt = update.message.text + '에 빈 화장실이 있어요. 빨리 달려가세요!\n' + '빈칸: ' + ('1번칸' if y8_m_01_open_yn else '') + ('/' if y8_m_01_open_yn and y8_m_02_open_yn else '') + ('2번칸' if y8_m_02_open_yn else '')
            update.message.reply_text(reply_txt, reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
            return MAINMENU

    elif update.message.text == '연호7층':
        location = 'Y7.M'

        y7_m_01_open_yn = not db.collection('current').document('Y7.M.01').get().to_dict()['using']
        y7_m_02_open_yn = not db.collection('current').document('Y7.M.02').get().to_dict()['using']

        if y7_m_01_open_yn or y7_m_02_open_yn:
            reply_txt = update.message.text + '에 빈 화장실이 있어요. 빨리 달려가세요!\n' + '빈칸: ' + ('1번칸' if y7_m_01_open_yn else '') + ('/'  if y7_m_01_open_yn and y7_m_02_open_yn else '') + ('2번칸' if y7_m_02_open_yn else '')
            update.message.reply_text(reply_txt, reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
            return MAINMENU
    
    select_resv_obj = db.collection('reservation').where('location', '==', location).where('telegram_id', '==', str(update.message.chat.id)).stream()

    resv_cnt = 0
    for x in select_resv_obj:
        resv_cnt = resv_cnt + 1

    nickname = ''
    nick_obj = db.collection('users').where('telegram_id', '==', str(update.message.chat.id)).stream()
    for nick in nick_obj:
        nickname = nick.to_dict()['nickname']

    if resv_cnt == 0:
        logger.info('탄다1')
        count_resv_obj = db.collection('reservation').where('location', '==', location).stream()

        for x in count_resv_obj:
            count = count + 1
    
        logger.info('위치: [%s] / 순번: [%d]', update.message.text, count + 1)
        
        doc_resv = db.collection('reservation')
        doc_resv.add({
            'location': location,
            'nickname': nickname, #update.message.from_user.first_name, #이건 실제 users의 닉네임으로 변경되어야 함
            'phone_num': '',
            'resv_channel': 'Telegram',
            'resv_dttm': getSysDt(),
            'seq': count + 1,
            'telegram_id': str(update.message.chat.id)
        })
 
        reply_txt = update.message.text + ' 예약 성공! 예약 순번: [' + str(count + 1) + ']'
        update.message.reply_text(reply_txt, reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
        return MAINMENU
    
    # Telegram으로 예약했다면, 취소할 것인지 물어봅니다
    else:
        temp_resv_location = location

        reply_txt = '이미 ' + update.message.text + ' 화장실에 예약이 되어있어요. 예약을 취소할까요?'
        update.message.reply_text(reply_txt, reply_markup=ReplyKeyboardMarkup(cancel_yn_keyboard, one_time_keyboard=True))
        return CANCEL

    return MAINMENU


def cancel(update, context):
    logger.info("Toliet Cancel? [%s]", update.message.text)
    reply_keyboard = [['비었니', '예약해줘'], ['누구인가', '할말이있어']]
    sno = 0

    if update.message.text == 'YES':
        logger.info("temp_resv_location: [%s]", temp_resv_location)
        # reservation 테이블에서 remove처리를 하고
        resv_cancel_obj = db.collection('reservation').where('location', '==', temp_resv_location).where('telegram_id', '==', str(update.message.chat.id)).stream()
        for resv in resv_cancel_obj:
            sno = resv.to_dict()['seq']
            db.collection('reservation').document(resv.id).delete()

        # 지운 건의 seq보다 큰 값들을 1씩 빼서 update합니다
        resv_obj = db.collection('reservation').where('location', '==', temp_resv_location)
        resv_cnt = 0
        for resv in resv_obj.stream():
            resv_cnt = resv_cnt + 1

        if resv_cnt == 0: # 지워지고 예약건수가 없으면 그냥 로직 종료
            reply_txt = '예약이 취소되었습니다. 다시 예약하시려면 \'예약해줘\' 버튼을 눌러주세요!'
            update.message.reply_text(reply_txt, reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
            return MAINMENU

        else: # 아니면 나머지 seq값을 1씩 빼서 update
            for resv in resv_obj.stream():
                current_sno = resv.to_dict()['seq']
                if current_sno > sno:
                    update_sno = current_sno - 1
                    db.collection('reservation').document(resv.id).update({'seq': update_sno})
 
            reply_txt = '예약이 취소되었습니다. 다시 예약하시려면 \'예약해줘\' 버튼을 눌러주세요!'
            update.message.reply_text(reply_txt, reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
            return MAINMENU

    else:
        reply_txt = '예약 상태가 그대로 유지됩니다. 알림을 받을때까지 기다리세요!'
        update.message.reply_text(reply_txt, reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
        return MAINMENU

    return MAINMENU


def location(update, context):
    logger.info("Toilet Location: %s", update.message.text) 
    
    reply_keyboard = [['비었니', '예약해줘'], ['누구인가', '할말이있어']]
    
    if update.message.text == '연호8층':
        # 8층 화장실의 개폐정보를 보여줍니다
        ref_y8_m_01 = db.collection('current').document('Y8.M.01').get()
        ref_y8_m_02 = db.collection('current').document('Y8.M.02').get()
    
        reply_txt = '연호8층 남자화장실 상태입니다.\n' + '1번칸: ' + ('사용가능' if not ref_y8_m_01.to_dict()['using'] else '사용중') + '\n' + '2번칸: ' + ('사용가능' if not ref_y8_m_02.to_dict()['using'] else '사용중')

        update.message.reply_text(reply_txt,
                                  reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
 
    elif update.message.text == '연호7층':
        # 7층 화장실의 개폐정보를 보여줍니다
        ref_y7_m_01 = db.collection('current').document('Y7.M.01').get()
        ref_y7_m_02 = db.collection('current').document('Y7.M.02').get()
        reply_txt = '연호7층 남자화장실 상태입니다.\n' + '1번칸: ' + ('사용가능' if not ref_y7_m_01.to_dict()['using'] else '사용중') + '\n' + '2번칸: ' + ('사용가능' if not ref_y7_m_02.to_dict()['using'] else '사용중')

        update.message.reply_text(reply_txt,
                                  reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))


    return MAINMENU


def skip_location(update, context):
    user = update.message.from_user
    logger.info("User %s did not send a location.", user.first_name)
    update.message.reply_text('You seem a bit paranoid! '
                              'At last, tell me something about yourself.')

    return PASSWD


def getSysDt():
    return datetime.fromtimestamp(datetime.now().timestamp()).strftime('%Y%m%d%H%M%S')


def passwd(update, context):
    if(update.message.text == '준경종'):
        update.message.reply_text('서비스 이용을 위한 닉네임을 입력해주세요.')
        return REGISTRATION

    else:
        update.message.reply_text('우리의 이름을 모르면 이용할 수 없어요. 다시 시작하려면 /start 를 입력하세요')
    return ConversationHandler.END


def registration(update, context):
    doc_user = db.collection('users')

    doc_user.add({
        'nickname': update.message.text,
        'reg_datetime': getSysDt(),
        'telegram_username': update.message.from_user.first_name,
        'telegram_id': str(update.message.chat.id),
        'telegram_chatid': str(update.message.chat.id),
        'noti_req_yn': 'Y',
        'noti_req_channel': 'Telegram',
        'noti_req_datetime': getSysDt(),
    })
    
    start(update, context)
    
    return ConversationHandler.END


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("855826758:AAGhShCtFGHPelo4tgNGM3id3M81Ijy-luQ", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    
    # Add conversation handler with the states MAINMENU, RESERVATION, LOCATION, PASSWD, NOTICE
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        
        states={
            MAINMENU: [MessageHandler(Filters.regex('^(비었니|예약해줘|누구인가|할말이있어)$'), mainmenu)],

            RESERVATION: [MessageHandler(Filters.regex('^(연호8층|연호7층)'), reservation)],

            LOCATION: [MessageHandler(Filters.regex('^(연호8층|연호7층)'), location)],

            PASSWD: [MessageHandler(Filters.text, passwd)],

            NOTICE: [MessageHandler(Filters.text, notice)],

            CANCEL: [MessageHandler(Filters.regex('^(YES|NO)'), cancel)],

            REGISTRATION: [MessageHandler(Filters.text, registration)]
        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )

    dp.add_handler(conv_handler)

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
