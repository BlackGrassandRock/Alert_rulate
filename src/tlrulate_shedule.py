import schedule
import time

from src.tlrulate_database_upd import *


#writing id to the shedule list
def shed_for_upd(tl_id):
    nm_flow = str(random.randint(1, 15))
    with open("sorce/shed_txt/shed_txt_" + nm_flow + ".txt", mode="a") as f:
        print(tl_id, file=f)

#shedule list counter
def time_nm():
    with open("sorce/shed_nm.txt", mode="r") as f:
        past_nm = int(f.read())
        if past_nm < 15:
            past_nm += 1
        else:
            past_nm = 1
    with open("sorce/shed_nm.txt", mode="w") as f:
        f.write(str(past_nm))
    return past_nm

#shedule
def job():
    nm_flow = str(time_nm())
    with open("sorce/shed_txt/shed_txt_" + nm_flow + ".txt", "r") as f:
        print("сейчас N:", nm_flow)
        for line in f:
            controler(line)

# Run job every 1 second/minute/hour/day/week,
# Starting 1 second/minute/hour/day/week from now
schedule.every(1).minutes.do(job)
