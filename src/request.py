import requests
from bs4 import BeautifulSoup

from src.tl_tg_request import *
from src.tl_db_lg_pas import *


def parser(users_data):
    try:
        session = requests.Session()
        rt = session.post('https://tl.rulate.ru/', {
             'login[login]': users_data[1],
             'login[pass]': users_data[2],
             'remember': 1,
        })
        rt = session.post('https://tl.rulate.ru/my/notices')

        if rt.url != "https://tl.rulate.ru/site/login":
            rt = rt.text
            soup = BeautifulSoup(rt, features="lxml")
            notice =  soup.find(id='Notices')
            for child in notice:
                users_data.append(child.get_text() + " \n")
            return users_data
        else:
            request_status_mess_4(users_data[0])
            edit_nmb_of_lg_attmp(users_data[0])
    except (requests.exceptions.ConnectionError, KeyError):
        request_status_mess_2(users_data[0])
    except  Exception:
        request_status_mess_5(users_data[0])
