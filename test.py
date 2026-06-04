bank = input("Karta turi:")
naqd_pul = int(input("Naqd pul: "))
usluga = naqd_pul * 0.005

# if bank == 'kapital':
#     usluga
# if bank == 'uzum':
#     usluga
# elif bank == 'universal':
#     usluga = 0

if bank == 'universal':
    usluga = 0
else:
    usluga
total = naqd_pul + usluga
print(f"yechim olindi: {total} so'm")

