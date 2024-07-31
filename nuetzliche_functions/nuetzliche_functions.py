from datetime import datetime
global start


#  Eine funktion die einfach nur Hello World ausgibt :)
def hello_world():
    print("Hello World")


def ping_start():
    global start
    start = datetime.now()


def ping():
    print(datetime.now() - start)


#  Eine NAND funktion
def nand(condition1: bool, condition2: bool) -> bool:
    return not (condition1 and condition2)


#  Eine NOR funktion
def nor(condition1: bool, condition2: bool) -> bool:
    return not (condition1 or condition2)


#  Eine XOR funktion
def xor(condition1: bool, condition2: bool) -> bool:
    if condition1 == condition2:
        return False
    else:
        return True


#  Eine XNOR funktion
def xnor(condition1: bool, condition2: bool) -> bool:
    return not xor(condition1, condition2)


#  Eine kleine funktion die letzten bestimmten Zeilen zu löschen
def clear(lines: int):
    for x in range(lines):
        print('\033[1A', end='\x1b[2K')


#  Eine Liste aus variationen, wie man mit Ja antworten kann
def ja() -> list:
    return ["Ja", "ja", "j"]


#  Eine Liste aus variationen, wie man mit Nein antworten kann
def nein() -> list:
    return ["Nein", "nein", "n"]


#  Eine funktion um zu prüfen, ob sich eine eingegebene Zahl, um eine narzisstische Zahl handelt.
def is_narcissistic_number(number: int) -> bool:
    hold = [int(i) ** int(len(str(number))) for i in str(number)]
    return sum(hold) == number


#  Eine funktion um zu prüfen, ob sich eine eingegebene Zahl, um eine perfekte Zahl handelt.
def is_perfect_number(number: int) -> bool:
    hold = [(int(i) if number % int(i) == 0 else 0) for i in range(1, int(number))]
    return sum(hold) == number
