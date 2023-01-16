import telebot
import json
import traceback
import pytz

import datetime

import tlrulate_request
import tlrulate_config
import tlrulate_validator as tl_vl
import tlrulate_selenium

P_TIMEZONE = pytz.timezone(tlrulate_config.TIMEZONE)
TIMEZONE_COMMON_NAME = tlrulate_config.TIMEZONE_COMMON_NAME
bot = telebot.TeleBot(tlrulate_config.TOKEN)

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(
        message.chat.id,
        'Привет.\n' +
        'Это бот для получения оповещений с сайта https://tl.rulate.ru/.\n' +
        'Чтобы получать уведомления с сайта, введи команду /login \n'+
        'Если хочешь получить доп. инфу по боту или инструкцию по работе с ним, введи команду /help \n'
        'Хочешь написать разрабу, введи команду /write'
  )

@bot.message_handler(commands=['write'])
def write_command(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(
        telebot.types.InlineKeyboardButton(
            'Написать разрабу', url='t.me/Dyagilev_Olexandr'
  )
    )
    bot.send_message(
        message.chat.id,
        'Если есть жалобы или предложения, буду рад ознакомится с ними.\n',
        reply_markup=keyboard
    )

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(
        message.chat.id,
        '1. Данний бот преднозначен исключительно для получения оповещений с сайта https://tl.rulate.ru/ в телеграм пользователя. ' +
        '2. Для непосредственой работы бота необходимо ввести команду /login, заполнить соответсвующие поле твоего логина (без пробела) и твоего пароля (тоже без пробела) \n' +
        '3. При первом подключении бота к твоей учётной записи, тебе прийдут 20 последних оповищений (возможно уже ранее тобой прочитанных). В дальнейщем отсылаться будут только новые оповещения \n' +
        '4. С момента публикации оповещения, до момента отправки его в телеграм, возможна задержка (не более 15 минут) \n' +
        '5. Даные о логинах и паролях, зашифрованы и используются только для для непосредственой работы бота \n' +
        '6. При необходимости, с кодом бота можно ознакомится тут: https://github.com/BlackGrassandRock/tlrulate_alert_bot'
    )

@bot.message_handler(commands=['login'])
def login_command(message):
    bot.send_message(
        message.chat.id,
        "Введи свой логин от сайта  https://tl.rulate.ru/")
    bot.register_next_step_handler(message, add_user)

def password_command(message):
    bot.send_message(
        message.chat.id,
        "Отлично. А теперь, введи пароль от сайта  https://tl.rulate.ru/")
    bot.register_next_step_handler(message, user_password)

#accepting login from the user
def add_user(message):
    if tl_vl.valid_log(message.text) == tl_vl.request_status[6]:
        tlrulate_request.request_status_mess_6(message) #вызов ошибки №6
        login_command(message)
    else:
        global login
        login = str(message.text)
        password_command(message)

#accepting password
def user_password(message):
    if tl_vl.valid_pas(message.text) == tl_vl.request_status[7]:
        tlrulate_request.request_status_mess_7(message)
        password_command(message)
    else:
        password = str(message.text)
        users_dt = [message.chat.id, login, password, "1"]
        print(users_dt)

        tlrulate_selenium.parser(users_dt)

bot.polling(none_stop=True)
