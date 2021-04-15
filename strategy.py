class QuackStrategy(object):
    def quack(self): pass

class LoudQuackStrategy(QuackStrategy):
    def quack(self):
        print("QUACK QUACK")

class GentleQuackStrategy(QuackStrategy):
    def quack(self):
        print("quack")

class LightStrategy(object):
    def lights_on(self): pass

class OnForTenSecondStrategy(LightStrategy):
    def lights_on(self):
        print("lights on for 10 seconds")


gentle_quack = GentleQuackStrategy()
loud_quack = LoudQuackStrategy()
ten_seconds = OnForTenSecondStrategy()

class Duck(object):
    def __init__(self, quackStrategy, lightStrategy):
        self.quackStrategy = quackStrategy
        self.lightStrategy = lightStrategy
    def quack(self):
        self.quackStrategy.quack()
    def lights_on(self):
        self.lightStrategy.lights_on()

class VillageDuck(Duck):
    def __init__(self):
        super(VillageDuck, self).__init__(loud_quack, None)
    def go_home(self):
        print("going to river")

class ToyDuck(Duck):
    def __init__(self):
        super(ToyDuck, self).__init__(gentle_quack, ten_seconds)

class CityDuck(Duck):
    def __init__(self):
        super(CityDuck, self).__init__(gentle_quack, None)

    def go_home(self):
        print("going to park pond")

class RobotDuck(Duck):
    def __init__(self):
        super(RobotDuck, self).__init__(loud_quack, ten_seconds)


robo = RobotDuck()
robo.quack()
robo.lights_on()    
