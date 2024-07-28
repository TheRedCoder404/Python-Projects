class Item:
    
    def __init__(self, name: list = None, diction: dict = None) -> None:
        self.name = name
        self.diction = diction
        self.output = {}
        self.input = {}

        if diction != None:
            self.name = diction["name"]
            self.output = diction["output"]
            self.input = diction["input"]

    def changeOutput(self, output: dict) -> None:
        self.output.update(output)

    def changeInput(self, input: dict) -> None:
        self.input.update(input)

    def item2dict(self, item) -> dict:
        diction: dict = {"name": item.name, "output": item.output, "input": item.input}
        return diction
