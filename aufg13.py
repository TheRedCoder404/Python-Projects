dualZ = input("Geben Sie bitte eine Dualzahl an: ")
counter = len(dualZ) - 1
dezZ = 0

for i in dualZ:
    dezZ += int(i) * (2 ** counter)
    counter -= 1

print(dezZ)
