#Write a program to check whether a number is a Perfect number.

n=int(input("Enter a Number is Perfect or Not "))
t=0

for i in range(1,n):
    if n%i==0:
        t=t+i
        
if t==n:
    print("The Number is Perfect Number ")
else:
    print("The Number is Not a Perfect Number ")
