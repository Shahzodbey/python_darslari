yangi_cars = ["toyota", "mazda", "hyundai", "gm", "kia"]
for avto in yangi_cars:
    if avto != "gm":
        print(avto.title())
    else:print(avto.upper())

#login = (input("Ismingizini kiriting:\n"))
#if login.lower == "admin":
   # print(f"Xush kelibsiz {login.title()} foydalanuvchilar ro'yxatini ko'rasizmi?")
#else:print(f"Xush kelibsiz {login}")

#a = int(input("Birinchi sonni kiriting:\n"))
#b = int(input("Ikkinchi sonni kiriting:\n"))
#if a==b:
    #print("sonlar teng")

#son = int(input("Xoxlagan soningizni kiriting:\n"))
#if son>0:
#    print("Bu son musbat")
#else:print("Bu son manfiy")

son = int(input("Sonni kiriting:\n"))
if son>0:
    print(son**(1/2))
else:print("Musbat son kiriting")