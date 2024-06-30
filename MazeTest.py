from random import random
import keyboard
import os
os.system("")

mazeMap = []
path = []
pathSplitList = []
playerPos = []
ja = ["Ja", "ja", "j"]

pathGen = True
main = True
playing = False

wall = "#"
player = "+"
finish = " "

lnUp = '\033[1A'
lnClear = '\x1b[2K'

while main:

    size = int(input("Wie groß soll das Labyrinth sein? "))
    xLoc = int(size / 2) if size % 2 == 0 else int((size / 2) + 1)
    yLoc = int(size / 2) if size % 2 == 0 else int((size / 2) + 1)
    playerPos.append(xLoc)
    playerPos.append(yLoc)
    posX = 0
    posY = 0

    tick = size
    while tick > 0:
        mazeMap.append([])
        tick -= 1

    while pathGen:
        direction = random()
        if direction < 0.25:
            if f"{str(yLoc)} / {str(yLoc - 1)}" not in path:
                if xLoc == 2:
                    xLoc -= 1
                    path.append(f"{str(yLoc)} / {str(xLoc)}")
                    finish = f"{str(yLoc)} / {str(xLoc)}"
                    pathGen = False
                else:
                    xLoc -= 1
                    path.append(f"{str(yLoc)} / {str(xLoc)}")
            else:
                pass
        elif direction < 0.5:
            if f"{str(yLoc + 1)} / {str(xLoc)}" not in path:
                if yLoc == size - 1:
                    yLoc += 1
                    path.append(f"{str(yLoc)} / {str(xLoc)}")
                    finish = f"{str(yLoc)} / {str(xLoc)}"
                    pathGen = False
                else:
                    yLoc += 1
                    path.append(f"{str(yLoc)} / {str(xLoc)}")
            else:
                pass
        elif direction < 0.75:
            if f"{str(yLoc)} / {str(xLoc + 1)}" not in path:
                if xLoc == size - 1:
                    xLoc += 1
                    path.append(f"{str(yLoc)} / {str(xLoc)}")
                    finish = f"{str(yLoc)} / {str(xLoc)}"
                    pathGen = False
                else:
                    xLoc += 1
                    path.append(f"{str(yLoc)} / {str(xLoc)}")
            else:
                pass
        else:
            if f"{str(yLoc - 1)} / {str(xLoc)}" not in path:
                if yLoc == 2:
                    yLoc -= 1
                    path.append(f"{str(yLoc)} / {str(xLoc)}")
                    finish = f"{str(yLoc)} / {str(xLoc)}"
                    pathGen = False
                else:
                    yLoc -= 1
                    path.append(f"{str(yLoc)} / {str(xLoc)}")
            else:
                pass

    tick = 0
    for i in path:
        pathSplit = path[tick].split()
        pathSplitList.append(pathSplit)
        tick += 1
    pathSplitList.sort()

    posX = 0
    posY = 0
    try:
        for ind in mazeMap:
            tick = size
            while tick > 0:
                for i in range(len(pathSplitList)):
                    if str(posY + 1) == pathSplitList[i][0]:
                        if pathSplitList[i][2] == str(posX + 1):
                            mazeMap[posY].append(" ")
                            break
                else:
                    if posY == 0 or posY == size - 1 or posX == 0 or posX == size - 1:
                        mazeMap[posY].append(wall)
                    else:
                        if random() < 0.5:
                            mazeMap[posY].append(wall)
                        else:
                            mazeMap[posY].append(" ")
                posX += 1
                tick -= 1
            posY += 1
            posX = 0
    except IndexError:
        pass

    mazeMap[start - 1][start - 1] = "+"

    for i in mazeMap:
        print(str(i).replace("[", "").replace("]", "").replace(",", "").replace("'", ""))

    playing = True
    while playing:
        try:
            if keyboard.is_pressed("nach-oben"):
                if not keyboard.is_pressed("nach-oben"):
                    if mazeMap[playerPos[0] + 1][playerPos[1]] == " ":
                        mazeMap[int(playerPos[0] + 1)][int(playerPos[1]) - 1] = "+"
                        mazeMap[int(playerPos[0])][int(playerPos[1]) - 1] = " "
                        playerPos = [int(playerPos[0] + 1), int(playerPos[1])]
                        tick = size

                        while tick > 0:
                            print(lnUp, end=lnClear)
                            tick -= 1
                        for i in mazeMap:
                            print(str(i).replace("[", "").replace("]", "").replace(",", "").replace("'", ""))
        except:
            pass

    print()
    if input("Noch ein Labyrinth? ") in ja:
        mazeMap.clear()
        path.clear()
        pathSplitList.clear()
        pathGen = True
    else:
        pathGen = False
        main = False
