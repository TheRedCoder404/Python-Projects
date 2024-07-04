while True:
    zahl = int(input("Bitte Zahl eingeben: "))

    teilbar = True

    teiler = 2
    geteilt = 0
    nebenW = 0

    ganzTeiler = []
    printList = []

    while teilbar:
        geteilt = zahl / teiler
        if geteilt == int(geteilt):
            ganzTeiler.append(int(geteilt))
        if geteilt < 1:
            teilbar = False
        else:
            teiler += 1

    ganzTeiler.sort()

    for i in ganzTeiler:
        nebenW += i

    if zahl == nebenW:
        print(f"Die echten Teiler der Zahl {zahl} sind {ganzTeiler[0:-1]} und {ganzTeiler[-1]}, die Summe ergibt "
              f"wieder "f"{zahl}".replace("[", "").replace("]", ""))
    else:
        print(f"Die Zahl {zahl} ist keine perfekte Zahl.")
    print("")
