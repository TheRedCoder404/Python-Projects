dezZ = int(input())

zahlen = ""
zwischenz = 0

while dezZ > 0:
    zahlen = str(dezZ % 2) + zahlen
    dezZ = int(dezZ / 2)

print(zahlen)
