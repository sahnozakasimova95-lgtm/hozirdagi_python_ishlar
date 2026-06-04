import datetime
import os
import pathlib

current_dir = pathlib.Path(__file__).parent
current_file = "parkovka.txt"
combine = os.path.join(current_dir,current_file)

def mashina_keldi(davlat_raqami):
    current_time = datetime.datetime.now()
    vaqt = current_time.strftime("[%Y-%m-%d %H:%M:%S]")
    two_hours_later = current_time + datetime.timedelta(hours=2)
    vaqt2 = two_hours_later.strftime("[%Y-%m-%d %H:%M:%S]")
    hour = current_time.hour
    hour2 = two_hours_later.hour
    print(hour,hour2)
    a = hour2 - hour    
    Kirish = True
    if Kirish == True:
        with open(combine,"a",encoding="utf-8") as file:
            file.write(f"{vaqt},Kirish,{davlat_raqami} avtoturargohga kirdi \n")
        with open(combine,"a",encoding="utf-8") as file:
            file.write(f"{vaqt2},chiqish,{davlat_raqami} avtoturargohga chiqdi \n")
    with open(combine,"a",encoding="utf-8") as file:
        file.write(f"parkovka 1soat 10 min ,shunda siz {a}-soat o'tirdingiz shunda siz:{10 * a} ming to'lashingiz kerak\n \n")

mashina_keldi("01,A,777,AA")
