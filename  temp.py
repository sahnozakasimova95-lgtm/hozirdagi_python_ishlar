temp = int(input("temperatura:"))

if temp > 30:
    print(f"{temp} issiq")
elif temp < 0:
    print(f"{temp} juda sovuq")
elif temp == 0:
    print(f"{temp} sovuq")
elif temp <= 15:
    print(f"{temp} sovuq")
elif temp > 15:
    print(f"{temp} illiq")
elif temp <= 30:
    print(f"{temp} illiq")

else:
    print("boshqatan kiriting")