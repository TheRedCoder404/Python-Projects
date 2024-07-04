import os
import json

if os.path.isfile("ReadmePrinter/names.txt"):
    open("ReadmePrinter/names.txt", "w").close()

dont = ["__pycache__", ".gitignore", ".git", "README.md"]

description = json.load(open("ReadmePrinter/descriptions.json"))

path = input()
txtfile = open("ReadmePrinter/names.txt", "a")

numbers = 1
for n in os.listdir(path):  # ich benutze hier kein enummerate, weil es sonst zahlen überspringt
    if not n in dont:
        if numbers == 1:
            txtfile.write("<details open>")
        else:
            txtfile.write("\n\n\n<details>")
        txtfile.write(f"\n  <summary>{numbers}. {n}</summary>")
        if n in description:
            txtfile.write(f"\n\n  {description[n]}\n")
        txtfile.write("\n</details>")
        numbers += 1

txtfile.close()
