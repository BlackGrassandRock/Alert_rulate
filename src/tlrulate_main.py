import tlrulate_selenium
import tlrulate_request
import tlrulate_database
import tlrulate_telegram_bot

id_usr = ['635346942'] #tests data

def main():
    data = tlrulate_database.answ_from_bd(id_usr[0])
#    new_usr_data = tlrulate_selenium.parser(data[0:4])
#    sorted_all_data, sort_new_dt = tlrulate_database.comparison_data(data, new_usr_data)




if __name__ == '__main__':
    main()
