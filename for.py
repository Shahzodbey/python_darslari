dostlar = ["Ali", "Vali", "Alisher", "SHerali", "Bahodir"]
for dost in dostlar:
    print(f"Salom {dost} tuzukmisan")
print(f"kod {len(dostlar)} marta takrorlandi")

toq_sonlar = list(range(11, 100, 2))
for son in toq_sonlar:
    print(son**3)
print(toq_sonlar)

n_odamlar = int(input("Bugun necha kishi bilan suhbatlashdingiz?"))
ismlar = []
for n in range(n_odamlar):
    ismlar.append(input(f"{n+1}-chi odam\n"))
print(ismlar)

kinolar = []
print("5 ta sevimli kinoingiz qaysilar?")
for k in range(5):
    kinolar.append(input(f"{k+1}-kino:"))
print(kinolar)
