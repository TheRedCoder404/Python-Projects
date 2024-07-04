import nuetzliche_functions as nf
import os
os.system("")


def matrixrow():
    raise NotImplemented("Matrix reihen erstellen")


def matrix():
    raise NotImplemented("Matrix erstellen")


def clear(lines):
    global line
    if lines == "all":
        lines = line
    for x in range(lines):
        print(lnUp, end=lnClear)
        line -= 1


commandEingabe = ""
kursiv = '\033[3m'
endForm = '\033[0m'
lnUp = '\033[1A'
lnClear = '\x1b[2K'

line = 0

main = True
setup = True

commands = {
   "inverse": {
    "bool": False,
    "beschr": "Ein Rechner um die Inverse einer quadratischen Matrix diverser größe zu errechnen"
}, "gauss": {
    "bool": None,
    "beschr": "Noch nicht implementiert"
}, "add": {
    "bool": None,
    "beschr": "Noch nicht implementiert"
}, "multi": {
    "bool": None,
    "beschr": "Noch nicht implementiert"
}, "divid": {
    "bool": None,
    "beschr": "Noch nicht implementiert"
}}

while main:
    while setup:
        commandEingabe = input("Was für eine art Rechnung soll vollzogen werden? ")
        line += 1
        if commandEingabe in commands:
            commands[commandEingabe] = True
            setup = False
        elif "help" in commandEingabe:
            if commandEingabe == "help":
                keys = ""
                for key in commands:
                    if key == list(commands.keys())[0]:
                        keys = key
                    elif key == list(commands.keys())[-1]:
                        keys = keys + " und " + key
                    else:
                        keys = keys + ", " + key
                print(f"Zur auswahl stehen {keys}. Für eine erklärung was die einzelnen Optionen machen bitte \"help "
                      + kursiv + f"option\" " + endForm + " eingeben")
                line += 1
            elif commandEingabe.split()[1] in commands:
                print(commands[commandEingabe.split()[1]]["beschr"])
                input(kursiv + "Enter zum fortfahren drücken..." + endForm)
                line += 2
                clear(all)

            else:
                print("Ungültige Eingabe. Für eine liste der zur verfügung stehenden Optionen bitte help eingeben.")
                line += 1
        else:
            print("Ungültige Eingabe. Für eine liste der zur verfügung stehenden Optionen bitte help eingeben.")
            line += 1

    while commands["inverse"]["bool"]:
        groesse = input("Wie groß ist die Matrix?")
        line += 1

        eingabe = input("Bitte die erste Reihe der Matrix eingeben: ")
        line += 1
