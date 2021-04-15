class DrawingApi:
    def draw_circle(self, x, y, radius): pass

class DrawingApi1(DrawingApi):
    def draw_circle(self, x, y, radius): 
        print('1 draw',x,y,radius)

class DrawingApi2(DrawingApi):
    def draw_circle(self, x, y, radius): 
        print('2 draw',x,y,radius)

class Shape(object):
    drawing_api = None
    def __init__(self, drawing_api):
        self.drawing_api = drawing_api
    def draw(self): pass
    def resize_by_percentage(self): pass

class CircleShape(Shape):
    def __init__(self, x, y, radius, drawing_api):
        self.x = x
        self.y = y
        self.radius = radius
        super(CircleShape, self).__init__(drawing_api)

    def draw(self):
        self.drawing_api.draw_circle(self.x, self.y, self.radius)
    
    def resize_by_percentage(self):
        print('resize')

s1 = CircleShape(1,2,3,DrawingApi1())
s2 = CircleShape(1,2,3,DrawingApi2())
s1.draw()
s2.draw()