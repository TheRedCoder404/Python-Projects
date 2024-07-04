while True:
    jahr = int(input("Bitte Jahreszahl eingeben: "))

    check1 = False
    check2 = False
    check3 = False

    methode = ""

    if jahr / 4 == int(jahr / 4):
        check1 = True
        methode = "teilbar durch 4"
    if jahr / 100 == int(jahr / 100):
        check2 = True
        methode = "teilbar durch 4 und 100"
    if jahr / 400 == int(jahr / 400):
        check3 = True
        methode = "teilbar durch 4, 100 und 400"
    if not check1 and not check2 and not check3:
        methode = "teilbar durch keiner der Kriterien"

    if check1:
        if check2:
            if check3:
                print(f"Das Jahr {jahr} ({methode}) ist ein Schaltjahr!")
            else:
                print(f"Das Jahr {jahr} ({methode}) ist kein Schaltjahr!")
        else:
            if check3:
                print(f"Das Jahr {jahr} ({methode}) ist kein Schaltjahr!")
            else:
                print(f"Das Jahr {jahr} ({methode}) ist ein Schaltjahr!")
    else:
        print(f"Das Jahr {jahr} ({methode}) ist kein Schaltjahr!")
    print("")
