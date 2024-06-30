anzKistKl = int(input("Anzahl kleiner Kisten eingeben: "))
anzKistGr = int(input("Anzahl großer Kisten eingeben: "))
hoehe = int(input("Höhe des gewünschten Stapels eingeben: "))

gewiKistKl = 1
gewiKistGr = 5

if (anzKistKl * gewiKistKl) + (anzKistGr * gewiKistGr) == hoehe:
    print(f"Ja, ein Stapel der Höhe {hoehe} kann aus {anzKistGr} großen und {anzKistKl} kleinen Kiste(n) gebaut werden")
else:
    print(f"Nein, ein Stapel der Höhe {hoehe} kann nicht aus {anzKistGr} großen und {anzKistKl} kleinen Kiste(n) gebaut werden")
