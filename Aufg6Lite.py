while True:
    betrag = int(input("Bitte einen Betrag eingeben: "))

    if betrag >= 500:
        print(f"Bei {betrag}€ beträgt der Rabattbetrag {betrag * 0.1}€ und der Zahlbetrag {betrag - (betrag * 0.1)}€")
    elif betrag > 100:
        print(f"Bei {betrag}€ beträgt der Rabattbetrag {betrag * 0.05}€ und der Zahlbetrag {betrag - (betrag * 0.05)}€")
    else:
        print(f"Bei {betrag}€ beträgt der Rabattbetrag 0€ und der Zahlbetrag {betrag}€")
        print("")
