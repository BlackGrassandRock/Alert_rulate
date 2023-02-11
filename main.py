import threading

from src.tlrulate_telegram_bot import *
from src.tlrulate_telegram_bot import *
from src.tlrulate_shedule import *
from src.tlrulate_config import * #secure data


def tl_bot():
    while True:
        schedule.run_pending()

def tl_shed():
    bot = telebot.TeleBot(TOKEN)

th1 = threading.Thread(target=tl_bot)
th2 = threading.Thread(target=tl_shed)

def main():
    #th2.start()
    #th1.start()
    #bot = telebot.TeleBot(TOKEN)
    #while True:
    #    schedule.run_pending()
    #    time.sleep(1)

if __name__ == "__main__":
    main()
