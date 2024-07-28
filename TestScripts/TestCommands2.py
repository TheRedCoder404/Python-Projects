import json
import sys
sys.path.append('../Git/RezepteRechner')
import ItemCreation
sys.path.append('../Git/nuetzliche_functions')
import nuetzliche_functions as nf

items = []

with open("RezepteRechner/test.json", "r") as outfile:
    saveList = json.load(outfile)
outfile.close

for i in saveList:
    items.append(ItemCreation.Item(diction=i))

for i in items:
    print(i.name)