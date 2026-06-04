import random

a = 0
while a <= 100:
    r_n = random.randint(1,100)
    n = int(input(f"son kiriting:{r_n}:"))
    if r_n == n:
        print("to'gri")
        break
    else:
        print("xato")
