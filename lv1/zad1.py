#1 zad

'''
radniSati = float(input("Unesite radne sate: "))
satnica = float(input("Unesite satnicu: "))
zarada = radniSati * satnica
print("Ukupno: " + str(zarada) + "eura")
'''
def total_euro(radniSati, satnica):
    print("Ukupno: " + str(radniSati*satnica) + "eura")

def main():

    radniSati = float(input("Unesite radne sate: "))

    satnica = float(input("Unesite satnicu: "))

    total_euro(radniSati, satnica)
   
main()