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

cred = credentials.Certificate('../firebase/ajoah_key.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://ajoah-2121f.firebaseio.com/'
})

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

end = False

REACTION = range(1)

def reaction(update, context):
    '''
    알림에 반응을 한다면?
        1. reservation 테이블에 있는 건을 바로 지워줍니다
        2. 응답 메시지를 뿌려줍니다
        3. 리액션은 끝
    '''



def execute_func_y8(second=10.0):
    global end
    bot = telegram.Bot(token='855826758:AAGhShCtFGHPelo4tgNGM3id3M81Ijy-luQ')
    
    logger.info("8층 프로세스 시작~")

    if end:
        return
    
    # To-do logic
    y8_m_01_obj = db.reference('current/Y8:M:01/')
    if y8_m_01_obj.get()['using'] is True:
        history_y8_m_01_obj = db.reference('history/Y8:M:01/')
        if sorted(history_y8_m_01_obj.get().items(), reverse=True)[0][1]['using'] is False:
            # 알림서비스 기동!
            resv_obj_y8_m_01 = db.reference('reservation/연호8층/')
            resv_dict_y8_m_01 = resv_obj_y8_m_01.get()
            
            if resv_dict_y8_m_01 is None:
                return

            for cid in resv_dict_y8_m_01.keys():
                if resv_dict_y8_m_01[cid]['seq'] == 1:
                    send_msg = '연호8층 1번칸이 비었습니다! 빨리 달려가세요!'
                    bot.send_message(chat_id=cid, text=send_msg, reply_markup=ReplyKeyboardMarkup(['들어갔어', '안들어갈래'], one_time_keyboard=True))
    
    y8_m_02_obj = db.reference('current/Y8:M:02/')
    if y8_m_02_obj.get()['using'] is True:
        history_y8_m_02_obj = db.reference('history/Y8:M:02/')
        if sorted(history_y8_m_02_obj.get().items(), reverse=True)[0][1]['using'] is False:
            # 알림서비스 기동!연호8층/')
            resv_dict_y8_m_02 = resv_obj_y8_m_01.get()

            if resv_dict_y8_m_02 is None:
                return

            for cid in resv_dict_y8_m_02.keys():
                if resv_dict_y8_m_02[cid]['seq'] == 1:
                    send_msg = '연호8층 2번칸이 비었습니다! 빨리 달려가세요!'
                    bot.send_message(chat_id=cid, text=send_msg, reply_markup=ReplyKeyboardMarkup(['들어갔어', '안들어갈래'], one_time_keyboard=True))


    threading.Timer(second, execute_func_y8, [second]).start()


def execute_func_y7(second=10.0):
    global end
    bot = telegram.Bot(token='855826758:AAGhShCtFGHPelo4tgNGM3id3M81Ijy-luQ')    

    logger.info("7층 프로세스 시작~")

    if end:
        return

    # To-do logic
    y7_m_01_obj = db.reference('current/Y7:M:01/')
    if y7_m_01_obj.get() is None:
        threading.Timer(second, execute_func_y7, [second]).start()

    elif y7_m_01_obj.get()['using'] is True:
        history_y7_m_01_obj = db.reference('history/Y7:M:01/')

        if history_y7_m_01_obj.get() is None:
            threading.Timer(second, execute_func_y7, [second]).start()

        elif sorted(history_y7_m_01_obj.get().items(), reverse=True)[0][1]['using'] is False:
            # 알림서비스 기동!
            resv_obj_y7_m_01 = db.reference('reservation/연호7층/')
            resv_dict_y7_m_01 = resv_obj_y7_m_01.get()

            if resv_dict_y7_m_01 is None:
                threading.Timer(second, execute_func_y7, [second]).start()

            for cid in resv_dict_y7_m_01.keys():
                if resv_dict_y7_m_01[cid]['seq'] == 1:
                    send_msg = '연호7층 1번칸이 비었습니다! 빨리 달려가세요!'
                    bot.send_message(chat_id=cid, text=send_msg, reply_markup=ReplyKeyboardMarkup(['들어갔어', '안들어갈래'], one_time_keyboard=True))


    y7_m_02_obj = db.reference('current/Y7:M:02/')
    if y7_m_02_obj.get() is None:
        threading.Timer(second, execute_func_y7, [second]).start()

    elif y7_m_02_obj.get()['using'] is True:
        history_y7_m_02_obj = db.reference('history/Y7:M:02/')

        if history_y7_m_02_obj.get() is None:
            threading.Timer(second, execute_func_y7, [second]).start()

        elif sorted(history_y7_m_02_obj.get().items(), reverse=True)[0][1]['using'] is False:
            # 알림서비스 기동!
            resv_obj_y7_m_02 = db.reference('reservation/연호7층/')
            resv_dict_y7_m_02 = resv_obj_y7_m_02.get()

            if resv_dict_y7_m_02 is None:
                threading.Timer(second, execute_func_y7, [second]).start()

            for cid in resv_dict_y7_m_02.keys():
                if resv_dict_y7_m_02[cid]['seq'] == 1:
                    send_msg = '연호7층 2번칸이 비었습니다! 빨리 달려가세요!'
                    bot.send_message(chat_id=cid, text=send_msg, reply_markup=ReplyKeyboardMarkup(['들어갔어', '안들어갈래'], one_time_keyboard=True))


    threading.Timer(second, execute_func_y7, [second]).start()


def main():
    execute_func_y8(10.0)
    execute_func_y7(10.0)

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
        }

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
