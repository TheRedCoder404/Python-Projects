import time

print("Guten Morgen!")
time.sleep(3)

wiederh = True

while wiederh:

    Vorname = input("Wie lautet der Vorname der Person?: ")
    Nachname = input("Wie lautet der Nachname von " + Vorname + "?: ")
    Alter = input("Wie alt ist " + Vorname + "?: ")

    alter = int(Alter)

    if alter >= 18:
        print(Vorname + " " + Nachname + " ist Volljährig")
    else:
        print(Vorname + " " + Nachname + " ist nicht Volljährig")

    time.sleep(5)
    bestaetigt = input("Wollen Sie noch eine Person Nachfragen? (ja/nein)  ")

    if bestaetigt == "ja":
        print("Ok, dann zum Nächsten!")
        time.sleep(3)
    else:
        wiederh = False
