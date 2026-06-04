f1 = "oddiy"
f2 = "student"
f3 = "pensioner"

chegirma1 = 0.10
chegirma2 = 0.15


foydalanuvchi = int(input(f"foydalanuvchini kiriting(1.{f1},2.{f2},3.{f3}) :"))
narx = int(input(f"{foydalanuvchi} qancha narx boldi: " ))
b = narx - (narx * chegirma1)
c = narx - (narx * chegirma2)


if foydalanuvchi == 1:
    pass
elif foydalanuvchi == 2:
    b
elif foydalanuvchi == 3:
    c

