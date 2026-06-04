import os
import pathlib
from datetime import datetime

def log_yozish(daraja, xabar):
    now = datetime.now()
    current = pathlib.Path(__file__)
    file_nomi = now.strftime("log_%Y_%m_%d.txt")
    vaqt = now.strftime("[%Y-%m-%d %H:%M:%S]")
    yozuv = f"{vaqt} [daraja] {xabar}\n"
    current_dir = os.path.join(current,file_nomi)

    with open(file_nomi, "a", encoding="utf-8") as file:
        back = file.write(yozuv)
        print(back)

log_yozish("INFO", "Foydalanuvchi tizimga muvaffaqiyatli kirdi.")
log_yozish("ERROR", "Ma'lumotlar bazasiga ulanishda xatolik!")


