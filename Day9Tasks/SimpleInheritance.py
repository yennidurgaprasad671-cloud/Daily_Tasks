"""3. Employee Salary System (Simple Inheritance)
A company has two types of employees: Employee and Manager. Create a base class
Employee containing name and salary. Create a derived class Manager that inherits
from Employee and displays the employee details."""
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
class Manager(Employee):
    def print_details(self):
        print(f"Name Of Employee is {self.name}")
        print(f"Salary of Employeee is {self.salary}")
emp=Manager("Prasad",35000)
emp.print_details()
