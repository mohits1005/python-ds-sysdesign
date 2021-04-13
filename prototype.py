import copy
class Shape(object):
    def __init__(self, sides):
        self.sides = sides
    def show(self):
        print("shape of sides",self.sides)
    def clone(self):
        return copy.copy(self)

class Type1(Shape):
    def __init__(self, sides):
        super(Type1, self).__init__(sides)

t = Type1(4)
t.show()
t2 = t.clone()
t2.show()