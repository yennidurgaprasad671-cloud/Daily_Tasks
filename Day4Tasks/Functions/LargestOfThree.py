#20. Write a Python program with a function that returns the largest of three numbers

def largest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
a=int(input("Enter a value "))
b=int(input("Enter b value "))
c=int(input("Enter c value "))
print("The Largets of Three numbers is ", largest(a,b,c))

