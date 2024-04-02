#6 zad
def main():
    # Inicijalizacija varijabli za brojanje riječi i poruka
    total_words_ham = 0
    total_words_spam = 0
    total_ham_messages = 0
    total_spam_messages = 0
    exclamatory_spam_count = 0

    # Učitavanje datoteke SMSSpamCollection.txt
    filename = "SMSSpamCollection.txt"
    try:
        with open(filename, 'r') as file:
            # Čitanje datoteke po linijama
            for line in file:
                # Razdvajanje oznake (ham ili spam) od sadržaja poruke
                label, message = line.split('\t')
                # Brojanje riječi u poruci
                word_count = len(message.split())
                # Ažuriranje ukupnog broja riječi i poruka ovisno o oznaci
                if label == 'ham':
                    total_words_ham += word_count
                    total_ham_messages += 1
                elif label == 'spam':
                    total_words_spam += word_count
                    total_spam_messages += 1
                    # Provjera je li spam poruka završava uskličnikom
                    if message.strip().endswith('!'):
                        exclamatory_spam_count += 1

        # Izračun prosječnog broja riječi u ham i spam porukama
        average_words_ham = total_words_ham / total_ham_messages
        average_words_spam = total_words_spam / total_spam_messages

        # Ispis rezultata
        print("Prosječan broj riječi u ham porukama:", average_words_ham)
        print("Prosječan broj riječi u spam porukama:", average_words_spam)
        print("Broj spam poruka koje završavaju uskličnikom:", exclamatory_spam_count)

    except FileNotFoundError:
        print(f"Datoteka '{filename}' nije pronađena.")

main()