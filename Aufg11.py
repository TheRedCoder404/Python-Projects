zeichk1 = input("Erste Zeichenkette eingen: ")
zeichk2 = input("Zweite Zeichenkette eingen: ")

res = []

for n in zeichk1:
    if n in zeichk2 and not (n in res):
        res.append(n)

res.sort()
print(res)
