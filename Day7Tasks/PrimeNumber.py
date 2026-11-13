#Write a program to check whether a number is Prime.

n=int(input("Enter a number to check primeor not "))
c=0
for i in range(1,n+1):
    print(i)
    if n%i==0:
        c=c+1
if c==2:
    print("The Numbe is Prime Number ")
else:
    print("Not Prime Number")
    
