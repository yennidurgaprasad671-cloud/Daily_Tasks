"""9. Online Shopping System (Multilevel Inheritance)
An e-commerce company organizes products using multiple levels. Create classes
Product → ElectronicProduct → MobilePhone using multilevel inheritance and
display product details."""

class Product:
    def __init__(self,name, product_id):
        self.name= name
        self.product_id=product_id
    def display(self):
        print(f"Name : {self.name} ")
        print(f"Product ID : {self.product_id}")
class ElectronicProduct(Product):
    def __init__(self,name,product_id,price ,warranty):
        super().__init__(name,product_id)
        self.price =price
        self.warranty= warranty
    def display(self):
        super().display()
        print(f"Price : {self.price}")
        print(f"Warranty : {self.warranty} ")
class MobilePhone(ElectronicProduct):
    def __init__(self,name,product_id,price ,warranty, ram ,storage):
        super().__init__(name,product_id,price,warranty)
        self.ram = ram
        self.storage = storage
    def display(self):
        super().display()
        print(f"Ram : {self.ram}GB")
        print(f"Strorage : {self.storage}GB")
phone = MobilePhone(
    product_id="ELEC101",
    name="Galaxy S26",
    price=799.99,
    warranty=2,
    ram=12,
    storage=256
)
phone.display()
