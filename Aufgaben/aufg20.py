zeichk = input("Zeichenkette eingeben: ")

buchst = []

vokale = {
    "A": {
        "häufig": 0,
        "wahrsch": 0
    }, "E": {
        "häufig": 0,
        "wahrsch": 0
    }, "I": {
        "häufig": 0,
        "wahrsch": 0
    }, "O": {
        "häufig": 0,
        "wahrsch": 0
    }, "U": {
        "häufig": 0,
        "wahrsch": 0
    }
}

for i in zeichk:
    for x in i:
        buchst.append(x.upper())
        
for i in buchst:
    if i == "A":
        vokale["A"]["häufig"] += 1
    elif i == "E":
        vokale["E"]["häufig"] += 1
    elif i == "I":
        vokale["I"]["häufig"] += 1
    elif i == "O":
        vokale["O"]["häufig"] += 1
    elif i == "U":
        vokale["U"]["häufig"] += 1
        
for i in vokale:
    vokale[i]["wahrsch"] = round((vokale[i]["häufig"] / len(buchst) * 100), 2)
    print(f"{i} > {vokale[i]['häufig']}x ({vokale[i]['wahrsch']}%).")
    