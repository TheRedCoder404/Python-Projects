while True:
    zahl = int(input("Zahl eingeben: "))

    nebenW = 0
    zwischenList = []
    zwischenList2 = []

    for n in str(zahl):
        x = int(n) ** len(str(zahl))
        nebenW += x
        zwischenList.append(f"{n}^{len(str(zahl))}")
        zwischenList2.append(x)

    if nebenW == zahl:
        print(f"Ja, {zahl} ist eine narzistische Zahl")
        print(f"    ({zahl} = {zwischenList} = {zwischenList2})".replace(",", " +").replace("[", "")
              .replace("]", "").replace("'", ""))
    else:
        print(f"Die Zahl {zahl} ist keine narzistische Zahl")
    print()

