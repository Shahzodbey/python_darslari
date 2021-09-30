#ismlar = ["Bahodir", "Sherali", "Me"]
#print("Bugun tennisga borasanmi", ismlar[0])
#print(ismlar[1], "ishlaring yaxshimi?")
#print("Yeah it is ", ismlar[2])

#sohlarga doir
#sonlar =[-25, 58, 22, 26.6]
#sonlar[-1] = 27
#print(sonlar[-1])
#print(sonlar[0] + 225)
#sonlar.append(250)
#sonlar.insert(-2, 366)
#print(sonlar)

#pop ga doir
#t_shaxslar = ["Ali", "Botir", "Charlie"]
#z_shaxslar = ["Z", "X", "Doniyor"]
#print("Men tarixiy shaxslardan ", t_shaxslar.pop(1), "bilan, zamonaviy shaxslardan", z_shaxslar.pop(-1), "bilan suhbatlashishni xoxlayman")

friends =[]
friends.append("Ali")
friends.append("Alisher")

friends.remove("Ali")
friends.insert(0, "Messi")
friends.insert(2, "Ronaldo")
mehmonlar =[]
mehmonlar.append("Akam")
mehmonlar.append("Qo'shni")
mehmonlar.append(friends.pop(2))
print(mehmonlar)