f1 = "oddiy"
f2 = "student"
f3 = "pensioner"

chegirma1 = 0.10
chegirma2 = 0.15


foydalanuvchi = str(input(f"foydalanuvchini kiriting(1.{f1},2.{f2},3.{f3}) :"))
narx = int(input(f"{foydalanuvchi} qancha narx boldi: " ))
b = narx - (narx * chegirma1)
c = narx - (narx * chegirma2)


if foydalanuvchi == f1:
    print("sizga chegirma yo'q")
elif foydalanuvchi == f2:
    print(f"sizga {b} boldi chunki sizga 10% chegirma bor")
elif foydalanuvchi == f3:
    print(f"sizga {c} boldi chunki sizga 15% chegirma bor")
else:
    print("iltimos boshqatan urining")


0.85