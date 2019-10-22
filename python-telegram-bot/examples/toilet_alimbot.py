#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

import threading
import datetime

import logging
import firebase_admin
import telegram

from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import firestore

from datetime import datetime

cred = credentials.Certificate('../firebase/ajoah_key.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

end = False

REACTION = range(1)



def getSysDt():
    return datetime.fromtimestamp(datetime.now().timestamp()).strftime('%Y-%m-%d %H:%M:%S')


def execute_func_y8(second=10.0):
    global end
    bot = telegram.Bot(token='855826758:AAGhShCtFGHPelo4tgNGM3id3M81Ijy-luQ')
    
    logger.info("8층 프로세스 시작~")

    if end:
        return

    is_deleted = False

    y8_m_obj = db.collection('current').where('group', '==', 'Y8.M').stream()
    target_seq = 0  # 들어갈 순번이 target_seq가 되었을때 들여보냄
    
    for x in y8_m_obj:
        # obj의 사용상태가 false인 경우만 들여보내는 알림을 보내도록 함
        if x.to_dict()['using'] is False:
            target_seq = target_seq + 1

            resv_obj_y8 = db.collection('reservation').where('location', '==', 'Y8.M').where('seq', '==', target_seq).stream()
            resv_cnt = 0
            for resv in resv_obj_y8:
                resv_cnt = resv_cnt + 1
                send_msg = x.to_dict()['name'] + '이 비었습니다! 빨리 달려가세요. 제한시간은 1분입니다. 1분이 지나면 다른 사람에게 순서가 넘어가요.'
                
                if resv.to_dict()['resv_channel'] == 'Telegram':
                    bot.send_message(chat_id=resv.to_dict()['telegram_id'], text=send_msg)

                    doc_noti = db.collection('noties')
                    doc_noti.add({
                        'users_fid': resv.to_dict()['telegram_id'],
                        'send_type': '빈칸알림',
                        'nickname': resv.to_dict()['nickname'],
                        'channel': 'Telegram',
                        'telegram_chatid': resv.to_dict()['telegram_id'],
                        'send_datetime': getSysDt(),
                        'send_message': send_msg 
                    })
                elif resv.to_dict()['resv_channel'] == 'MobileWeb':
                    logger.info('MobileWeb alim')

                    doc_noti = db.collection('noties')
                    doc_noti.add({
                        'users_fid': resv.to_dict()['phone_num'],
                        'send_type': '빈칸알림',
                        'nickname': resv.to_dict()['nickname'],
                        'channel': 'MobileWeb',
                        'sms_phone_number': resv.to_dict()['phone_num'],
                        'send_datetime': getSysDt(),
                        'send_message': send_msg
                    })

                # 해당건의 reservation collection건을 delete 처리하고
                db.collection('reservation').document(resv.id).delete()
                is_deleted = True

            #target_seq = target_seq + 1

    # 나머지 건들의 순번을 앞당겨줍니다
    if is_deleted:
        other_resv_obj = db.collection('reservation').where('location', '==', 'Y8.M')
        for other_resv in other_resv_obj.stream():
            current_seq = other_resv.to_dict()['seq']
            if current_seq > target_seq:
                update_seq = current_seq - target_seq
                db.collection('reservation').document(other_resv.id).update({'seq': update_seq})

    target_seq = 0

    threading.Timer(second, execute_func_y8, [second]).start()


def execute_func_y7(second=10.0):
    global end
    bot = telegram.Bot(token='855826758:AAGhShCtFGHPelo4tgNGM3id3M81Ijy-luQ')    

    logger.info("7층 프로세스 시작~")

    if end:
        return

    is_deleted = False

    # To-do logic
    y7_m_obj = db.collection('current').where('group', '==', 'Y7.M').stream()
    target_seq = 0  # 들어갈 순번이 target_seq가 되었을때 들여보냄

    for x in y7_m_obj:
        # obj의 사용상태가 false인 경우만 들여보내는 알림을 보내도록 함
        if x.to_dict()['using'] is False:
            target_seq = target_seq + 1

            resv_obj_y7 = db.collection('reservation').where('location', '==', 'Y7.M').where('seq', '==', target_seq).stream()
            resv_cnt = 0
            for resv in resv_obj_y7:
                resv_cnt = resv_cnt + 1
                send_msg = x.to_dict()['name'] + '이 비었습니다! 빨리 달려가세요! 제한시간은 1분입니다. 1분이 지나면 다른 사람에게 순서가 넘어가요.'

                if resv.to_dict()['resv_channel'] == 'Telegram':
                    bot.send_message(chat_id=resv.to_dict()['telegram_id'], text=send_msg)

                    doc_noti = db.collection('noties')
                    doc_noti.add({
                        'users_fid': resv.to_dict()['telegram_id'],
                        'send_type': '빈칸알림',
                        'nickname': resv.to_dict()['nickname'],
                        'channel': 'Telegram',
                        'telegram_chatid': resv.to_dict()['telegram_id'],
                        'send_datetime': getSysDt(),
                        'send_message': send_msg
                    })
                elif resv.to_dict()['resv_channel'] == 'MobileWeb':
                    logger.info('MobileWeb alim')

                    doc_noti = db.collection('noties')
                    doc_noti.add({
                        'users_fid': resv.to_dict()['phone_num'],
                        'send_type': '빈칸알림',
                        'nickname': resv.to_dict()['nickname'],
                        'channel': 'MobileWeb',
                        'sms_phone_number': resv.to_dict()['phone_num'],
                        'send_datetime': getSysDt(),
                        'send_message': send_msg
                    })

                # 해당건의 reservation collection건을 delete 처리하고
                db.collection('reservation').document(resv.id).delete()
                is_deleted = True
    
            #target_seq = target_seq + 1

    # 나머지 건들의 순번을 앞당겨줍니다
    if is_deleted:
        other_resv_obj = db.collection('reservation').where('location', '==', 'Y7.M')
        for other_resv in other_resv_obj.stream():
            current_seq = other_resv.to_dict()['seq']
            if current_seq > target_seq:
                update_seq = current_seq - target_seq
                db.collection('reservation').document(other_resv.id).update({'seq': update_seq})

    target_seq = 0

    threading.Timer(second, execute_func_y7, [second]).start()


def cancel():
    logger.info('프로세스 취소~')


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    execute_func_y8(60.0)
    execute_func_y7(60.0)
'''
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("855826758:AAGhShCtFGHPelo4tgNGM3id3M81Ijy-luQ", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add conversation handler with the states MAINMENU, RESERVATION, LOCATION, PASSWD, NOTICE
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('reaction', reaction)],

        states={
            REACTION: [MessageHandler(Filters.text, reaction)]
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
'''

if __name__ == '__main__':
    #execute_func_y8(5.0)
    #execute_func_y7(5.0)
    main()
