from random import randrange
from time import sleep
from os import system
system("")

setup = True
main = True
abfrage = False
printTipp = False

lnUp = '\033[1A'
lnClear = '\x1b[2K'

zahl = 0
tick = 0
tick2 = 0
counter = 0
versuch = 1
geschZahl = 0

ja = ["Ja", "ja", "j"]
tippList = []
geschaetzte = []

tipps = {"durchZehn": "Die Zahl ist durch Zehn teilbar",
         "nDurchZehn": "Die Zahl ist nicht durch Zehn Teilbar",
         "durchFünf": "Die Zahl ist durch Fünf Teilbar",
         "nDurchFünf": "Die Zahl ist nicht durch Fünf Teilbar",
         "durchZwei": "Die Zahl ist durch Zwei Teilbar",
         "nDurchZwei": "Die Zahl ist nicht durch Zwei Teilbar",
         "anfNummer": "",
         "midNummer": "Die Zahl hat eine Null in der Mitte",
         "endNummer": "",
         "hatLänge": "",
         "einZeichen": "Die Zahl ist ein Zeichen lang",
         "nichtGesucht": ""}

# print des Start-Screens
print("Zahlen Raten!!!")
print()
print("Rate eine Zahl zwischen 0 und 100!")
print()


while main:
    while setup:
        tick = 0
        tick2 = 0
        counter = 0
        versuch = 1

        geschaetzte = []
        tippList = ["hatLänge"]

        # Random Zahl Generator
        zahl = int(randrange(0, 100))
        print()

        tipps["hatLänge"] = f"Die Zahl ist {len(str(zahl))} Zeichen lang"

        # Test der Tipps
        if zahl % 10 == 0:
            tippList.append("durchZehn")
        else:
            tippList.append("nDurchZehn")

        if zahl % 5 == 0:
            tippList.append("durchFünf")
        else:
            tippList.append("nDurchFünf")

        if zahl % 2 == 0:
            tippList.append("durchZwei")
        else:
            tippList.append("nDurchZwei")

        if len(str(zahl)) > 1:
            tippList.append("anfNummer")
            tipps["anfNummer"] = f"Die Zahl fängt mit {str(zahl)[0]} an"
            tippList.append("endNummer")
            tipps["endNummer"] = f"Die Zahl endet mit {str(zahl)[-1]}"
        else:
            tippList.append("einZeichen")

        if len(str(zahl)) > 2:
            tippList.append("midNummer")

        abfrage = True
        setup = False

    while abfrage:
        try:
            schaetzung = int(input("Bitte eine Zahl eingeben: "))

            # Abfrage, ob die Schätzung richtig ist
            print()
            if schaetzung == zahl:
                print(f"Richtig!! Du hast die Zahl {zahl} in "
                      f"{"einem Versuch" if versuch == 1 else f"{versuch} Versuchen"} richtig erraten!")
                sleep(3)

                # Abfrage, ob noch eine Zahl geraten werden soll
                print()
                if input("Möchtest du noch eine Zahl raten? ") in ja:
                    tick = tick2 + 6
                    while tick > 0:
                        print(lnUp, end=lnClear)
                        tick -= 1

                    setup = True
                    abfrage = False
                else:
                    main = False
                    abfrage = False
            else:
                print(f"Die Zahl {schaetzung} ist leider nicht die gesuchte Zahl.")
                versuch += 1
                geschaetzte.append(schaetzung)
                sleep(3)

                tick += 3
                while tick > 0:
                    print(lnUp, end=lnClear)
                    tick -= 1

                # Tipp Ausgabe
                if tippList:
                    printTipp = True
                    while printTipp:
                        try:
                            tipp = tippList[int(randrange(len(tippList) - 1))]
                            if tipp == "anfNummer" and versuch < 10:
                                counter += 1
                                if counter > 3:
                                    printTipp = False
                            elif tipp == "endNummer" and versuch < 15:
                                counter += 1
                                if counter > 3:
                                    printTipp = False
                            elif tipp == "nichtGesucht" and versuch > 4:
                                if geschaetzte:
                                    geschZahl = str(geschaetzte[randrange(0, len(geschaetzte))])
                                    geschZahl = int(geschZahl[randrange(0, len(geschZahl))])

                                    if geschZahl in zahl:
                                        if versuch > 14:
                                            print(f"Die Zahl {geschZahl} ist in der gesuchten Zahl")
                                            print()
                                            tick2 += 2
                                            printTipp = False
                                        else:
                                            pass
                                    else:
                                        print(f"Die Zahl {geschZahl} ist nicht in der gesuchten Zahl")
                                        print()
                                        tick2 += 2
                                        printTipp = False
                            else:
                                print(tipps[tipp])
                                print()
                                tick2 += 2
                                tippList.remove(tipp)
                                printTipp = False
                        except IndexError:
                            pass

        except ValueError:
            # Ausgabe bei ungültiger Eingabe
            print()
            print("Diese Eingabe war ungültig. Bitte eine Zahl zwischen 0 und 100 eingeben.")
            sleep(3)

            tick += 3
            while tick > 0:
                print(lnUp, end=lnClear)
                tick -= 1
