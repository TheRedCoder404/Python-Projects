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
    print("\n\n")

def printListItems() -> None:
    print("-------------------------------")
    print("------ List Recipe Mode -------")
    print("-------------------------------")
    print("\n\nAlle Rezepte:\n")

def printEditRecipe() -> None:
    print("-------------------------------")
    print("------ Edit Recipe Mode -------")
    print("-------------------------------")
    print("\n\n")

def printRechnerMode() -> None:
    print("-------------------------------")
    print("-------- Rechner Mode ---------")
    print("-------------------------------")
    print("\n\n")

def printDelRecipe() -> None:
    print(red)
    print("-------------------------------")
    print("------ Recipe Delete Mode -----")
    print("-------------------------------")
    print(normal + "\n\n")

def printHelp(inputlist: list) -> None:
    if len(inputlist) < 2:
        for i in options:
            print(f"{i:<10}: {options[i]["beschr"]}")
    else:
        print("Es gibt noch keine Parameter verarbeitung")

def save() -> None:
    saveList = []
    for i in items:
        diction = i.item2dict()
        saveList.append(diction)
    save = open("RezepteRechner/items.json", "w")
    saveJson = json.dumps(saveList)
    save.write(saveJson)
    save.close()

def load() -> None:
    if os.path.isfile("RezepteRechner/items.json"):
        global items, itemNames
        with open("RezepteRechner/items.json", "r") as outfile:
            saveList = json.load(outfile)
        outfile.close
        for i in saveList:
            for name in i["name"]:
                itemNames.append(name)
            items.append(ItemCreation.Item(diction=i))

def lineClearer(lines: int) -> None:
    for i in range(lines):
        print(lnUp, end=lnClear)

def editRecipe(recipe):
    # Abfrage welche Items erzeugt werden
    item = input("Was soll erzeugt werden?: ")
    itemNameList = [item]

    if input("Wird bei diesem Rezept noch ein Item erzeugt?: ") in nf.ja():
        moreItems = True
        while moreItems:
            item = input("Wie heißt dieses Item?: ")
            itemNameList.append(item)
            if not input("Wird bei diesem Rezept noch ein Item erzeugt?: ") in nf.ja():
                moreItems = False
            
    recipe.name = itemNameList
    print()
    # Abfrage wie viele Items erzeugt werden
    for i in itemNameList:
        recipe.changeOutput({f"{i}": int(input(f"Wie viel von \"{i}\" wird erzeugt?: "))})

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
            
    print()
    # Abfrage wie viele Items gebraucht werden
    for i in itemNameList:
        recipe.changeInput({f"{i}": int(input(f"Wie viel von \"{i}\" wird benötigt?: "))})
            
    return recipe


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
    "delRecipe": {
        "beschr": "Erlaubt das Löschen von zuvor erstellten Rezepten",
        "parameters": None
    },
    "rechner": {
        "beschr": "Der Rechner, mit welchem man die Recourcen für die Rezepte rechnen kann",
        "parameters": None
    },
    "help": {
        "beschr": "Gibt eine liste an allen Befehlen mit der jeweiligen beschreibung aus",
        "parameters": None
    },
    "exit": {
        "beschr": "Schließt das Script",
        "parameters": None
    }
}

items = []
itemNames = []

lnUp = '\033[1A'
lnClear = '\x1b[2K'
red = "\033[0;31m"
normal = '\033[0m'

dist = 15

main = True
getOption = True

load()
printTitle()
while main:
    while getOption:
        option = [para.strip() for para in input().split("\"")]
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
        option = []

    # Zum hinzufügen von Rezepten
    elif option[0] == "addRecipe":
        addItemMode = True
        clear()
        printAddItemMode()
        while addItemMode:
            newItem = editRecipe(ItemCreation.Item(["newItem"]))
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
        option = []
    
    # Listet alle bisher erstellten Rezepte
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
        option = []
    
    # Um ein Rezept bearbeiten zu können
    elif option[0] == "editRecipe":
        clear()
        printEditRecipe()
        if len(option) > 1:
            itemName = option[1]
            if itemName in itemNames:
                if input(f"Sind Sie sicher, dass Sie {itemName} ändern möchten?") in nf.ja():
                    for i in items:
                        if itemName in i.name:
                            recipe = i
                    recipe.output = {}
                    recipe.input = {}
                    editRecipe(recipe)
                    save()

        elif len(option) == 1:
            itemName = input("Welches Rezept soll bearbeitet werden?: ")
            if itemName in itemNames:
                if input(f"Sind Sie sicher, dass Sie {itemName} ändern möchten?: ") in nf.ja():
                    for i in items:
                        if itemName in i.name:
                            recipe = i
                    recipe.output = {}
                    recipe.input = {}
                    editRecipe(recipe)
                    save()
        else:
            print("Ungültige Eingabe. Für Hilfe mit oder eine liste von den Optionen, bitte \"help\" eingeben")  
            sleep(3) 
        
        clear()
        save()
        printTitle()
        itemName = ""
        option = []
        getOption = True

    # Um ein Rezept Löschen zu können
    elif option[0] == "delRecipe":
        clear()
        printDelRecipe()
        if len(option) > 1 :
            itemName = option[1]
            if itemName in itemNames:
                print(f"Sind Sie sicher, dass Sie \"{itemName}\" Löschen möchten? Wenn Ja bitte {red}\"LÖSCHEN\"{normal} eingeben")
                if input() == "LÖSCHEN":
                    for i in items:
                        if itemName in i.name:
                            delItem = i
                    delNames = delItem.name
                    for i in delNames:
                        itemNames.remove(i)
                    items.remove(delItem)
                    print(f"\"{itemName}\" wurde erfolgreich entfernt...")
                    input("Enter zum fortfahren drücken...")

        elif len(option) == 1:
            itemName = input("Welches Rezept soll gelöscht werden?: ")
            if itemName in itemNames:
                print(f"Sind Sie sicher, dass Sie \"{itemName}\" Löschen möchten? Wenn Ja bitte {red}\"LÖSCHEN\"{normal} eingeben")
                if input() == "LÖSCHEN":
                    for i in items:
                        if itemName in i.name:
                            delItem = i
                    delNames = delItem.name
                    for i in delNames:
                        itemNames.remove(i)
                    items.remove(delItem)
                    print(f"\"{itemName}\" wurde erfolgreich entfernt...")
                    input("Enter zum fortfahren drücken...")

        else:
            print("Ungültige Eingabe. Für Hilfe mit oder eine liste von den Optionen, bitte \"help\" eingeben")  
            sleep(3)   

        clear()
        save()
        printTitle()
        itemName = ""
        option = []
        getOption = True
    
    # geht in den Rechner Modus
    elif option[0] == "rechner":
        rechner = True
        while rechner:
            clear()
            printRechnerMode()
            itemToCraft, amount = input("Welches Item und wie viel davon soll berechnet werden? Bitte Item und Menge mit einem Komma (,) Trennen.: ").split(",")
            if itemToCraft in itemNames:
                for i in items:
                    if itemToCraft in i.name:
                        item = i
                
                print(amount)
                amount = int(amount)
                amountOfCrafts = int(amount / item.output[itemToCraft]) + (amount % item.output[itemToCraft] > 0)

                itemsToCraft = {}

                for i in item.input:
                    print(i)
                    print(item.input)
                    if i in itemsToCraft:
                        itemsToCraft.update({i, itemsToCraft[i] + (amountOfCrafts * item.input[i])})
                    else:
                        itemsToCraft.update({i, amountOfCrafts * item.input[i]})
                
                print(itemsToCraft)
                input()
            
            else:
                print("Ungültige Eingabe. Vergewissern Sie sich, dass keine Rechtschreibfehler im namen sind")
                sleep(3)

    # Schließt das Script
    elif option[0] == "exit":
        main = False
