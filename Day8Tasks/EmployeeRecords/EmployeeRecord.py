"""6. Employee Salary Management System
A company stores employee data in a file employees.txt in the format:
EmployeeName Salary
Example:
Ramesh 25000
Sita 30000
Arun 28000
Write a Python program that:
● Reads employee data from the file
● Displays all employee details
● Finds the employee with the highest salary
● Appends a new employee record to the file"""
highest_salary = -1
top_employee = ""

print("--- Employee Details ---")
try:
    with open("employees.txt", "r") as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 2:
                name = parts[0]
                salary = float(parts[1])
                print(f"Employee: {name} | Salary: {salary}")
                
                if salary > highest_salary:
                    highest_salary = salary
                    top_employee = name

    if top_employee:
        print(f"\nHighest Paid Employee: {top_employee} ({highest_salary})")
    else:
        print("\nNo employee records found.")

except FileNotFoundError:
    print("employees.txt not found. A new file will be created.")

# Append a new employee record
print("\n--- Add New Employee ---")
new_name = input("Enter new employee name: ")
new_salary = input("Enter new employee salary: ")

with open("employees.txt", "a") as file:
    file.write(f"\n{new_name} {new_salary}")

print("New employee record added successfully!")
