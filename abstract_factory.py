class CarFactory:
    def createEngine(self): pass
    def createCar(self): pass

class PublicCar(CarFactory):
    def createEngine(self):
        print("public car engine created")
    def createCar(self):
        print("public car created")

class MilitaryCar(CarFactory):
    def createEngine(self):
        print("military car engine created")
    def createCar(self):
        print("military car created")

p = PublicCar()
m = MilitaryCar()
p.createEngine()
p.createCar()
m.createEngine()
m.createCar()