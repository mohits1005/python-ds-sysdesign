class PrintText:
    def __init__(self,text):
        self.text = text
    def printthis(self):
        return self.text

class BoldText:
    def __init__(self, textObject):
        self.textObject = textObject
    def printthis(self):
        return '<b>'+self.textObject.printthis()+'<b>'

class ItalicsText:
    def __init__(self, textObject):
        self.textObject = textObject
    def printthis(self):
        return '<i>'+self.textObject.printthis()+'<i>'

p = PrintText("print me")
i = ItalicsText(BoldText(p))
print(i.printthis())