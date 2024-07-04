hexZ = input("Bitte eine Hexa-Dezimal Zahl eingeben: ")
dezZ = 0
counter = int(len(hexZ) - 1)

hexaDict = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}

for i in hexZ:
    if i in hexaDict:
        dezZ += hexaDict[i] * (16 ** counter)
    else:
        dezZ += int(i) * (16 ** counter)
    counter -= 1

print(dezZ)
