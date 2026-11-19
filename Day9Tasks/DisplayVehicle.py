"""5. Vehicle Management System (Inheritance)
A transport company manages different vehicles. Create a base class Vehicle with
attributes like brand and speed. Create derived classes Car and Bike that inherit from
Vehicle and display their details."""
class Vehicle:
    def __init__(self, brand, speed):
        self.brand=brand
        self.speed=speed

class Car(Vehicle):
    def display(self):
        print(f"Brand : {self.brand}")
        print(f"speed : {self.speed} km/hr")

class Bike(Vehicle):
    def display(self):
        print(f"Brand : {self.brand}")
        print(f"speed : {self.speed} km/hr")
c=Car("suzuki",300)
c.display()
b=Bike("Pulsar",120)
b.display()
