while True:
    zeichKette = input("Bitte eine Zeichenkette eingeben: ")

    anfStrich = False
    endStrich = False

    counter = 0
    ausgKette = []
    worter = zeichKette.split(" ")

    for wort in worter:
        if "_" in wort:
            counter = 0
            anfStrich = False
            endStrich = False

            for buchst in wort:
                counter += 1
                if buchst == "_" and counter == 1:
                    wort = wort.upper()
                    anfStrich = True
                elif buchst == "_" and counter == len(wort):
                    wort = wort.lower()
                    endStrich = True

            if (anfStrich != endStrich) or (anfStrich and endStrich):
                wort = wort.replace("_", "")

        ausgKette.append(wort)

    print(zeichKette, "wird zu", str(ausgKette).replace("[", "").replace("]", "").replace("'", "").replace(",", ""))
    print("")
