p = str(input("parolni kiriting: "))

if len(p) >= 8 and any(char.isdigit() for char in p):
    print("parol to'g'ri")
elif len(p) < 8 and any(char.isdigit() for char in p):
    print