class SubSystemA:
    def method(self):
        return "A"

class SubSystemB:
    def method(self):
        return "B"

class Facade:
    def __init__(self):
        self.subsystemA = SubSystemA()
        self.subsystemB = SubSystemB()
    
    def method(self):
        return self.subsystemA.method()+self.subsystemB.method()

f = Facade()
print(f.method())