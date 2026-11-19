""". Student Information System (Class & Object)
A school wants a program to store student details. Create a Student class with
attributes such as name, roll number, and marks. Create objects for at least three
students and display their details."""
class student:
    def __init__(self,name ,rollNo,marks):
        self.name = name
        self.rollNo=rollNo
        self.marks=marks
    def display(self):
        print(f" Name Of the Student :{self.name}")
        print(f" marks Of the Student :{self.marks}")
        print(f" rollNo Of the Student :{self.rollNo}")

s=student("Prasad",4,99)
s1=student("Charan",2,90)
s3=student("Manoj",3,89)
s.display()
s1.display()
s3.display()
        
    
