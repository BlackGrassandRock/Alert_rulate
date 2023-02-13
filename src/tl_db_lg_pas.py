import pymysql

from src.tl_tg_request import *
from src.tl_config import *

#testing module!!! checking for incorrect password entry


def chkr_pas_from_tg(users_data):
    password_n = pasw_from_bd(users_data)
    if password_n == None or password_n != 0:
        return "ok"
    else:
        request_status_mess_10(users_data)

def edit_nmb_of_lg_attmp(users_data):
    password_n = pasw_from_bd(users_data)
    if password_n == None:
        req_to_bd(users_data)
    elif int(password_n) == 3 or int(password_n) == 2 or int(password_n) == 1:
        update_data(users_data, int(password_n))
    else:
        rem_user(users_data)

# removing a user from the txt lists
def rem_user(val_for_del):
    for i in range(1, 16, 1):
        list = []
        with open("sorce/shed_txt/shed_txt_" + str(i) + ".txt", "r") as f:
            for line in f:
                list.append(line.replace("\n", ""))
        if str(val_for_del) in list:
            list.remove(str(val_for_del))
            with open("sorce/shed_txt/shed_txt_" + str(i) + ".txt", "w") as f:
                for line in list:
                    f.write(line  + "\n")

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
            INSERT INTO nm_of_attempts(Id, Attempts)
            VALUES (%s, %s)
            """
            reviewers_records = [
            (users_data, 3)
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

#Database updating
def update_data(users_data, password_n):
    mydb = pymysql.connect(
        host = "localhost",
        user = DB_USER,
        password = DB_PASS,
        database = DB_BASE,
    )
    mycursor = mydb.cursor()
    update_query = "UPDATE nm_of_attempts SET Attempts = %s WHERE Id = %s"
    val_tuple = (password_n-1, users_data)
    mycursor.execute(update_query, val_tuple)
    mydb.commit()
