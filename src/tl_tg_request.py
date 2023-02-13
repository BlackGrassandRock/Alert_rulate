import telebot

from src.tl_config import *

P_TIMEZONE = TIMEZONE
TIMEZONE_COMMON_NAME = TIMEZONE_COMMON_NAME
bot = telebot.TeleBot(TOKEN)

#Sending an error message to the user
def request_status_mess_2(id):
    bot.send_message(
        id,
        "Упс. Что-то случилось с сайтом. Попробуем достучатся до него позднее. А пока, можешь написать о проблеме разрабу /write "
        )

def request_status_mess_3(id):
    bot.send_message(
        id,
        "В  последднее время на этот акаунт пытались зайти слишком много раз. Включилась блокировка. Придётся подождать пока она не снимется. А пока, можешь написать о проблеме разрабу /write"
        )

def request_status_mess_4(id):
    bot.send_message(
        id,
        "Неправильно указан логин или пароль."
        )

def request_status_mess_5(id):
    bot.send_message(
        id,
        "Что-то с парсером не так."
        )

def request_status_mess_6(id):
    bot.send_message(
        id,
        "Такого логина быть не может. Попробуй ввести логин ещё раз"
        )

def request_status_mess_7(id):
    bot.send_message(
        id,
        "Такого пароля быть не может. Начните авторизацию сначала /login"
        )

def request_status_mess_9(id):
    bot.send_message(
        id,
        "Неполадки с ботом, обратить в поддержку"
        )

def request_status_mess_10(id):
    bot.send_message(
        id,
        "Превышнено количество раз неправильно веденного логина или пароля. Доступ к оповещениям - приостоновлен. Для возобновления досткупа напишите разработчику /write"
        )

def answer(message, id):
    bot.send_message(
        id,
        message
        )
