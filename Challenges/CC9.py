import os
from time import sleep
import nuetzliche_functions as nf
os.system("")

lnUp = '\033[1A'
lnClear = '\x1b[2K'

main = True

eingabe = 0


def clear(lines):
    for x in range(lines):
        print(lnUp, end=lnClear)


while main:
    try:
        eingabe: int = int(input("Bitte eine Zahl eingeben: "))

        auseinander = []
        sortiert = ""
        sortiertBw = ""

        for i in str(eingabe):
            auseinander.append(i)

        auseinander.sort()

        for i in auseinander:
            sortiert += i

        auseinander.sort(reverse=True)

        for i in auseinander:
            sortiertBw += i

        print(f"\nDas ergebnis ist: {int(sortiertBw) - int(sortiert)}")
        if input("\nSoll noch eine Zahl berechnet werden? ") in nf.ja():
            clear(5)
        else:
            main = False

    except ValueError:
        print("\nDies war keine Zahl sondern eine andere form der eingabe. Bitte eine Zahl im Dezimal format und ohne "
              "Komma eingeben.")
        sleep(3)
        input("\nBitte Enter zum Fortfahren drücken ...")
        clear(5)
