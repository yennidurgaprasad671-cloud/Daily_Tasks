#16. Write a function that returns the factorial of a number.

def factorial(n):
    if n==0 or n==1:
        return 1
    else :
        factorial=1
        for i in range(2,n+1):
            factorial*=i
        return factorial
n=int(input("Enter a number to find Factorial "))
print("The Factorial of a number is ",factorial(n))

            
    
