import time
from fractions import Fraction

setup = True
setupInvers = False
setupGaus = False
invers = False
gaus = False
main = True

lin1list = []
lin2list = []
lin3list = []
lin4list = []
lin5list = []
lin6list = []
loesungListc = []
loesungListd = []
loesungListe = []

ja = ["Ja", "ja", "j"]

while main:

    tick = 0
    zwischW15 = 0
    zwischW16 = 0
    zwischW17 = 0

    lin1list.clear()
    lin2list.clear()
    lin3list.clear()
    lin4list.clear()
    lin5list.clear()
    lin6list.clear()

    while setup:
        inInvGaus = input("Invers modus (2x2) oder Gauß modus (3x3)? (Invers / Gauß) ")
        if inInvGaus == "Gauß":
            setupGaus = True
            setup = False
        elif inInvGaus == "Invers":
            setupInvers = True
            setup = False
        else:
            print()
            print("leider ist dies keine Auswahl möglichkeit. Die auswahl möglichkeiten sind 'Invers' oder 'Gauß'.")
            print()

    while setupGaus:
        try:
            print("Nach diesem Schema:")
            print()
            print("I   : x + y + z = Ergebnis")
            print("II  : x + y + z = Ergebnis")
            print("III : x + y + z = Ergebnis")
            print()
            lin11 = input("Wie lautet I : x?: ")
            lin12 = input("Wie lautet I : y?: ")
            lin13 = input("Wie lautet I : z?: ")
            lin14 = input("Wie lautet I : Ergenis?: ")
            lin21 = input("Wie lautet II : x?: ")
            lin22 = input("Wie lautet II : y?: ")
            lin23 = input("Wie lautet II : z?: ")
            lin24 = input("Wie lautet II : Ergenis?: ")
            lin31 = input("Wie lautet III : x?: ")
            lin32 = input("Wie lautet III : y?: ")
            lin33 = input("Wie lautet III : z?: ")
            lin34 = input("Wie lautet III : Ergenis?: ")

            lin1list = [float(lin11), float(lin12), float(lin13), float(lin14)]
            lin2list = [float(lin21), float(lin22), float(lin23), float(lin24)]
            lin3list = [float(lin31), float(lin32), float(lin33), float(lin34)]

            print()
            print("Sieht Ihre Matrix so aus?:")
            print()
            print("I  : ", lin1list[0], "x ", lin1list[1], "y ", lin1list[2], "z  =", lin1list[3])
            print("II : ", lin2list[0], "x ", lin2list[1], "y ", lin2list[2], "z  =", lin2list[3])
            print("III: ", lin3list[0], "x ", lin3list[1], "y ", lin3list[2], "z  =", lin3list[3])
            print()

            if input("(ja / nein): ") in ja:
                setupGaus = False
                gaus = True
            else:
                while tick < 3:
                    print()
                    tick += 1

        except ValueError:
            print()
            print("Leider ist hier eine ungültige Eingabe passiert. Statt , bitte . verwenden.")
            while tick < 3:
                print()
                tick += 1

    while setupInvers:
        try:
            print("Nach diesem Schema:")
            print()
            print("[1, 2]")
            print("[3, 4]")
            print()
            lin11 = input("Wie lautet die erste Zahl?: ")
            lin12 = input("Wie lautet die zweite Zahl?: ")
            lin21 = input("Wie lautet die dritte Zahl?: ")
            lin22 = input("Wie lautet die vierte Zahl?: ")

            lin1list = [float(lin11), float(lin12), float(1), float(0)]
            lin2list = [float(lin21), float(lin22), float(0), float(1)]

            print("Sieht Ihre Matrix so aus?:")
            print()
            print(lin1list[0:2])
            print(lin2list[0:2])
            print()

            if input("(ja / nein): ") in ja:
                setupInvers = False
                invers = True
            else:
                while tick < 3:
                    print()
                    tick += 1

        except ValueError:
            print()
            print("Leider ist hier eine ungültige Eingabe passiert. Statt , bitte . verwenden.")
            while tick < 2:
                print()
                tick += 1

    while gaus:
        zwischW1 = lin2list[0] / lin1list[0] * -1
        zwischW2 = lin1list[0] * zwischW1 + lin2list[0]
        zwischW3 = lin1list[1] * zwischW1 + lin2list[1]
        zwischW4 = lin1list[2] * zwischW1 + lin2list[2]
        zwischW5 = lin1list[3] * zwischW1 + lin2list[3]

        lin4list = [zwischW2, zwischW3, zwischW4, zwischW5]

        zwischW6 = lin3list[0] / lin1list[0] * -1
        zwischW7 = lin1list[0] * zwischW6 + lin3list[0]
        zwischW8 = lin1list[1] * zwischW6 + lin3list[1]
        zwischW9 = lin1list[2] * zwischW6 + lin3list[2]
        zwischW10 = lin1list[3] * zwischW6 + lin3list[3]

        lin5list = [zwischW7, zwischW8, zwischW9, zwischW10]

        zwischW11 = lin5list[1] / lin4list[1] * -1
        zwischW12 = lin4list[1] * zwischW11 + lin5list[1]
        zwischW13 = lin4list[2] * zwischW11 + lin5list[2]
        zwischW14 = lin4list[3] * zwischW11 + lin5list[3]

        lin6list = [lin5list[0], zwischW12, zwischW13, zwischW14]

        print()
        print("I  : ", lin1list[0], "x ", lin1list[1], "y ", lin1list[2], "z  =", lin1list[3])
        print("II : ", lin4list[0], "x ", lin4list[1], "y ", lin4list[2], "z  =", lin4list[3])
        print("III: ", lin6list[0], "x ", lin6list[1], "y ", lin6list[2], "z  =", lin6list[3])
        print()

        if lin6list[0] == 0 and lin6list[1] == 0 and lin6list[2] == 0 and lin6list[3] == 0:
            print()
            print("Unendlich viele Lösungen")
        else:
            if lin6list[2] == 0 or lin6list[3] == 0:
                zwischW15 = 0
            else:
                zwischW15 = lin6list[3] / lin6list[2]

            zwischW16 = lin4list[3] / (lin4list[1] + lin4list[2] * zwischW15)
            zwischW17 = (((lin1list[1] * zwischW16) + (lin1list[2] * zwischW15)) - lin1list[3]) / lin1list[0]

            print("L = {(", zwischW17, "|", zwischW16, "|", zwischW15, ")}")

        if input("Noch ein Gauß? (ja / nein): ") in ja:
            while tick < 3:
                print()
                tick += 1
            setupGaus = True
            gaus = False

        elif input("Möchtest du den Rechenweg sehen? (ja / nein): "):
            while tick < 3:
                print()
                tick += 1
            print("I  : ", lin1list[0], "x ", lin1list[1], "y ", lin1list[2], "z  =", lin1list[3])
            print("II : ", lin4list[0], "x ", lin4list[1], "y ", lin4list[2], "z  =", lin4list[3])
            print("III: ", lin6list[0], "x ", lin6list[1], "y ", lin6list[2], "z  =", lin6list[3])
            print()

            input("Bitte Enter zum fortfahren drücken")

            print()
            print("I  : ", lin1list[0], "x ", lin1list[1], "y ", lin1list[2], "z  =", lin1list[3])
            print("II : ", lin2list[0], "x ", lin2list[1], "y ", lin2list[2], "z  =", lin2list[3], "  | *",
                  Fraction(zwischW1).limit_denominator())
            print("II : ", lin4list[0], "x ", lin4list[1], "y ", lin4list[2], "z  =", lin4list[3])
            print("III: ", lin3list[0], "x ", lin3list[1], "y ", lin3list[2], "z  =", lin3list[3], "  | *",
                  Fraction(zwischW6).limit_denominator())
            print("III: ", lin5list[0], "x ", lin5list[1], "y ", lin5list[2], "z  =", lin5list[3])
            print()

            input("Bitte Enter zum fortfahren drücken")

            print()
            print("I  : ", lin1list[0], "x ", lin1list[1], "y ", lin1list[2], "z  =", lin1list[3])
            print("II : ", lin4list[0], "x ", lin4list[1], "y ", lin4list[2], "z  =", lin4list[3])
            print("III: ", lin5list[0], "x ", lin5list[1], "y ", lin5list[2], "z  =", lin5list[3], "  | *",
                  Fraction(zwischW11).limit_denominator())
            print("III: ", lin6list[0], "x ", lin6list[1], "y ", lin6list[2], "z  =", lin6list[3])
            print()

            input("Bitte Enter zum fortfahren drücken")

            print()
            print("I  : ", lin1list[0], "x ", lin1list[1], "y ", lin1list[2], "z  =", lin1list[3])
            print("II : ", lin4list[0], "x ", lin4list[1], "y ", lin4list[2], "z  =", lin4list[3])
            print("III: ", lin6list[0], "x ", lin6list[1], "y ", lin6list[2], "z  =", lin6list[3])
            print()

            input("Bitte Enter zum fortfahren drücken")
            print()

            if lin6list[0] == 0 and lin6list[1] == 0 and lin6list[2] == 0 and lin6list[3] == 0:
                print("Untersete Zeile hat x, y, z = 0, also:")
                print("Unendlich viele Lösungen")
            else:
                if lin6list[2] == 0 or lin6list[3] == 0:
                    print("z oder das Ergebnis ist = 0, also ist z = 0")
                else:
                    print(lin6list[3], "/", lin6list[2], "z  =", zwischW15, "z")

                print()
                input("Bitte Enter zum fortfahren drücken")

                print()
                print("(", lin4list[1], "y  +", lin4list[2], "*", zwischW15, ") /", zwischW16, "=", zwischW16, "y")
                print("(((", lin1list[1], "*", zwischW16, ") + (", lin1list[2], "*", zwischW15, ")) -", lin1list[3],
                      ") /", lin1list[0], " =", zwischW17, "x")

                print()
                input("Bitte Enter zum fortfahren drücken")

                print()
                print("L = {(", zwischW17, "|", zwischW16, "|", zwischW15, ")}")
                print()

                if input("Noch ein Gauß? (ja / nein)") in ja:
                    while tick < 3:
                        print()
                        tick += 1
                    setupGaus = True
                    gaus = False
                elif input("Rechen-Modus wechseln? (ja / nein): ") in ja:
                    while tick < 3:
                        print()
                        tick += 1
                    gaus = False
                    setup = True
                else:
                    main = False
                    gaus = False

        elif input("Rechen-Modus wechseln? (ja / nein): ") in ja:
            while tick < 3:
                print()
                tick += 1
            gaus = False
            setup = True
        else:
            main = False
            gaus = False

    while invers:
        try:
            zwischW1 = float(lin2list[0] / lin1list[0] * -1)
            zwischW2 = float(lin1list[0] * zwischW1 + lin2list[0])
            zwischW3 = float(lin1list[1] * zwischW1 + lin2list[1])
            zwischW4 = float(lin1list[2] * zwischW1 + lin2list[2])

            lin3list = [zwischW2, zwischW3, zwischW4, 1.0]

            zwischW5 = float(lin1list[1] / zwischW3 * -1)
            zwischW6 = float(zwischW3 * zwischW5 + lin1list[1])
            zwischW7 = float(zwischW4 * zwischW5 + lin1list[2])
            zwischW8 = float(lin3list[3] * zwischW5 + lin1list[3])

            lin4list = [lin1list[0], zwischW6, zwischW7, zwischW8]

            zwischW8 = float(1 / lin4list[0])
            for x in lin4list:
                frac1 = str(Fraction(x * zwischW8).limit_denominator())
                lin5list.append(frac1)

            zwischW9 = float(1 / lin3list[1])
            for y in lin3list:
                frac2 = str(Fraction(y * zwischW9).limit_denominator())
                lin6list.append(frac2)

            print()
            print("Fertige Inverse:")
            print(lin5list[2:])
            print(lin6list[2:])
            print()

            if input("Noch eine Inverse? (ja / nein): ") in ja:
                while tick < 3:
                    print()
                    tick += 1
                setupInvers = True
                invers = False
            else:
                if input("Möchtest du den Rechenweg sehen? (ja / nein): ") in ja:
                    print()
                    print(lin1list)
                    print(lin2list)
                    print()

                    input("Bitte Enter zum fortfahren drücken")

                    for c in lin1list:
                        fracc = str(Fraction(c).limit_denominator())
                        loesungListc.append(fracc)

                    for d in lin3list:
                        fracd = str(Fraction(d).limit_denominator())
                        loesungListd.append(fracd)

                    print()
                    print(loesungListc, "   | * ", str(Fraction(zwischW1).limit_denominator()), "  + x")
                    print(loesungListd)
                    print()

                    input("Bitte Enter zum fortfahren drücken")

                    for e in lin4list:
                        frace = str(Fraction(e).limit_denominator())
                        loesungListe.append(frace)

                    print()
                    print(loesungListe)
                    print(loesungListd, "   | * ", str(Fraction(zwischW5).limit_denominator()), "  + x")
                    print()

                    input("Bitte Enter zum fortfahren drücken")

                    print()
                    print(lin5list, "   | * ", str(Fraction(zwischW8).limit_denominator()))
                    print(lin6list, "   | * ", str(Fraction(zwischW9).limit_denominator()))
                    print()

                    input("Bitte Enter zum fortfahren drücken")

                    print()
                    print(lin5list)
                    print(lin6list)
                    print()

                    if input("Noch eine Inverse?: (ja / nein) ") in ja:
                        while tick < 3:
                            print()
                            tick += 1
                        setupInvers = True
                        invers = False
                    elif input("Rechen-Modus wechseln?: (ja / nein) ") in ja:
                        while tick < 3:
                            print()
                            tick += 1
                        invers = False
                        setup = True
                    else:
                        main = False
                        invers = False

                elif input("Rechen-Modus wechseln? (ja / nein) ") in ja:
                    while tick < 3:
                        print()
                        tick += 1
                    invers = False
                    setup = True
                else:
                    main = False
                    invers = False
        except ZeroDivisionError:
            print()
            print("Diese Matrix hat leider keine Inverse")
            print()

            time.sleep(1)

            if input("Soll der Grund erklärt werden? (ja / nein) ") in ja:
                determin = lin1list[0] * lin2list[1] - lin1list[1] * lin2list[0]
                print()
                print("(", lin1list[0], "*", lin2list[1], ") - (", lin1list[1], "*", lin2list[0], ") =", determin)
                print()

            if input("Noch eine Inverse? (ja / nein) ") in ja:
                while tick < 3:
                    print()
                    tick += 1
                setupInvers = True
                invers = False
            elif input("Rechen-Modus wechseln? (ja / nein) ") in ja:
                while tick < 3:
                    print()
                    tick += 1
                invers = False
                setup = True
            else:
                main = False
                invers = False
