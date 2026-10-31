#3. Write a program to find the sum of numbers from 1 to N using a loop.

num= int(input("Enter a number "))
total=0
for i in range(1,num+1):
    total+=i
print(f"Sum of Numbers 1 to {num} is ",total)
