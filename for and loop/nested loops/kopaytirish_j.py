s = int(input("birinchi raqam: "))
e = int(input("oxirgi raqam: "))

for i in range(s,e):
    for d in range(s,e):
        print(f"{i}X{d}={i * d}")