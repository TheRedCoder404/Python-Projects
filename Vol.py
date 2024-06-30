from time import sleep
import math
main = True

while main:
    groessen = input("Bitte die Größen eingeben (b x h cm): ")

    if groessen in ["stop", "exit"]:
        main = False
        break
    else:
        try:
            bxhList = groessen.split()
            count = 0
            x = 0
            chVal = 1
            b = float(bxhList[0])
            h = float(bxhList[2])

            p = ((2 * ((b * -2) + (h * -2))) / 12)
            q = ((b * h) / 12)
            x1 = (-p / 2) + math.sqrt(((p / 2) ** 2) - q)
            x2 = (-p / 2) - math.sqrt(((p / 2) ** 2) - q)

            if x1 * 2 < b or x1 < h:
                x = x2
            else:
                x = x1

            vol = ((b - (2 * x)) * (h - (2 * x)) * x)

            innerSrfc = (b - (2 * x)) * (h - (2 * x))
            outerSrfc = (4 * (x * x)) + (((b - (2 * x)) * x) * 2) + (((h - (2 * x)) * x) * 2)
            flaeche = b * h
            print(f"\nDer Rand muss eine Dicke von {x} cm haben")
            print(f"Der Behälter wird ein Volumen von {vol} cm³ haben")
            print(f"Die Grundfläche nimmt eine Fläche von {innerSrfc} cm² ein")
            print(f"Der Rand nimmt eine Fläche von {outerSrfc} cm² ein")
            print(f"Der Flächeninhalt des Blattes beträgt {flaeche} cm²")
            sleep(3)
            print("\n")

        except ValueError:
            print("Dies war eine Ungültige Eingabe")
            sleep(3)
            print("\n")
