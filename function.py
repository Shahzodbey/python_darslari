#def mal_sorovchi(ism, yosh):
#    """Foydalanuvchidan ismi va yoshini so'rab t_yil topuvchi dastur"""
#    print(f"{ism.title} siz {2020-yosh}-yilda tug'ilgansiz.")
#mal_sorovchi("olim", 25)

#def darajaga_kotar(son):
#    """Sonni kvadrati va kubini topuvchi dastur"""
#   print(f"{son}ning kvadrati {son**2}ga teng.\n"
#          f"{son}ning kubi esa {son**3}ga teng.")
#darajaga_kotar(366)

#def son_tekshir(raqam):
#  """sonni toq yoki juft ekanligini tekshiruvchi dastur"""
    #   if raqam%2 == 0:
    #      print("Bu son juft son.")
#   else:print("Bu son toq son.")
#son_tekshir(123265)

#def katta_kichik(son1, son2):
#    """ikki sonning katta-kichikligini tekshiruvchi dastur"""
#    if son1 > son2:
#        print(f"Sonlardan {son1} katta")
 #   elif son1 < son2:
#       print(f"Sonlardan {son2} katta")
 #   else:print("Bu sonlar teng.")
#katta_kichik(153626, 456989)


#def x_va_y(x = input("Birinchi sonni kiriting:\n"), y = input("Ikkinchi sonni kiriting:\n")):
#    """x va y ni qabul qilib ularni konsolga chiqaruvchi dastur"""
#   print(f"Siz kiritgan sonlar:{x} va {y}")
#x_va_y()

#def x_va_y(x = input("Birinchi sonni kiriting:\n"), y = 2):
#    """x va 2 ni qabul qilib ularni konsolga chiqaruvchi dastur"""
#   print(f"Siz kiritgan sonlar:{x} va {y}")
#x_va_y()


def bolishni_tekshir(sonlar):
    """kiritilgan sonni 2 dan 10 gacha sonlarga qoldiqsiz bo'linishini tekshiruvchi dastur"""
    for n in range(2, 11):
        if not sonlar%n:
            print(f"{sonlar} {n} ga qoldiqsiz bolinadi")

bolishni_tekshir(1245)
