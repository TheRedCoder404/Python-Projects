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
            self.diction = None

    def changeOutput(self, output: dict) -> None:
        self.output.update(output)

    def changeInput(self, input: dict) -> None:
        self.input.update(input)

    def getLongestOut(self) -> int:
        length: int = 0
        for i in self.output:
            if len(i) > length:
                length = len(i)
        return length

    def item2dict(item):
        return item.__dict__
