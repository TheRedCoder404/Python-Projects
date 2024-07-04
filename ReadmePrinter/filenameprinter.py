import os
import json

print(os.path.isfile("names.txt"))

path = input()
txtfile = open("names.txt", "a")

for i, n in enumerate(os.listdir(path), start=1):
    txtfile.write("\n\n\n<details>")
    txtfile.write(f"\n  <summary>{i}. {n}</summary>")
    txtfile.write("\n</details>")

txtfile.close()
