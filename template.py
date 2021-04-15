class MakeMeal(object):
    def prepare(self):pass
    def cook(self):pass
    def eat(self):pass
    def go(self):
        self.prepare()
        self.cook()
        self.eat()

class MakePizza(MakeMeal):
    def prepare(self):
        print("Prepare Pizze")
    
    def cook(self):
        print("Cook Pizza")
    
    def eat(self):
        print("Eat Pizza")

m = MakePizza()
m.go()