a = print("xizmatlarni tanglang: 1] UZS - USD,2] USD - UZS")
x = int(input("Xizmatni tanlang:"))

if x == 1:
    uz = float(input(f"qancha UZS:"))
    usd = uz / 12055
    print(f"{usd:,.2f}")
elif x == 2:
    us = float(input("qancha USD:"))
    usz = us * 12055
    print(round(usz, 2))    
else:
    print("xizmatni noto'g'ri tanladingiz")
