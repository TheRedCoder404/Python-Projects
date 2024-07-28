import json
import sys
sys.path.append('../Git/RezepteRechner')
import ItemCreation
sys.path.append('../Git/nuetzliche_functions')
import nuetzliche_functions as nf

newItem = ItemCreation.Item(["Reactor (Blazing)"])
newItem.changeOutput({"Reactor (Blazing)": 4})
newItem.changeInput({"Reactor (Hardened)": 4, "Blazing Capacitor": 4, "Uraninite": 1})

newItem2 = ItemCreation.Item(["Reactor (Hardened)"])
newItem.changeOutput({"Reactor (Hardened)": 4})
newItem.changeInput({"Reactor (Basic)": 4, "Basic Capacitor": 4, "Uraninite": 1})

saveList = [newItem.item2dict(), newItem2.item2dict()]

with open("RezepteRechner/test.json", "w") as outfile:
    json.dump(saveList, outfile)

outfile.close()