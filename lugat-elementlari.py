python_izohli_lugati = {
    "int":"butun son",
    "float":"o'nli son",
    "string":"matn",
    "sort": "tartiblash"
    }
for k, q in sorted(python_izohli_lugati.items()):
    print(f"{k} ning qiymati {q}ga teng.")

info = {
    "Uzbekistan": "Tashkent",
    "USA": "Washington",
    "Japan": "Tokio"
}
print("Davlatlar:")
for dav in sorted(info):
    print(dav.title())
print("Ularning poytaxtlari:")
for poy in sorted(info.values()):
    print(poy.title())

davlatlar = {
    "o'zbekiston":'toshkent',
    'aqsh':'washington d.c.',
    'rossiya':'moskva',
    'tojikiston':'dushanbe',
    "qirg'iziston":'bishkek',
    'qozog\'iston':'nursulton',
    'malayziya':'kuala-lumpur',
    'singapur':'sungapur',
    'italiya':'rim'}
country = input('Qaysi davlatning poytaxtini bilishni istaysiz?:').lower()
capital = davlatlar.get(country)
if capital==None:
    print('Kechirasiz, bizda bu haqida ma\'lumot yo\'q')
else:
    print(f"{country.upper()}ning poytaxti {capital.title()} shahri")

menu = {
    "osh": 15000,
    "somsa": 5000,
    "manti": 2000,
    "sho'rva": 11000,
    "dimlama": 12000,
    "mastava": 10000,
    "shashlik": 9000,
    "grill": 12000,
    "non": 2000,
    'choy': 1000
    }
mijoz = []
for n in range(3):
    mijoz.append(input(f"{n+1}chi buyurtmangiz:>>"))
for buyurtma in mijoz:
    if buyurtma in menu:
        print(f"{buyurtma.title()}ning narxi {menu[buyurtma]} so'm")
    else:print(f"Kechirasiz bizda {buyurtma} yo'q")
