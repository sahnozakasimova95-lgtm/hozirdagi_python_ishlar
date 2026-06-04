#dictionary
data = {
    "kompaniya": "Tech Solutions LLC",
    "bino_manzili": {
        "mamlakat": "O'zbekiston",
        "shahar": "Toshkent",
        "tumani": "Mirobod",
        "kocha": "Amir Temur",
        "uy": 45
    },
    "faolmi": True,
    "hodimlar_soni": 3,
    "hodimlar": [
        {
            "id": 1024,
            "ism": "Laylo",
            "email": "laylo@example.com",
            "lavozimi": "Senior Team Lead",
            "maorif": {
                "daraja": "Magistr",
                "universitet": "TUIT"
            },
            "manzil": {
                "shahar": "Toshkent",
                "tumani": "Mirobod",
                "kocha": "Amir Temur"
            },
            "qiziqishlari": ["shaxmat", "kitobxonlik", "sayohat"],
            "ko'nikmalari": ["Python", "Django", "PostgreSQL", "Docker"],
            "faolmi": True
        },
        {
            "id": 1025,
            "ism": "Asadbek",
            "email": "asadbek@example.com",
            "lavozimi": "Frontend Developer",
            "maorif": {
                "daraja": "Bakalavr",
                "universitet": "Inha"
            },
            "manzil": {
                "shahar": "Samarqand",
                "tumani": "Siyob",
                "kocha": "Registon"
            },
            "qiziqishlari": ["futbol", "kibersport", "fotosurat"],
            "ko'nikmalari": ["JavaScript", "React", "Tailwind CSS", "Git"],
            "faolmi": True
        },
        {
            "id": 1026,
            "ism": "Malika",
            "email": "malika@example.com",
            "lavozimi": "UI/UX Designer",
            "maorif": {
                "daraja": "Bakalavr",
                "universitet": "WIUT"
            },
            "manzil": {
                "shahar": "Toshkent",
                "tumani": "Chilonzor",
                "kocha": "Qatortol"
            },
            "qiziqishlari": ["rasm chizish", "raqs", "psixologiya"],
            "ko'nikmalari": ["Figma", "Adobe XD", "Illustrator", "Prototyping"],
            "faolmi": False
        }
    ],
    "loyihalar": [
        {
            "nomi": "E-Kompaniya Portal",
            "status": "Tugallangan",
            "byudjet_usd": 15000
        },
        {
            "nomi": "Mobil Ilova CRM",
            "status": "Jarayonda",
            "byudjet_usd": 28000
        }
    ]
}

# print(f'2.qiziqisjlari')
# for raqam, qiziqish in enumerate(['qiziqishlari']start=1):

print(data["kompaniya"])
print("bino_manzili")
print(f"{data["bino_manzili"]['mamlakat']} mamlakat,{data["bino_manzili"]['shahar']} shahar,{data["bino_manzili"]['tumani']} tuman,{data["bino_manzili"]['kocha']} kochasi,{data["bino_manzili"]['uy']} uy")
# for son,loyihalar in enumerate(data["loyihalar"],start = 1):
    # print(f'\t{son}:{loyihalar} ')
print(f"faolmi:{data['faolmi']}")
print(f"hodimlar soni {data['hodimlar_soni']} ta")
print(f"hodimlar")
for key , val in enumerate(data['hodimlar'], start=1):
    print(f"\t{key} -- {val['ism']}")
    for idv , va in val.items():
        print(f"\t\t{idv} -- {va}") 
# for idx, row in enumerate(data['hodimlar'], start=1):
    # print(f"\t{idx}. {row["ism"]}: ")
    # for key, val in row.items():
        # print(f"\t\t{key}: {val}")
# print(f"Loyihalar soni: {len(data['loyihalar'])} ta.")
# for idx, row in enumerate(data['loyihalar'], start=1):
    # print(f"\t{idx}. {row['nomi']}")
    # for key, val in row.items():
        # print(f"\t\t{key}: {val}")
