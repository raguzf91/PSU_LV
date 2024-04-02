#3 zad

brojac = 0
lista = []
while(1):
    broj = input("Unesi broj: ")
    if broj == 'Done':
        break
    try:
        num = float(broj)
        lista.append(num)
    except ValueError:
        print("Neispravan unos. Unesite broj: ")


print("Lista: ", lista)
print("Broj unesenih brojeva: ", len(lista))
print("Minimalna vrijednost: ", min(lista))
print("Maksimalna vrijednost: ", max(lista))
print("Srednja vrijednost: ", sum(lista)/len(lista))
lista.sort()
print("Sortirana lista: ", lista)