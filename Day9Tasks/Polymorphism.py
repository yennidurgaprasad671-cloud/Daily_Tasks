"""6. Shape Area Calculator (Polymorphism)
A graphics application needs to calculate the area of different shapes. Create classes
Circle, Rectangle, and Triangle, each having an area() method. Demonstrate
polymorphism by calling the same method for different objects."""

class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        pi=3.14
        area_circle=pi*self.radius*self.radius
        return area_circle
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        rectangle_area=self.length*self.width
        return rectangle_area
class Traingle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height

shapes =[Circle(5),Rectangle(20,30),Traingle(30,20)]
for s in shapes:
    print(s.area())

    
