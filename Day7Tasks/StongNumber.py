#Write a program to check whether a given number is a Strong numbe

def factorial(n):
    if n==0 or n==1:
        return n
    else:
        return n*factorial(n-1)
number =int(input("Enter a number to Find Strong or Not "))
n2=number
t=0
while(number>0):
    l=number%10
    t=t+factorial(l)
    number=number//10
if t==n2:
    print("The Given Number is Strog Number ")
else:
    print("The Number is Not Strong Number ")

    
    
