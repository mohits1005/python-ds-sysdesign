from abc import abstractmethod
class Duck:
    @abstractmethod
    def quack(self):
        pass
    @abstractmethod
    def fly(self):
        pass

class MallardDuck(Duck):
    def quack(self):
        print("quack")
    def fly():
        print("Fly Fly Fly Fly")

class Turkey:
    @abstractmethod
    def gobble(self):
        pass
    @abstractmethod
    def fly(self):
        pass

class WildTurkey(Turkey):
    def gobble(self):
        print("gobble")
    def fly(self):
        print("fly for a short distance")

# Suppose that we are short on Ducks and the solution is to use some
# Turkey objects in their place. To do this, we would need to create
# an adapter:

class TurkeyAdapter(Duck):
    def __init__(self, turkey):
        self.turkey = turkey
    def quack(self):
        self.turkey.gobble()
    def fly(self):
        self.turkey.fly()
    
duck = MallardDuck()
turkey = WildTurkey()
turkeyAdapter = TurkeyAdapter(turkey)
turkeyAdapter.quack()
turkeyAdapter.fly()
