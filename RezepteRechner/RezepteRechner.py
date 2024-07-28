import json
import os
import sys
import ItemCreation
sys.path.append('../Git/nuetzliche_functions')
import nuetzliche_functions as nf
from time import sleep
os.system("")

clear = lambda: os.system('cls')

def printTitle() -> None:
    print("-------------------------------")
    print("------- Rezepte Rechner -------")
    print("-------------------------------")
    print("\n\nWas würden Sie gerne tun?")

def printAddItemMode() -> None:
    print("-------------------------------")
    print("------- Add Recipe Mode -------")
    print("-------------------------------")

def printListItems() -> None:
    print("-------------------------------")
    print("------ List Recipe Mode -------")
    print("-------------------------------")
    print("\n\nAlle Rezepte:\n")

def printHelp(inputlist: list) -> None:
    if len(inputlist) < 2:
        for i in options:
            print(f"{i:<10}: {options[i]["beschr"]}")
    else:
        print("Es gibt noch keine Parameter verarbeitung")

def save() -> None:
    saveList = []
    for i in items:
        diction: dict = i.item2dict
        saveList.append(diction)
    save = open("RezepteRechner/items.json", "w")
    saveJson = json.dumps(saveList)
    save.write(saveJson)
    save.close()

def load() -> None:
    if os.path.isfile("RezepteRechner/items.json"):
        global items
        save = open("RezepteRechner/items.json", "r")
        saveJson = save.read
        saveList = json.loads(saveJson)
        for i in saveList:
            newItem = ItemCreation.Item(diction=i)
            items.append(newItem)
        save.close

def lineClearer(lines: int) -> None:
    for i in range(lines):
        print(lnUp, end=lnClear)


options = {
    "addRecipe": {
        "beschr": "Fügt ein neues Rezept zum Rechner hinzu",
        "parameters": None
    },
    "editRecipe": {
        "beschr": "Erlaubt ein zuvor hinzugefütes Rezept zu verändern",
        "parameters": None
    },
    "listRecipes": {
        "beschr": "Listet alle bisher hinzugefügten Rezepte auf",
        "parameters": None
    },
    "help": {
        "beschr": "Gibt eine liste an allen Befehlen mit der jeweiligen beschreibung aus",
        "parmeters": None
    }
}

items = []

lnUp = '\033[1A'
lnClear = '\x1b[2K'

dist = 15

main = True
getOption = True

load()
printTitle()
while main:
    while getOption:
        option = input()
        option = option.split()
        if option[0] in options:
            getOption = False
            print()
        else:
            print("Dies ist leider keine Gültige Option. Für Hilfe mit oder eine liste von den Optionen, bitte \"help\" eingeben.")
            sleep(3)
            lineClearer(2)
    
    if option[0] == "help":
        printHelp(option)
        getOption = True
        option = ""

    elif option[0] == "addRecipe":
        addItemMode = True
        clear()
        printAddItemMode()
        while addItemMode:
            # Abfrage welche Items erzeugt werden
            item = input("\n\nWas soll erzeugt werden?: ")
            itemNameList = [item]

            if input("Wird bei diesem Rezept noch ein Item erzeugt?: ") in nf.ja():
                moreItems = True
                while moreItems:
                    item = input("Wie heißt dieses Item?: ")
                    itemNameList.append(item)
                    if input("Wird bei diesem Rezept noch ein Item erzeugt?: ") in nf.nein():
                        moreItems = False
            
            newItem = ItemCreation.Item(itemNameList)   # Angabe welche Items erzeugt werden
            outputDict = {}
            print()
            # Abfrage wie viele Items erzeugt werden
            for i in itemNameList:
                newItem.changeOutput({f"{i}": int(input(f"Wie viel von \"{i}\" wird erzeugt?: "))})

            # Abfrage welche Items benötigt werden
            item = input("\nWelches Item wird für diese Rezept benötigt?: ")
            itemNameList = [item]

            if input("Wird für dieses Rezept noch ein Item benötigt?: ") in nf.ja():
                moreItems = True
                while moreItems:
                    item = input("Wie heißt dieses Item?: ")
                    itemNameList.append(item)
                    if not input("Wird für dieses Rezept noch ein Item benötigt?: ") in nf.ja():
                        moreItems = False
            
            inputDict = {}
            print()
            # Abfrage wie viele Items gebraucht werden
            for i in itemNameList:
                newItem.changeInput({f"{i}": int(input(f"Wie viel von \"{i}\" wird benötigt?: "))})
            
            items.append(newItem)
            save()

            if not input("\n\nSoll noch ein Rezept hinzugefügt werden?: ") in nf.ja():
                clear()
                printTitle()
                addItemMode = False
            else:
                clear()
                printAddItemMode()
        getOption = True
        option = ""
    
    elif option[0] == "listRecipes":
        clear()
        printListItems()
        print(f"{"Erzeugt:":<25}{"Menge:":<9}{"Benötigt:"}")
        for i in items:
            inputItems = ""
            for x, inputs in enumerate(i.input):
                if x > 0:
                    inputItems += f", {inputs} ({i.input[inputs]})"
                else:
                    inputItems = f"{inputs} ({i.input[inputs]})"

            for y in i.name:
                print(f"{y:<25}{i.output[y]:<9}{inputItems}")
        
        input("\n\nBitte Enter Drücken...")
        clear()
        printTitle()
        getOption = True
        option = ""
            