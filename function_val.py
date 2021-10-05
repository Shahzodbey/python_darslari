def raange(x, y, z=1):
    sonlar =[]
    while x < y:
        if z==None:
            sonlar.append(x)
            x += 1
        elif z != None:
            sonlar.append(x)
            x += z
    return sonlar

print(raange(3, 20, 2))


