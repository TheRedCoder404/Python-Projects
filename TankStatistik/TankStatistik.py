from time import sleep
import json
import os
os.system("")

lnUp = '\033[1A'
lnClear = '\x1b[2K'
datum = ""
liter = ""

nextId = 0
zeilen = 0
count = 0
hochst = 0

ja = ["Ja", "ja", "j"]
cleared = []

tankStops = {"cleared": cleared}

datumAbfr = True
literAbfr = True

while True:
    while zeilen > 0:
        print(lnUp, end=lnClear)
        zeilen -= 1

    eingabe = input("Was wollen Sie Tun? ")
    print()
    zeilen += 2

    if eingabe == "list":
        try:
            while zeilen > 0:
                print(lnUp, end=lnClear)
                zeilen -= 1

            hochst = 0
            count = 1
            for i in tankStops:
                if not i == "cleared":
                    if int(i) > int(hochst):
                        hochst = int(i)

            while not int(count) > int(hochst):
                if str(count) in cleared:
                    count += 1
                else:
                    print(str(tankStops[int(count)]).replace("{", "").replace("}", "").replace("'", ""))
                    zeilen += 1
                    count += 1
            print()
            print("Zum zurück kommen Enter drücken...")
            input()

            zeilen += 4
        except KeyError:
            print("Bitte erst die Statistik befüllen")
            zeilen += 1
            sleep(4)

    elif eingabe == "add":
        datumAbfr = True
        while datumAbfr:
            while zeilen > 0:
                print(lnUp, end=lnClear)
                zeilen -= 1

            eingabe = input("An welchem Datum haben Sie denn getankt? ")
            print()
            zeilen += 2
            if input(f"Ist dieses Datum ({eingabe}) richtig? ") in ja:
                datum = eingabe
                print()
                zeilen += 2
                datumAbfr = False

        literAbfr = True
        while literAbfr:
            while zeilen > 0:
                print(lnUp, end=lnClear)
                zeilen -= 1

            eingabe = input("Wie viele Liter haben Sie getankt? ")
            print()
            zeilen += 2
            if input(f"Ist diese Liter Zahl ({eingabe} L) richtig? ") in ja:
                liter = eingabe
                print()
                zeilen += 2
                literAbfr = False

        if cleared:
            nextId = cleared[0]
            cleared.remove(nextId)
        else:
            nextId = len(tankStops)

        tankStops[nextId] = {"Id": str(nextId), "Datum": datum, "Liter": liter}

    elif eingabe == "save":
        while zeilen > 0:
            print(lnUp, end=lnClear)
            zeilen -= 1

        save = open("save.json", "w")
        saveDict = json.dumps(tankStops)
        save.write(saveDict)
        save.close()

    elif eingabe == "load":
        while zeilen > 0:
            print(lnUp, end=lnClear)
            zeilen -= 1

        save = open("save.json", "r")
        saveDict = save.read()
        tankStops = json.loads(saveDict)
        nextId = len(tankStops)
        cleared = tankStops["cleared"]
        save.close()

    elif "clear" in eingabe:
        while zeilen > 0:
            print(lnUp, end=lnClear)
            zeilen -= 1

        try:
            if "*" in eingabe:
                tankStops.clear()
            else:
                eingabeSplit = eingabe.split()
                if eingabeSplit[1].isnumeric():
                    tankStops.pop(str(eingabeSplit[1]))
                    cleared.append(eingabeSplit[1])
                    tankStops["cleared"] = cleared
        except IndexError:
            print("Ungültiger Index")
            sleep(2)

    elif eingabe == "delete":
        while zeilen > 0:
            print(lnUp, end=lnClear)
            zeilen -= 1

        if os.path.exists("save.json"):
            os.remove("save.json")
        else:
            print("Es gibt keine Save Datei")

