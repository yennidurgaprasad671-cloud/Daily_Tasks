#15. Write a function to check whether a number is even or odd.

def check_even_odd(num):
    if num%2==0:
        print("Number is Even")
    else:
        print("Number is Odd")
num=int(input("Enter a number "))
check_even_odd(num)
