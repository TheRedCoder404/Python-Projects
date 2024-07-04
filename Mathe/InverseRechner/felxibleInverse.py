from time import sleep
from fractions import Fraction
import os
os.system("")

origListList = [[], [], [], [], [], [], [], []]
listListr1 = [[], [], [], [], [], [], [], []]
listListr2 = [[], [], [], [], [], [], [], []]
listListr3 = [[], [], [], [], [], [], [], []]
listListSch = [[], [], [], [], [], [], [], []]
determWerte = [[], [], [], [], [], [], [], []]

zwischenwertLst = []

ja = ["Ja", "ja", "j"]

groesse = 0
tick = 0
runde = 0
determWert = 0

determRech = ""

lnUp = '\033[1A'
lnClear = '\x1b[2K'

main = True
setup = True
matrixGroesse = True
rechnung = False

counter = 1

while main:
    while setup:
        for i in origListList:
            i.clear()
        for i in listListr1:
            i.clear()
        for i in listListr2:
            i.clear()
        for i in listListr3:
            i.clear()
        for i in listListSch:
            i.clear()
        zwischenwertLst.clear()

        groesse = ""

        grWiedHol = 0
        counterX = 0
        counterY = 0

        try:
            while matrixGroesse:
                groesse = int(input("Welche größe hat die Matrix? "))
                while counter > 0:
                    print(lnUp, end=lnClear)
                    counter -= 1
                if groesse < 2 or groesse > 8:
                    print("Ungültige Matrix größe")
                    counter += 2
                else:
                    grWiedHol = groesse ** 2
                    while grWiedHol > 0:
                        origListList[counterY].append(float(1 if counterX == counterY else 0))
                        counterX += 1
                        grWiedHol -= 1
                        if counterX == groesse:
                            counterY += 1
                            counterX = 0
                    matrixGroesse = False

        except ValueError:
            print("Ungültige Matrix größe")
            print()
            counter += 2

        counterY = 0
        counterX = 0

        for i in origListList:
            if i:
                for n in origListList[counterY]:
                    counter += 1
                    listListSch[counterY].append(counter)
                    counterX += 1
                counterY += 1

        print("Bitte die Zahlen dach diesem Schema eingeben:")
        for i in listListSch:
            if i:
                print(i)
        print("")

        try:
            counterY = 0
            counterX = -1

            for i in listListSch:
                if i:
                    for n in i:
                        if counterX < groesse - 1:
                            counterX += 1
                        else:
                            counterX = 0
                        inForMatrix = float(input(f"Bitte Zahl nummer {(listListSch[counterY])[counterX]} Eingeben: "))
                        print(lnUp, end=lnClear)
                        origListList[counterY].insert(counterX, inForMatrix)
                    counterY += 1

            tick = 4
            while tick > 0:
                print(lnUp, end=lnClear)
                tick -= 1

            for i in origListList:
                if i:
                    print(i[0:groesse])
            print("")

            if input("Ist die Matrix so Richtig? ") in ja:
                tick = 4
                while tick > 0:
                    print(lnUp, end=lnClear)
                    tick -= 1

                print("Start Matrix:")
                for i in origListList:
                    if i:
                        print(i[0:groesse])

                rechnung = True
                setup = False
            else:
                counter = 6
                matrixGroesse = True
                print()

        except ValueError:
            print("Da ist wohl leider eine Falsche Eingabe passiert :-/ ...")

    while rechnung:
        try:
            counterY = 0
            counterX = 0

            for i in origListList:
                if i:
                    if counterY > 0:
                        for n in origListList[counterY - 1]:
                            listListr1[counterY].append((float(n) * float(zwischenwertLst[counterY - 1]) +
                                                         (origListList[counterY])[counterX]))
                            counterX += 1
                            if counterX == groesse * 2:
                                counterX = 0
                    else:
                        listListr1[0] = origListList[0]
                        zwischenwertLst.append((float((origListList[counterY + 1])[0]) / float(i[0]) * -1))
                    counterY += 1

            counterY = 0
            counterX = 0

            for i in listListr1:
                if i:
                    if counterY < groesse - 1:
                        listListr2[1] = listListr1[counterY + 1]
                        zwischenwertLst.append((float(i[groesse - 1]) / (listListr1[groesse - 1])[groesse - 1] * -1))
                        for n in listListr1[counterY]:
                            listListr2[counterY].append((listListr2[counterY + 1])[counterX] * zwischenwertLst[-1] + n)
                            counterX += 1
                            if counterX == groesse * 2:
                                counterX = 0
                        counterY += 1

            counterY = 0

            for i in listListr2:
                if i:
                    zwischenwertLst.append(1 / i[counterY])
                    for n in i:
                        if n != 0:
                            listListr3[counterY].append(n * zwischenwertLst[-1])
                        else:
                            listListr3[counterY].append(0)
                    counterY += 1

            print("")
            print("Fertige Inverse:")
            counterY = 0

            for i in listListSch:
                i.clear()

            for i in listListr3:
                if i:
                    for n in i:
                        listListSch[counterY].append(str(Fraction(n).limit_denominator()))
                    counterY += 1

            for i in listListSch:
                if i:
                    print(str(i[groesse:]).replace("'", ""))

            sleep(2)
            print()
            if input("Noch eine Inverse? ") in ja:
                counter = 5 + groesse * 2
                while counter > 0:
                    print(lnUp, end=lnClear)
                    counter -= 1
                setup = True
                matrixGroesse = True
                rechnung = False
                counter = 1
            else:
                rechnung = False
                main = False

        except ZeroDivisionError:
            print()
            print("Diese Matrix hat leider keine Inverse")
            print()
            if input("Möchten Sie wissen warum dies so ist? ") in ja:

                # Ersteller der Matrix der Determinanten-Rechnung
                counterY = 0
                for i in origListList:
                    if i:
                        listListr1[counterY] = origListList[counterY][0:groesse]
                        counterY += 1

                # Determinanten-Werte Sortierer
                counterY = 0
                counter = 1
                tick = 0
                for i in listListr1:
                    if i:
                        for n in i:
                            determWerte[counterY].append(n)
                            if tick == groesse - 1:
                                counterY = counter
                                tick = 0
                            elif counterY == groesse - 1:
                                counterY = 0
                                tick += 1
                            else:
                                counterY += 1
                                tick += 1
                        counter += 1

                # Determinanten-Rechnung String Builder
                counterX = 0
                counterY = 0
                for i in determWerte:
                    if i:
                        for n in i:
                            if counterX == 0 and counterY == 0:
                                determRech = str("(" + ("(" + str(n) + ")" if "-" in str(n) else str(n)))
                                counterX += 1
                            elif counterX == 0:
                                determRech += str(" - (" + ("(" + str(n) + ")" if "-" in str(n) else str(n)))
                                counterX += 1
                            else:
                                determRech += str(" * " + ("(" + str(n) + ")" if "-" in str(n) else str(n)))
                                counterX += 1
                                if counterX == groesse:
                                    determRech += ")"
                                    counterX = 0
                        counterY += 1

                # Determinanten Mal Rechner
                counterX = -1
                counterY = 0
                for i in determWerte:
                    if i:
                        for n in i:
                            if counterX == -1:
                                listListr2[counterY] = determWerte[counterY]
                                counterX += 1
                            else:
                                listListr2[counterY][0] = n * listListr2[counterY][counterX]
                                counterX += 1
                            if counterX == groesse - 1:
                                counterX = -1
                        counterY += 1

                # Determinanten Minus Rechner
                for i in listListr2:
                    if i:
                        determWert = i[0] - determWert

                # Fertigstellung des Strings der Determinanten-Rechnung
                determRech += str(f" = {determWert}")

                counter = 3
                while counter > 0:
                    print(lnUp, end=lnClear)
                    counter -= 1

                # Ausgabe der Determinanten Rechnung
                print(determRech)
                print()
                print(f"Die Determinanten-Rechnung ergibt {determWert}")
                print()

                # Abfrage, ob noch eine Inverse berechnet werden soll
                sleep(2)
                if input("Noch eine Inverse? ") in ja:
                    setup = True
                    matrixGroesse = True
                    rechnung = False
                else:
                    main = False
                    rechnung = False

            else:
                # Abfrage, ob noch eine Inverse berechnet werden soll
                print()
                if input("Noch eine Inverse? ") in ja:
                    setup = True
                    matrixGroesse = True
                    rechnung = False
                else:
                    main = False
                    rechnung = False
