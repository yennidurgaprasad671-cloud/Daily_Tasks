"""5. Employee Management System (OOP + File + Dict)
Scenario:
Manage employee data.
Task:
● Create a class Employee
● Store employees in a dictionary
● Save data to a file
● Use exception handling for invalid salary input
● Use loop to display all employees"""

class Employee:

  def __init__(self, emp_id, name, salary):
    self.emp_id = emp_id
    self.name = name
    self.salary = salary

  def __str__(self):
    return f"ID: {self.emp_id} | Name: {self.name} | Salary: ${self.salary:,.2f}"


employees = {}

while True:
  emp_id = input("\nEnter Employee ID (or 'done' to finish): ").strip()
  if emp_id.lower() == "done":
    break

  name = input("Enter Employee Name: ").strip()

  try:
    salary = float(input("Enter Salary: "))
    if salary < 0:
      raise ValueError("Salary cannot be negative.")
    employees[emp_id] = Employee(emp_id, name, salary)
  except ValueError as e:
    print(f"Invalid salary input: {e}. Employee not added.")

# Save data to a file
try:
  with open("employees.txt", "w") as file:
    for emp in employees.values():
      file.write(f"{emp.emp_id},{emp.name},{emp.salary:.2f}\n")
except IOError as e:
  print(f"Error saving file: {e}")

# Use loop to display all employees
print("\n--- Employee Directory ---")
for emp in employees.values():
  print(emp)
