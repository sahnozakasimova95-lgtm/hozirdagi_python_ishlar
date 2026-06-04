parol = "hello"
sorov = str(input("parolni kiriting: "))
while parol != sorov:
    print("parol xato parolni qaytatan kiriting")
    sorov = str(input("parolni kiriting: "))
if parol == sorov:
    print("to'g'ri")