import time

# Deklaration der variablen & co.
wiederh = True
roundOne = True
password = "Pfannkuchen"
tick = 0

nameList = []
namePos = 0
ageList = []

# Begrüßung nach öffnung und kleiner delay
print("Guten Morgen!")
time.sleep(3)

PassAbfrage = input("Wie lautet das Passwort?: ")  # Passwort abfrage

while wiederh:  # Anfang des Loops

    tick = 0  # tick-Zähler zurücksetzen

    if PassAbfrage == password:  # Test, ob das Passwort richtig eingegeben wurde
        if roundOne:  # Test, ob es der erste durchgang ist
            print("Ja richtig! Das ist das Passwort! ")
            roundOne = False  # Deklarierung, dass die erste Runde passiert wurde
            time.sleep(2)
        Vorname = input("Wie lautet der Vorname des Pfannkuchens?: ")
    else:
        if roundOne:  # Test, ob es der erste durchgang ist
            print("Ne, das ist das Passwort leider nicht. Aber ich lasse dich doch noch auf Volljährigkeit Prüfen.")
            roundOne = False  # Deklarierung, dass die erste Runde passiert wurde
            time.sleep(2)
        Vorname = input("Wie heißt denn die Person mit Vornamen? ")

    Nachname = input("Wie lautet der Nachname von " + Vorname + "?: ")

    if Vorname + " " + Nachname in nameList:
        namePos = nameList.index(Vorname + " " + Nachname)
        Alter = ageList[namePos]
    else:
        Alter = input("Wie alt ist " + Vorname + "?: ")
        nameList.append(Vorname + " " + Nachname)
        ageList.append(Alter)
        print(nameList)
        print(namePos)
        print(ageList)

    alter = int(Alter)  # Konvertierung zum int, weil die alters abfrage sonst meckert >:|

    if PassAbfrage == password:  # Test, ob das Passwort richtig eingegeben wurde
        if alter >= 18:  # Test, ob das nötige alter erreicht wurde
            print(Vorname + " " + Nachname + " ist ein Volljähriger Pfannkuchen")
        else:
            print(Vorname + " " + Nachname + " ist kein Volljähriger Pfannkuchen")
    else:
        if alter >= 18:
            print(Vorname + " " + Nachname + " ist Volljährig")
        else:
            print(Vorname + " " + Nachname + " ist nicht Volljährig")

    time.sleep(5)
    if PassAbfrage == password:  # Test, ob das Passwort richtig eingegeben wurde
        bestaetigt = input("Wollen Sie noch einen Pfannkuchen Nachfragen? (ja/nein)  ")
    else:  # Abfrage, ob noch eine Person geprüft werden soll
        bestaetigt = input("Wollen Sie noch eine Person Nachfragen? (ja/nein)  ")

    if bestaetigt == "ja" or bestaetigt == "Ja":  # Test ob noch eine Person geprüft werden soll
        if PassAbfrage == password:  # Test, ob das Passwort richtig eingegeben wurde
            print("Ok, dann zum Nächsten Pfannkuchen!")
        else:
            print("Ok, dann zum Nächsten!")
        time.sleep(3)
        while tick < 2:  # Eine kleine Schleife, damit zwischen dem neuen und alten Test ein bisschen abstand ist
            print()
            tick += 1
    else:
        wiederh = False  # Beenden der while-Schleife
