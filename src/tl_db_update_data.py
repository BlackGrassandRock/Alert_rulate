import pymysql

from src.tl_tg_request import *
from src.tl_config import *
from src.request import *


def controler(users_data):
    upd_answ = answ_from_bd(users_data)
    users_data = [int(upd_answ[0]), upd_answ[1], upd_answ[2], upd_answ[3]]
    new_usr_data = parser(users_data)
    comparison_data(upd_answ, new_usr_data)

#writing id to the shedule list
def shed_for_upd(tl_id):
    nm_flow = str(random.randint(1, 15))
    shed_dict = tl_id
    with open("shed_txt/shed_txt_" + nm_flow + ".txt", mode="a") as f:
        print(shed_dict, file=f)

#Receiving data from a database
def answ_from_bd(id_usr):
    list_of_user = []
    with pymysql.connect(
        host = "localhost",
        user = DB_USER,
        password = DB_PASS,
        database = DB_BASE,
    ) as connection:
        select_answer_query = "SELECT * from tlrulate WHERE (Id = "+ id_usr +")"
        with connection.cursor() as cursor:
            cursor.execute(select_answer_query)
            for i in cursor.fetchone():
                list_of_user.append(i)
    return list_of_user

#comparison of old and new data
def comparison_data(list_of_user, new_usr_data):
    sort_txt = ""
    sorted_all_data = new_usr_data[0:4] + list((set(new_usr_data[4:24]) - set(list_of_user[4:24])) | (set(list_of_user[4:24]) & set(new_usr_data[4:24])))
    sort_new_dt = list(set(new_usr_data[4:24]) - set(list_of_user[4:24])) #
    for i in sort_new_dt:
        sort_txt += i + "\n" + "\n"
    if sort_txt != "":
        answer(sort_txt, new_usr_data[0])
        update_data(sorted_all_data)

#Database updating
def update_data(sorted_all_data):
    mydb = pymysql.connect(
        host = "localhost",
        user = DB_USER,
        password = DB_PASS,
        database = DB_BASE,
    )
    mycursor = mydb.cursor()
    update_query = "UPDATE tlrulate SET Login = %s, Password = %s, Stat_Answer = %s, Alert1 = %s, Alert2 = %s, Alert3 = %s, Alert4 = %s, Alert5 = %s, Alert6 = %s, Alert7 = %s, Alert8 = %s, Alert9 = %s, Alert10 = %s, Alert11 = %s, Alert12 = %s, Alert13 = %s, Alert14 = %s, Alert15 = %s, Alert16 = %s, Alert17 = %s, Alert18 = %s, Alert19 = %s,  Alert20 = %s WHERE Id = %s"
    val_tuple = (sorted_all_data[1], sorted_all_data[2], sorted_all_data[3], sorted_all_data[4], sorted_all_data[5], sorted_all_data[6], sorted_all_data[7], sorted_all_data[8], sorted_all_data[9], sorted_all_data[10], sorted_all_data[11], sorted_all_data[12], sorted_all_data[13], sorted_all_data[14], sorted_all_data[15], sorted_all_data[16], sorted_all_data[17], sorted_all_data[18], sorted_all_data[19], sorted_all_data[20], sorted_all_data[21], sorted_all_data[22], sorted_all_data[23], sorted_all_data[0])
    mycursor.execute(update_query, val_tuple)
    mydb.commit()
