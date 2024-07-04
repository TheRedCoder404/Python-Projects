main = True
ja = ["Ja", "ja", "j"]

while main:
    x = int(input("Bitte die F Zahl angeben: "))
    a = x
    b = True
    y = 0
    z = 1

    if x == 0:
        print("F 0 = 0")
    elif x == 1:
        print("F 1 = 1")
    else:
        while x > 1:
            if b:
                y = y + z
                x -= 1
                b = False
            else:
                z = y + z
                x -= 1
                b = True
        print("F" + str(a) + " = ", str(z) if b else str(y))
    print("")

    if input("Noch eine Zahl?: ") in ja:
        print("")
    else:
        main = False
