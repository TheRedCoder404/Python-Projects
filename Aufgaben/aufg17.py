while True:
    erstZKette = input("Erste Zahl eingeben: ")
    zweiZKette = input("Zweite Zahl eingeben: ")
    
    pruefw = (len(erstZKette) - len(zweiZKette))
    
    if erstZKette[pruefw:] == zweiZKette:
        print("Die letzten Ziffern stimmen überein")
    else:
        print(f"Die letzten Ziffern stimmen nicht überein (hätte gestimmt, bei zweite Zahl {erstZKette[pruefw:]})")
