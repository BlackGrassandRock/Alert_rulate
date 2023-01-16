import telebot
import pytz
import json
import traceback

import datetime

import tlrulate_validator as tl_vl
import tlrulate_config

P_TIMEZONE = pytz.timezone(tlrulate_config.TIMEZONE)
TIMEZONE_COMMON_NAME = tlrulate_config.TIMEZONE_COMMON_NAME
bot = telebot.TeleBot(tlrulate_config.TOKEN)

#Sending an error message to the user
def request_status_mess_2(message, id):
    bot.send_message(
        id,
        tl_vl.request_status[2]
        )

def request_status_mess_3(message):
    bot.send_message(
        id,
        tl_vl.request_status[3]
        )

def request_status_mess_4(message):
    bot.send_message(
        id,
        tl_vl.request_status[4]
        )

def request_status_mess_5(message):
    bot.send_message(
        id,
        tl_vl.request_status[5]
        )

def request_status_mess_6(message):
    bot.send_message(
        id,
        tl_vl.request_status[6]
        )

def request_status_mess_7(message):
    bot.send_message(
        id,
        tl_vl.request_status[7]
        )

def request_status_mess_9(message):
    bot.send_message(
        id,
        tl_vl.request_status[9]
        )

def answer(message):
    bot.send_message(
        id,
        message
        )

#bot.polling(none_stop=True)
