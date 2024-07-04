from time import sleep
import nuetzliche_functions as nf
import os

os.system("")

morseCode = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..",
             "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-",
             "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--",
             "z": "--..", "ä": ".-.-", "ö": "---.", "ü": "..--", "ß": "...--..", "0": "-----", "1": ".----",
             "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..",
             "9": "----.", ".": ".-.-.-", ",": "--..--", ":": "---...", ";": "-.-.-.", "?": "..--..", "!": "-.-.--",
             "-": "-....-", "_": "..--.-", "(": "-.--.", ")": "-.--.-", "'": ".----.", "=": "-...-", "+": ".-.-.",
             "/": "-..-.", "@": ".--.-.", "\"": ".-..-.", "space": ""}

main = True

while main:
    space = True
    modus = input("Wollen Sie von Normal zu Morse Code übersetzen (1) oder von Morse zu Normal (2)? ")
    if modus == "1":
        while space:
            spaceArt = input("\nWelche art der Space Methode wollen Sie benutzen: 1( ), 2(_), 3(/) ")
            if spaceArt == "1":
                morseCode["space"] = " "
                space = False
            elif spaceArt == "2":
                morseCode["space"] = "_"
                space = False
            elif spaceArt == "3":
                morseCode["space"] = "/"
                space = False
            else:
                print("\nDies war eine ungültige Eingabe. Gültige Eingaben sind: 1, 2 oder 3")

        eingabe = input("\nBitte den zu übersetzenden Text eingeben: ")
        wordList = eingabe.split()
        ausgabe = ""

        for i in wordList:
            if ausgabe:
                ausgabe += f" {morseCode["space"]}"
            for n in i:
                ausgabe += f" {morseCode[n.lower()]}" if ausgabe else morseCode[n.lower()]

        print(f"\n{ausgabe}")
        sleep(3)
        if input("\nBrauchen Sie noch eine übersetzung? ") in nf.ja():
            nf.clear(7)
        else:
            main = False

    elif modus == "2":
        while space:
            spaceArt = input("\nWelche art der Space Methode wird hier verwendet?: 1( ), 2(_), 3(/) ")
            if spaceArt == "1":
                morseCode["space"] = " "
                space = False
            elif spaceArt == "2":
                morseCode["space"] = "_"
                space = False
            elif spaceArt == "3":
                morseCode["space"] = "/"
                space = False
            else:
                print("\nDies war eine ungültige Eingabe. Gültige Eingaben sind: 1, 2 oder 3")

        eingabe = input("\nBitte den zu übersetzenden Morse Code eingeben: ")
        wordList = eingabe.split()
        ausgabe = ""

        if morseCode["space"] == " ":
            spacepos = []
            trippSpace = []

            for i, letter in enumerate(eingabe):
                if letter == " ":
                    spacepos.append(i)
                    if i - 1 in spacepos and i - 2 in spacepos:
                        trippSpace.append(int(((i - (len(trippSpace) + 2)) / 2) + ((i - (len(trippSpace) + 2)) % 2)))
        else:
            for i in wordList:
                if i == morseCode["space"]:
                    ausgabe += " "
                else:
                    ausgabe += list(morseCode.keys())[list(morseCode.values()).index(i)]

        print(f"\n{ausgabe}")
        sleep(3)
        if input("\nBrauchen Sie noch eine übersetzung? ") in nf.ja():
            nf.clear(7)
        else:
            main = False
    else:
        print("\nDies war leider keine gültige eingabe. Gültige eingaben sind: 1, für Normal zu Morse und 2, für Morse "
              "zu Normal")
        sleep(3)
        input("\nBitte Enter zum fortfahren drücken ...")
        nf.clear(5)
