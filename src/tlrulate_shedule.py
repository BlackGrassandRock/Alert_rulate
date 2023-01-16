import schedule
import time
import tlrulate_database_upd


#writing id to the shedule list
def shed_for_upd(tl_id):
    nm_flow = str(random.randint(1, 15))
    shed_dict = tl_id
    with open("shed_txt/shed_txt_" + nm_flow + ".txt", mode="a") as f:
        print(shed_dict, file=f)

#shedule list counter
def time_nm():
    with open("shed_nm.txt", mode="r") as f:
        nm = int(f.read())
        past_nm = nm
        if nm < 15:
            nm += 1
        else:
            nm = 1
        nm = str(nm)
    with open("shed_nm.txt", mode="w") as f:
        f.write(nm)
    return past_nm

#shedule
def job():
    nm_flow = str(time_nm())
    with open("shed_txt/shed_txt_" + nm_flow + ".txt", "r") as f:
        for line in f:
            tlrulate_database_upd.controler(line)

# Run job every 1 second/minute/hour/day/week,
# Starting 1 second/minute/hour/day/week from now
schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
