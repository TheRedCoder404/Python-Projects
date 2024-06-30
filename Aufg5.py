umsatz = int(input("Bitte geben Sie einen Umsatz ein: "))

if umsatz > 10000:
    print(f"Der eingegebene Umsatz von {umsatz} entspricht Kategorie A")
elif umsatz >= 1000:
    print(f"Der eingegebene Umsatz von {umsatz} entspricht Kategorie B")
else:
    print(f"Der eingegebene Umsatz von {umsatz} entspricht Kategorie C")
