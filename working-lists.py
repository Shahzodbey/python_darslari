davlatlar = ["USA", 'UZBEKISTAN', 'JAPAN']
print(len(davlatlar))
print(sorted(davlatlar))
#davlatlar.sort(reverse=True)
#print(davlatlar)
print(sorted(davlatlar, reverse=True))
print(sorted(davlatlar, reverse=False))
print(davlatlar)
davlatlar.reverse()
print(davlatlar)
davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)

sonlar = list(range(120, 1200))
print(sonlar)
print(sum(sonlar))
print(max(sonlar)-min(sonlar))
print(len(sonlar))
print(sonlar[:15])

taomlar = ["osh", "sho'rva", "manti", "somsa"]
tushlik = taomlar[:]
print(tushlik)
tushlik.append("shashlik")
print(tushlik)
print(taomlar)
tushlik.remove("osh")
print(tushlik)

tushlik[0] = "non va qaymoq"
tushlik = tuple(tushlik)
print(tushlik)