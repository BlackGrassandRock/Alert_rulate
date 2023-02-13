import telebot
import pytz

from src.tlrulate_validator import *
from src.tl_config import * #secure data
from src.tlrulate_selenium import parser
from src.tl_db_new_data import *
from src.tl_db_lg_pas import *


users_dt = []

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
def write_to_develop(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(
        telebot.types.InlineKeyboardButton(
            'Написать разрабу', url= DEVELOPER
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

#accepting login from the user
def add_user(message):
    users_dt = [message.chat.id, str(message.text)]
    if valid_log(message.text, users_dt[0]) == False:
        login_command(message)
    else:
        bot.send_message(
            message.chat.id,
            "Отлично. А теперь, введи пароль от сайта  https://tl.rulate.ru/")
        bot.register_next_step_handler(message, user_password, users_dt)

#accepting password
def user_password(message, users_dt):
    if valid_pass(message.text, users_dt[0]) == True: #file tlrulate_validator
        users_dt += [str(message.text), "1"]
        if chkr_pas_from_tg(users_dt[0]) == "ok": #file tl_db_lg_pas
            users_dt = parser(users_dt) #file tlrulate_selenium
            if users_dt != None:
                cheker(users_dt)

def main():
    bot.polling(none_stop=True)

if __name__ == "__main__":
    main()
