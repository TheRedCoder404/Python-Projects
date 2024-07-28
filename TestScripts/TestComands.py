import json

save = open("RezepteRechner/test.json", "w")
test = json.dumps([{"test": "Alos"}, {"Moin": "ws"}])
save.write(test)
save.close