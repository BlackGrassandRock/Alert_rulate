import pymysql

#from src.tlrulate_request import *
#from src.tlrulate_config import *
from tlrulate_config import *
users_data = ['3456']

#testing module!!! checking for incorrect password entry

#password_n == None - ok | else - checking attempts of invalid entries
def chkr_pas_from_tg(users_data):
    password_n = pasw_from_bd(users_data[0])
    if password_n == None or password_n != 0:
        return "ok"
    else:
        request_status_mess_10(users_data[0])

#writing id to the shedule list
def shed_for_upd(tl_id):
    nm_flow = str(random.randint(1, 15))
    shed_dict = tl_id
    with open("sorce/shed_txt/shed_txt_" + nm_flow + ".txt", mode="a") as f:
        print(shed_dict, file=f)

#Request from Selenium to the database new data
def req_to_bd(users_data):
    try:
        with pymysql.connect(
            host = "localhost",
            user = DB_USER,
            password = DB_PASS,
            database = DB_BASE,
        ) as connection:
            insert_request_query = """
            INSERT INTO tlrulate(Id, Login, Password, Stat_Answer, Alert1, Alert2, Alert3, Alert4, Alert5, Alert6, Alert7, Alert8, Alert9, Alert10, Alert11, Alert12, Alert13, Alert14, Alert15, Alert16, Alert17, Alert18, Alert19, Alert20)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            reviewers_records = [
            (users_data[0], users_data[1], users_data[2], users_data[3], users_data[4], users_data[5], users_data[6], users_data[7], users_data[8], users_data[9], users_data[10], users_data[11], users_data[12], users_data[13], users_data[14], users_data[15], users_data[16], users_data[17], users_data[18], users_data[19], users_data[20], users_data[21], users_data[22], users_data[23])
            ]
            with connection.cursor() as cursor:
                cursor.executemany(insert_request_query,
                    reviewers_records)
            connection.commit()
    except Exception:
        request_status_mess_9(users_data[0])

#Receiving data from a database
def pasw_from_bd(id_usr):
    id_usr = str(id_usr)
    try:
        list_of_user = []
        with pymysql.connect(
            host = "localhost",
            user = DB_USER,
            password = DB_PASS,
            database = DB_BASE,
        ) as connection:
            select_answer_query = "SELECT Attempts from nm_of_attempts WHERE (Id = "+ id_usr +")"
            with connection.cursor() as cursor:
                cursor.execute(select_answer_query)
                for i in cursor.fetchone():
                    list_of_user = i
    except Exception:
        list_of_user = None
    return list_of_user

#comparison of old and new data
def comparison_data(list_of_user, new_usr_data):
    sort_txt = ""
    sorted_all_data = new_usr_data[0:4] + list((set(new_usr_data[4:24]) - set(list_of_user[4:24])) | (set(list_of_user[4:24]) & set(new_usr_data[4:24])))
    sort_new_dt = list(set(new_usr_data[4:24]) - set(list_of_user[4:24])) #

    for i in sort_new_dt:
        sort_txt += i + "\n"
    if sort_txt != "":
        answer(sort_txt, list_of_user[0])
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


chkr_pas_from_tg(users_data)
