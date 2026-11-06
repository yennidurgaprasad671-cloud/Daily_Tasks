#3. Write a recursive function to calculate the sum of digits of a number.
#Example: Input = 123 → Output = 6

def sum(n):
    total=0
    while(n>0):
        s=n%10
        total+=s
        n=n//10
    return total
n=int(input("Entera value to sum of Digits "))
print("Sum of digits is ",sum(n))
