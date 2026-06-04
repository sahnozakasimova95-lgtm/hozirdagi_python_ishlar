a = int(input("uchburchakning A tomonini kiriting: "))
b = int(input("uchburchakning B tomonini kiriting: "))
c = int(input("uchburchakning C tomonini kiriting: "))


if a + b <= c or a + c <= b or c + b <= a:
    print("Uchburchak mavjud emas")
elif a == b == c:
    print("teng tomonli")
elif a == b or a == c or b == c:
    print("teng yongli")
elif a != b != c:
    print("turli tomonli") 
else:
    print("boshqatan urining")