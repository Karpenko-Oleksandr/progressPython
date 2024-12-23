class Line:
    name = "Line"
    sm = "Something"

    def draw(self):
        print("Line")

class Circle(Line):
    name = "Circle"

    def draw(self):
        print("Circle")

class Rectangle(Circle):
    name = "Rectangle"
    

l = Line()
g = Circle()
r = Rectangle()

l.draw()
g.draw()
print(r.sm)