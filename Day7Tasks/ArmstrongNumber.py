#Write a program to check whether a given number is an Armstrong number or not

n=int(input("Enter a Number to Find ArmStrong number or not "))
s=len(str(n))
n2=n
t=0
while(n>0):
    l=n%10
    t=t+(l**s)
    n=n//10
if t==n2:
    print("The Given number is Armstrong Number ")
else:
    print("The Number is No Armstrong Number ")
