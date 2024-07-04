while True:
    betrag = int(input("Bitte einen Betrag eingeben: "))

    if betrag >= 500:
        rabatt = 0.1
    elif betrag > 100:
        rabatt = 0.05
    else:
        rabatt = 0

    rabattBetrag = int(betrag * rabatt)
    zahlBetrag = int(betrag - rabattBetrag)

    print(f"Bei {betrag}€ beträgt der Rabattbetrag {rabattBetrag}€ und der Zahlbetrag {zahlBetrag}€")
    print("")
