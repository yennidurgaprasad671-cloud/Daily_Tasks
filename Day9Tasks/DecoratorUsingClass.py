"""7. Employee Bonus Calculator (Decorators & OOP)
A company wants to apply a bonus calculation automatically before displaying the
salary. Create an Employee class and use a decorator that modifies the salary by
adding a bonus before displaying it."""

# 1. Define a simple decorator
def add_bonus(func):
    def wrapper(self):
        self.salary += 5000  # Add a flat bonus of 5,000
        return func(self)

    return wrapper


# 2. Define the Employee class
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # 3. Apply the decorator
    @add_bonus
    def display_salary(self):
        print(f"Employee: {self.name}")
        print(f"Final Salary: ₹{self.salary}")


# --- Run the code ---
emp = Employee("Rahul", 50000)
emp.display_salary()
