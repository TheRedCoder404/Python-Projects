from time import sleep
from random import randrange

while True:
    row = "\n"
    for i in range(16):
        number = hex(randrange(10, 255)).replace("0x", "").upper()
        while len(number) < 2:
            number = hex(randrange(10, 255)).replace("0x", "").upper()

        if row:
            row += f" {number}"
        else:
            row += f"{number}"

    print(row)
    sleep(0.1)
