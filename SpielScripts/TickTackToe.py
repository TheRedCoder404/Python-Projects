import time
import os
os.system("")

setup = True
main = True
player1 = True
player2 = False
p1Win = False
p2Win = False

lnUp = '\033[1A'
lnClear = '\x1b[2K'

player1name = ""
player2name = ""

tick = 0

spielF1 = [" ", " ", " "]
spielF2 = [" ", " ", " "]
spielF3 = [" ", " ", " "]
dict1 = {'winCon1': [1, 2, 3], 'winCon2': [4, 5, 6], 'winCon3': [7, 8, 9], 'winCon4': [1, 4, 7],
         'winCon5': [2, 5, 8], 'winCon6': [3, 6, 9], 'winCon7': [1, 5, 9], 'winCon8': [3, 5, 7]}
winList = ["winCon1", "winCon2", "winCon3", "winCon4", "winCon5", "winCon6", "winCon7", "winCon8"]
benutztp1 = []
benutztp2 = []
ja = ["Ja", "ja", "j"]

while main:
    while setup:
        player1 = True
        player2 = False
        p1Win = False
        p2Win = False

        player1name = input("Wie soll Spieler 1 heißen?: ")
        player2name = input("Wie soll Spieler 2 heißen?: ")

        tick = 0

        time.sleep(1)
        print(lnUp, end=lnClear)
        print(lnUp, end=lnClear)

        spielF1 = [" ", " ", " "]
        spielF2 = [" ", " ", " "]
        spielF3 = [" ", " ", " "]

        benutztp1 = []
        benutztp2 = []

        print(spielF1)
        print(spielF2)
        print(spielF3)

        setup = False

    while player1:
        print(player1name, ":")
        inZahl = int(input("Gib eine Zahl von 1 - 9 an. Oben links bis unten rechts: "))

        if not (inZahl in benutztp2 or inZahl in benutztp1):
            if inZahl <= 3:
                spielF1[inZahl - 1] = "x"
                benutztp1.append(inZahl)
            elif inZahl <= 6:
                spielF2[inZahl - 4] = "x"
                benutztp1.append(inZahl)
            else:
                spielF3[inZahl - 7] = "x"
                benutztp1.append(inZahl)

            tick += 6

            time.sleep(0.3)

            while tick > 0:
                print(lnUp, end=lnClear)
                tick -= 1

            print(spielF1)
            print(spielF2)
            print(spielF3)
            print()

            benutztp1.sort()

            for x in winList:
                winStor = dict1[x]
                if winStor[0] in benutztp1:
                    if winStor[1] in benutztp1 and winStor[2] in benutztp1:
                        print()
                        print("Herzlichen Glückwunsch " + player1name + ", du hast gewonnen!")
                        p1Win = True

                        if input("Wollt ihr noch eine Runde spielen?: (ja / nein) ") in ja:
                            while tick < 3:
                                print()
                                tick += 1
                            setup = True
                            player1 = False
                        else:
                            main = False
                            player1 = False

            if not p1Win:
                player2 = True
                player1 = False
        else:
            print()
            print("Schon belegt")
            print()
            tick += 5

    while player2:
        print(player2name, ":")
        inZahl = int(input("Gib eine Zahl von 1 - 9 an. Oben links bis unten rechts: "))

        if not (inZahl in benutztp2 or inZahl in benutztp1):
            if inZahl <= 3:
                spielF1[inZahl - 1] = "o"
                benutztp2.append(inZahl)
            elif inZahl <= 6:
                spielF2[inZahl - 4] = "o"
                benutztp2.append(inZahl)
            else:
                spielF3[inZahl - 7] = "o"
                benutztp2.append(inZahl)

            tick += 6

            time.sleep(0.3)

            while tick > 0:
                print(lnUp, end=lnClear)
                tick -= 1

            print(spielF1)
            print(spielF2)
            print(spielF3)
            print()

            benutztp2.sort()

            for x in winList:
                winStor = dict1[x]
                if winStor[0] in benutztp2:
                    if winStor[1] in benutztp2 and winStor[2] in benutztp2:
                        print()
                        print("Herzlichen Glückwunsch " + player2name + ", du hast gewonnen!")
                        p2Win = True

                        if input("Wollt ihr noch eine Runde spielen?: (ja / nein) ") in ja:
                            while tick < 3:
                                print()
                                tick += 1
                            setup = True
                            player2 = False
                        else:
                            main = False
                            player2 = False

            if not p2Win:
                player1 = True
                player2 = False
        else:
            print()
            print("Schon belegt")
            print()
            tick += 5
