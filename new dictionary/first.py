# dic = {
#     "id": 501,
#     "ism": "Aziz",
#     "email": "aziz@example.com",
#     "tugilgan yil": 2005,
#     "manzil": {
#         "shahar": "Toshkent",
#         "tumani": "Yakkasaroy",
#         "kocha": "Buyuk Turon"
#     },
#     "qiziqishlari": ["dasturlash", "futbol", "kitobxonlik"],
#     "faolmi": True
# }
# print(f"foydalanuvchi malumoti:")
# print(f"1. Ismi[{dic["id"]}]: {dic["ism"]}")
# print(f"2. Manzil: {dic["manzil"]['shahar']} shaxar,{dic["manzil"]['tumani']} tuman,{dic["manzil"]['kocha']} ko'chasi")
# print(f"3 Qiziqishlar:")
# for key,val in enumerate(dic['qiziqishlari'],start=1):
#     print(f"\t {key}.{val} ")
# print(f"4. Hisob faol:{dic["faolmi"]}")

# Online do'kon

# dic = {
#     "dokon_nomi": "Texno Market",
#     "manzil": "Toshkent, Chilonzor-8",
#     "faolmi": True,
#     "mahsulotlar": [
#         {"nomi": "Noutbuk", "narx" : 7500000 , "miqdor": 5},
#         {"nomi": "Smartfon", "narx" : 4200000 , "miqdor": 8},
#         {"nomi": "Quloqchin", "narx" : 2500000 , "miqdor": 12},
#     ]
# }
# print(f"\tDo'kon: {dic["dokon_nomi"]}")
# print(f"\tManzil: {dic["manzil"]}")
# print(f"\tFaolmi: {dic["faolmi"]}")
# print(f"\tMahsulotlar:")
# for i in dic["mahsulotlar"]:
#     print(i["nomi"], "-", i["narx"], "so'm","Qoldiq",i["miqdor"] ) 
# print("______________________________________________")
# print(f'\n Jami mahsulotlar soni: 3ta')

# kutubxona

# dic = { 
#     "kutubxona": "Ziyo Kutubxonasi",
#     "manzil": "Toshkent, Yunusobod",
#     "kitoblar": [
#         {"nomi": "Alkimyogar","muallif":"Paulo Coelho", "yil": 1988},
#         {"nomi": "1984","muallif":"George Orwell", "yil": 1949},
#         {"nomi": "Don Kixot","muallif":"Migel de Servantes", "yil": 1605},
#     ],
#     "a'zolar_soni": 120
# }

# print(f"Kutubxona: {dic["kutubxona"]}")
# print(f"Manzil: {dic["manzil"]}")
# print(f"A'zolar soni: {dic["a'zolar_soni"]}")
# print(f"Kitoblar ro'yxati:")
# for s,i in enumerate(dic["kitoblar"], start=1):
#     print(s,".",i["nomi"],"----",i["muallif"],"(",i["yil"],")")







# terma_jamoa_raqamlari = {
#     1: "O'tkir Yusupov",
#     2: "Muhammadqodir Hamraliyev",
#     3: "Hojiakbar Alijonov",
#     4: "Farrux Sayfiyev",
#     5: "Rustam Ashurmatov",
#     7: "Otabek Shukurov",
#     9: "Odiljon Hamrobekov",
#     10: "Jaloliddin Masharipov",
#     11: "Oston O'runov",
#     12: "Abduvohid Ne'matov",
#     13: "Umar Eshmurodov",
#     14: "Eldor Shomurodov",
#     15: "Abduqodir Husanov",
#     21: "Botirali Ergashev",
#     22: "Abbosbek Fayzullayev"
# }
# # print(terma_jamoa_raqamlari.keys())
# # print(terma_jamoa_raqamlari.values())
# # print(terma_jamoa_raqamlari.items())
# # terma_jamoa_raqamlari.clear()
# # print(terma_jamoa_raqamlari)

# dic = {
#     1:"1.manzura",
#     2:"2.sanjar",
#     3:"3.firdavs",
#     "qiziqishlar": [
#         {"qiziqish":"futboll"}
#     ]
# }
# print(f"{dic.keys()}")
# print(f"{dic.values()}")
# print(f"{dic.update()}")
# print(f"{dic.copy()}")
# print(f"{dic.items()}")
# print(f"1.{dic.pop(1)}")
# print(f"{dic.pop(2)}")
# print(f"{dic.pop("qiziqishlar")}")

diceng = {
    "apple":"olma",
    "school":"maktab",
    "water":"suv",
    "good":"yaxshi",
    "big":"katta",
    "book":"kitob",
    "teacher":"ustoz",
    "student":"talaba"
}
dicuz = {
    "olma":"apple",
    "maktab":"school",
    "suv":"water",
    "yaxshi":"good",
    "katta":"big",
    "kitob":"book",
    "ustoz":"teacher",
    "talaba":"student",
}


print("tarjima qilmoqchi bo'lgan so'zingiz: ")
choose = int(input("1)ENG/2)UZB:"))
if choose == 1:
    while True:
        word = input("tarjima qilmoqchi bo'lgan so'zingiz: ")
        print(f"ENG:{word}--UZB:{diceng.get(word)}")
        if diceng.get(word) == None:
            print("Yangi so'z qo'shishni xohlaysizmi:HA/YOQ")
            add = input("Javob:")
            if add == "HA":
                engtr = input("englishchasi:").lower()
                uzbtr = input("uzbekchasi:").lower()
                diceng[engtr] = uzbtr
                print(f"lug'at qo'shildi:{diceng.popitem()}")
                break
            elif add == "YOQ":
                break
elif choose == 2:
    while True:
        word = input("tarjima qilmoqchi bo'lgan so'zingiz: ")
        print(f"UZB:{word}--ENG:{dicuz.get(word)}")
        if dicuz.get(word) == None:
            print("Yangi so'z qo'shishni xohlaysizmi:HA/YOQ")
            add = input("Javob:")
            if add == "HA":
                uzbtr = input("uzbekchasi:").lower()
                engtr = input("englishchasi:").lower()
                dicuz[uzbtr] = engtr
                print(f"lug'at qo'shildi:{dicuz.popitem()}")
                break
            elif add == "YOQ":
                break
else:
    print("error")
            