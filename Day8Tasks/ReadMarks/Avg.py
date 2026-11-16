"""4. Student Marks File Analyzer
A teacher stores student marks in a file marks.txt in the format:
Name Marks
Example:
Rahul 80
Anita 90
Ravi 75
Write a Python program to:
● Read the file
● Display all student records
● Calculate and display the average marks of the clas"""

m=0
c=0
try:
    with open("marks.txt","r") as file:
        for line in file:
            parts=line.strip().split()
            marks=float(parts[1])
            name=parts[0]
            print(f"name : {name} and Marks : {marks}")
            m=m+marks
            c=c+1
    avg=m/c
    print("Avg Marks are ", avg)
except FileNotFoundError:
    print("file Not Found Please Check once ")
        
        
        
        
