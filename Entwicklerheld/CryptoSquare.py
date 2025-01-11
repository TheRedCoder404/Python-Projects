from math import sqrt

string = "If man was meant to stay on the ground, god would have given us roots."

def CryptoSquareEncrypter(message: str):
    plain = message.replace(".", "").replace(",", "").replace(" ", "").replace("-", "").replace("@", "").replace("%", "").replace("!", "").lower()

    columns = sqrt(len(plain)) if sqrt(len(plain)) % 1 == 0 else int(sqrt(len(plain))) + 1
    rows = int(sqrt(len(plain)))

    rowList = []
    row = ""

    for n, i in enumerate(plain, 1):
        if n % columns == 0:
            row += i
            rowList.append(row)
            row = ""
        elif n == len(plain):
            row += i
            row = row.ljust(rows)
            rowList.append(row)
            row = ""
        else:
            if n <= len(plain):
                row += i
            else:
                row += " "
    
    encodedMessage = ""
    x = 0
    y = 0
    for n in range(1, int(columns ** 2) + 1):
        try:
            encodedMessage += rowList[x][y] if rowList[x][y] != " " else ""
        except IndexError:
            if n != int(columns ** 2): encodedMessage += " "
            if y == rows - 1 and n != int(columns ** 2):
                encodedMessage += " "
        if x == columns - 1:
            x = 0
            y += 1 if y < rows else 0
            if n != int(columns ** 2) and encodedMessage[-1] != " ": encodedMessage += " "
        else:
            x += 1
    
    if encodedMessage[-2:-1] == "  ":
        encodedMessage = encodedMessage[:-1]

    return encodedMessage


def CryptoSquareDecrypter(message):
    pass


print(CryptoSquareEncrypter(string))
