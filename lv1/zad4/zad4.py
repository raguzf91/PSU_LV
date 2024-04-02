#4 zad
file_name = input("Unesite ime tekstualne datoteke: ")
try:
    with open(file_name, 'r') as file:
        count = 0
        total_confidence = 0

        for line in file:
            if line.startswith('X-DSPAM-Confidence:'):
                confidence = float(line.split(':')[1])
                total_confidence += confidence
                count += 1

        if count > 0:
            average_confidence = total_confidence / count
            print("Srednja vrijednost pouzdanosti je:", average_confidence)
        else:
            print("Nema linija oblika X-DSPAM-Confidence u datoteci.")
except FileNotFoundError:
    print("Datoteka nije pronađena.")