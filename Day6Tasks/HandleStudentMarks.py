'''Q1: Develop a Python program to manage student marks for three subjects. Store the subject
names in a tuple, maintain unique student names in a set, and store each student’s marks
in a list inside a dictionary where the key is the student name. Create user-defined
functions to add a student with marks, display all student records, and calculate the average
marks of a student. Implement a recursive function to calculate the total marks from the list of
marks. The program should interact with the user through a simple menu. Also include
exception handling to handle ValueError (non-numeric marks input), ZeroDivisionError
(average calculation issues), TypeError (incorrect data type in marks), and NameError (when a
student name entered does not exist in the dictionary).'''

t = ("English", "Telugu", "Hindi")
s = set()
d = {}

def add_user():
    try:
        u = input("Enter student name: ").strip()
        if not u:
            raise ValueError("Student name cannot be empty.")
        s.add(u)
        m = []
        for i in range(3):
            try:
                e = int(input(f"Enter marks for {t[i]}: "))
                # Ensure marks are numeric and of correct type
                if not isinstance(e, int):
                    raise TypeError("Marks data type error.")
                m.append(e)
            except ValueError:
                print("Invalid input! Please enter numeric marks.")
                return  # Exit function if input fails
        d[u] = m
        print("Student added successfully!")
    except Exception as err:
        print(f"Error adding student: {err}")

def display_students():
    if not d:
        print("No student records found.")
    else:
        for name, marks in d.items():
            print(f"{name} : {marks}")

def total_marks(marks):
    # Raises TypeError if elements are not numbers
    if not marks:
        return 0
    if not isinstance(marks[0], (int, float)):
        raise TypeError("Marks data type error.")
    return marks[0] + total_marks(marks[1:])

def avg():
    try:
        name = input("Enter student name to calculate average: ").strip()
        
        # Check NameError requirement when student does not exist
        if name not in d:
            raise NameError("Student name not found.")
            
        marks = d[name]
        
        # Verify data types inside marks list
        for mark in marks:
            if not isinstance(mark, (int, float)):
                raise TypeError("Marks data type error.")
                
        total = total_marks(marks)
        
        # Check ZeroDivisionError if list is empty
        if len(marks) == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
            
        average = total / len(marks)
        print("Total Marks:", total)
        print(f"Average Marks: {average:.1f}")
        
    except NameError as ne:
        print(ne)
    except ZeroDivisionError as zde:
        print(zde)
    except TypeError as te:
        print(te)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    while True:
        print("\n1. Add Student")
        print("2. Display Students")
        print("3. Calculate Average")
        print("4. Exit")
        
        try:
            choice = int(input("Enter choice: "))
            if choice == 1:
                add_user()
            elif choice == 2:
                display_students()
            elif choice == 3:
                avg()
            elif choice == 4:
                print("Exiting program.")
                break
            else:
                print("Invalid choice! Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input! Please enter a valid integer choice.")

if __name__ == "__main__":
    main()



    
