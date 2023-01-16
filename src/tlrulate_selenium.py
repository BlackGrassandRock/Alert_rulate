from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent

import time
import pickle

import tlrulate_validator as tl_vl
import tlrulate_request
import tlrulate_database

def parser(users_data):
    try:
        #options
        options = webdriver.ChromeOptions()

        #change useragent
        #useragent = UserAgent()
        #options.add_argument(f"user-agent={useragent.random}")

        #disable webdriver mode
        #options.add_argument("--disable-blink-features=AutomationControlled")

        #parser background mode!!!
        options.headless = True

        #open the site
        try:
            driver = webdriver.Chrome(options = options)
            driver.get("https://tl.rulate.ru/")
            assert "Tl.Rulate.ru" in driver.title
        except Exception:
            tlrulate_request.request_status_mess_2(2, int(users_data[0]))
            users_data[3] = 2
        else:

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
                #time.sleep(5)
                assert "Tl.Rulate.ru" in driver.title
            except Exception:
                tlrulate_request.request_status_mess_3(3, int(users_data[0]))
            else:

                try:
                    elem = driver.find_element(By.PARTIAL_LINK_TEXT, 'Оповеще')
                    elem.click()
                except Exception:
                    tlrulate_request.request_status_mess_4(4, int(users_data[0]))
                else:

                    elem = driver.find_element(By.ID, "Notices")
                    alert = elem.find_elements(By.TAG_NAME, 'p')
                    for i in alert:
                        chg_usr_dt.append(i.text) #throwing an answer to the list

                    for i in range(0, len(chg_usr_dt), 2):  #Formatting list
                        users_data.append(chg_usr_dt[i]+" "+chg_usr_dt[i+1])

    except Exception:
        tlrulate_request.request_status_mess_5(5, int(users_data[0]))

    finally:
        driver.close()
        driver.quit()

    if users_data[3]=='1':
        tlrulate_database.cheker(users_data)
