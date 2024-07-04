from time import sleep
import random
import keyboard
import os

os.system("")

mazeMap = []
path = []
playerPos = []
ja = ["Ja", "ja", "j"]

main = True
setup = True
pathGen = False
playing = False

wall = "#"
player = "+"
space = " "

lnUp = '\033[1A'
lnClear = '\x1b[2K'

line = 0
yLoc = 0
xLoc = 0


def clear(lines):
    global line
    for x in range(lines):
        print(lnUp, end=lnClear)
        line -= 1


def dispupdate():
    clear(line)
    for x in mazeMap:
        print(str(x).replace(",", "").replace("[", "|").replace("]", "|"))


def gedrueckt(event):
    if playing:
        if event.name == "nach-links":
            posaenderung(0, -1)
        elif event.name == "nach-oben":
            posaenderung(-1, 0)
        elif event.name == "nach-rechts":
            posaenderung(0, 1)
        elif event.name == "nach-unten":
            posaenderung(1, 0)


def posaenderung(y, x):
    global line
    global yLoc
    global xLoc
    mazeMap[yLoc][xLoc] = space

    yLoc += y
    xLoc += x
    mazeMap[yLoc][xLoc] = player
    line += size
    dispupdate()


keyboard.on_press(gedrueckt)

while main:

    start = 0
    size = 0

    while setup:
        size = int(input("Wie groß soll das Labyrinth sein? ")) + 2
        line += 1
        if size < 5:
            print("\nDie Mindestgröße beträgt 5.")
            line += 2
            sleep(3)
            clear(line)
        else:
            xLoc = int(size / 2)
            yLoc = int(size / 2)
            path.append(f"{yLoc} / {xLoc}")
            start = xLoc
            playerPos.append(xLoc)
            playerPos.append(yLoc)
            posX = 0
            posY = 0

            for i in range(size):
                mazeMap.append([])

            pathGen = True
            setup = False

    while pathGen:
        direction = random.randrange(1, 5)
        if direction == 1:
            if f"{yLoc} / {xLoc - 1}" not in path:
                xLoc -= 1
                path.append(f"{yLoc} / {xLoc}")
                if xLoc == 0:
                    pathGen = False
        elif direction == 2:
            if f"{yLoc + 1} / {xLoc}" not in path:
                yLoc += 1
                path.append(f"{yLoc} / {xLoc}")
                if yLoc == size - 1:
                    pathGen = False
        elif direction == 3:
            if f"{yLoc} / {xLoc + 1}" not in path:
                xLoc += 1
                path.append(f"{yLoc} / {xLoc}")
                if xLoc == size - 1:
                    pathGen = False
        elif direction == 4:
            if f"{yLoc - 1} / {xLoc}" not in path:
                yLoc -= 1
                path.append(f"{yLoc} / {xLoc}")
                if yLoc == 0:
                    pathGen = False

    for i in range(size):
        for n in range(size):
            if i == start and n == start:
                mazeMap[i].append(player)
            else:
                mazeMap[i].append(space)

    yLoc = start
    xLoc = start
    dispupdate()

    playing = True
    while playing:
        pass
