anzahl = int(input("Bitte geben Sie die anzahl an Zeichenketten an: "))
worter = ""
passw = ""

counter = 1

while anzahl > 0:
    print()
    zeichenkette = input(f"Bitte Zeichenkette {counter} eingeben: ")
    worter = zeichenkette.split()
    
    for i in worter:
        passw += str(i[0])
    
    print()
    passw += str(len(worter))
    
    counter += 1
    anzahl -= 1

print(passw)
