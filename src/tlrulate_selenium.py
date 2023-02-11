from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from src.tlrulate_request import *

def parser(users_data):
    chg_usr_dt = []
    bounce = True

    if bounce == True: #Allows to display one error message
        try:
            #options
            options = webdriver.ChromeOptions()

            #parser background mode!!!
            #options.headless = True

            #open the site
            driver = webdriver.Chrome(options = options)
            driver.get("https://tl.rulate.ru/")
            assert "Tl.Rulate.ru" in driver.title
        except Exception:
            request_status_mess_2(users_data[0])
            bounce = False

    if bounce == True:
        try:
            #enter login
            elem = driver.find_element(By.NAME, "login[login]")
            elem.clear()
            elem.send_keys(users_data[1])
            #enter password
            elem = driver.find_element(By.NAME, "login[pass]")
            elem.clear()
            elem.send_keys(users_data[2])
            elem.send_keys(Keys.ENTER)
            assert "Tl.Rulate.ru" in driver.title
        except Exception:
            request_status_mess_3(users_data[0])
            bounce = False

    if bounce == True:
        try:
            elem = driver.find_element(By.PARTIAL_LINK_TEXT, 'Оповеще')
            elem.click()
        except Exception:
            request_status_mess_4(users_data[0])
            bounce = False

    if bounce == True:
        try:
            elem = driver.find_element(By.ID, "Notices")
            alert = elem.find_elements(By.TAG_NAME, 'p')
            for i in alert:
                chg_usr_dt.append(i.text) #throwing an answer to the list
            for i in range(0, len(chg_usr_dt), 2):  #Formatting list
                users_data.append(chg_usr_dt[i]+" "+chg_usr_dt[i+1])
            return users_data
        except Exception:
            request_status_mess_5(users_data[0])
            bounce = False

    driver.close()
    driver.quit()
