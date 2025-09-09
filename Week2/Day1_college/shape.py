class shape:
    def __init__(self, name):
        self.name = name
    
    def area(self):
        pass

class rectangle(shape):
    def __init__(self, length, breadth):
        super().__init__("rectangle")
        self.length = length
        self.breadth = breadth
        
    def area(self):
        return self.length * self.breadth
    
class circle(shape):
    def __init__(self, radius):
        super().__init__("circle")
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius * self.radius
    

c = circle(5)
print("Area of circle:", c.area())

r = rectangle(4, 5)
print("Area of rectangle:", r.area())
