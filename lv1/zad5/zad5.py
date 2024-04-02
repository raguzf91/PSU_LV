#5 zad
def rjecnik(fileName):
    listaRijeci = {}
    posebneRijeci = []

    for line in fileName:
        sadrzaj = line.strip().split()

        for rijec in sadrzaj:
            if rijec in listaRijeci:
                listaRijeci[rijec] += 1
            else:
                listaRijeci[rijec] = 1
    
    for rijec, brojac in listaRijeci.items():
        if brojac == 1:
            posebneRijeci.append(rijec)
    
    #print(listaRijeci)

    return posebneRijeci

fileName = open('song.txt', 'r')
posebneRijeci = rjecnik(fileName)

print("Broj rijeci koje se pojavljuju samo jednom: ", len(posebneRijeci))
print("Rijeci koje se pojavljuju samo jednom: ")
for rijec in posebneRijeci:
    print(rijec)