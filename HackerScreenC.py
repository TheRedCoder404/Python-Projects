from time import sleep
from random import randrange
import os
os.system("")

colors = {
    "0": "\033[0;31m",
    "1": "\033[0;32m",
    "2": "\033[0;34m",
    "3": "\033[0;35m",
    "5": "\033[1;30m"
}
lns = int(input())
while True:
    row = "\n"

    for i in range(lns):
        row += colors[str(randrange(0, (len(colors) - 1)))]

        number = hex(randrange(10, 255)).replace("0x", "").upper()
        while len(number) < 2:
            number = hex(randrange(10, 255)).replace("0x", "").upper()

        if row:
            row += f" {number}"
        else:
            row += f"{number}"

    print(row)
    sleep(0.1)
