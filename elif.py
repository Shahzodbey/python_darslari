#son = int(input("Sonni kiriting "))
#if son%2:
#    print("Bu juft son emas")
#else:print("Rahmat")

#yosh = int(input("Yoshingiz nechchida?\n"))
#if yosh<4 or yosh>60:
#    print("Siz uchun bepul")
#elif yosh<18:
#    print("Siz uchun 10000 so'm")
#elif yosh>18:
 #   print("Siz uchun 20000 so'm")

#asoni = int(input("Birinchi sonni kiriting\n"))
#bsoni = int(input("Ikkinchi sonni kiriting\n"))
#if asoni ==bsoni:
#    print(f"{asoni} ga {bsoni}")
#elif asoni>bsoni:
#    print(f"{asoni} {bsoni}dan katta")
#elif asoni<bsoni:
#    print(f"{asoni} {bsoni}dan kichik")

#mahsulotlar = ["olma", "shokolad", "tuz", "gugurt", "shakar", "yog'", "un", "non", "choy", "novot"]
#yangi_savat = []
#for n in range(5):
#    yangi_savat.append(input(f"{n+1} chi mahsulotni kiriting\n"))
#for mahsulot in yangi_savat:
#    if mahsulot in mahsulotlar:
#        print("Mahsulot bor")
#    else:print("Mahsulot yo'q")


foydalanuvchilar = ["ali", "vali", "alisher", "shahzod", "aziz"]
login = input("Yangi login tanlang:\n")
if login.lower() in foydalanuvchilar:
    print("Login band bo'lgan ")
else:print("Xush kelibsiz")

mahsulotlar = ["olma", "shokolad", "tuz", "gugurt", "shakar", "yog'", "un", "non", "choy", "novot"]
smahsulot = []
for n in range(5):
  smahsulot.append(input(f"{n+1} chi mahsulotni kiriting:\n"))
b_mahsulotlar =[]
y_mahsulotlar =[]
for smah in smahsulot:
    if smah in mahsulotlar:
        b_mahsulotlar.append(smah)
    else:y_mahsulotlar.append(smah)
if y_mahsulotlar:
     print(f"Bizda bular yo'q")
     for smah in y_mahsulotlar:
       print(smah)
else:print(f"Bizda bularni hammasi bor ")

mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

bor_mahsulotlar = []
mavjud_emas = []
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)

if mavjud_emas:
  print(f"Do'konimizda quyidagi mahsulotlar yo'q:")
  for mahsulot in mavjud_emas:
    print(mahsulot)
else:
  print("Siz so'ragan barcha mahsulotlar do'konimizda bor")