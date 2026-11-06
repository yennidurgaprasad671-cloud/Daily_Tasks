#2. Write a recursive function to find the nth Fibonacci number.

def fib(n):
    if n==0 or n==1:
        return n
    else:
        return fib(n-1)+fib(n-2)
n=int(input("Enter The Number "))
print("The Fibinacci number is ",fib(n))
