klub1 = input("Klub A : ")
klub2 = input("Klub B : ")
winner = []
i = 1
x = 1
while True:
    skor1, skor2 = map(int,input("Pertandingan {} : ".format(i)).split())
    i+=1
    if skor1 < 0 or skor2 < 0:
        break
    elif skor1 > skor2:
        winner.append(klub1)
    elif skor1 < skor2:
        winner.append(klub2)
    elif skor1 == skor2:
        winner.append("Draw")
for win in winner:
    print("Hasil ",x," : ",win)
    x+=1
print("Pertandingan selesai")
