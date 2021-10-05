#amaliyot 1
#print("Kino so'rovchi dastur:")
#savol = "Yoqtirgan kinolaringizni kiriting:>>"
#qiymat = ""
#ishora = True
#while ishora:
#    qiymat = input(savol)
#    if qiymat == 'stop':
#        ishora = False
#    else:print(qiymat)

#amaliyot 2

#question = "Yoshingiz nechchida?>>>"

#while True:
 #   mal = input(question)
  #  if mal == 'stop' or mal == 'quit':
   #     break
    #yosh = int(mal)
#
 #   if yosh < 7:
  #      narh= 2000
   # elif 7 <= yosh < 18:
    #    narh = 3000
    #elif 18 <= yosh < 65:
     #   narh = 10000
   # else:
    #    narh = 0
    #if narh == 0:
     #   print("Siz uchun chipta bepul.")
    #else:
     #   print(f"Siz uchun chipta {narh} so'm")

savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    son = int(qiymat)
    if son < 0:
        continue
    elif qiymat == 'Exit':
        break
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")


