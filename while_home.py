buyurtma = []
n = 1
while True:
    savol = f'{n}-chi taomni kiriting:\n'
    tovar = input(savol)
    buyurtma.append(tovar)
    javob = input("Yana qoshishni xoxlaysizmi?")

    if javob == 'ha':
        n += 1
        continue
    else:
        break

e_bozor = {}
ishora = True
while ishora:
    mahsulot = input('Mahsulot nomini kiriting:\n')
    narh = input(f'{mahsulot}ning narhini kiriting:\n')
    e_bozor[mahsulot] = int(narh)
    javoblar = input("Yana malumot qoshasizmi?\n")
    if javoblar != "yoq":
        continue
    else:break

buyurtmalar = ["olma", "osh", "tufli", "atir"]
mahsulotlar = {"olma": 15000, "tuz": 2000, "tufli": 150000, "asal": 300000}
while buyurtmalar:
    buyum = buyurtmalar.pop()
    if buyum in mahsulotlar.keys():
        narx = mahsulotlar[buyum]
        print(f"{buyum.title()}ning narxi {narx} so'm")
    else:print("Bizda bunday mahsulot yoq")

