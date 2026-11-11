"""5. Create a Number Guessing Game where:
● The program generates a random number between 1 and 50 using random.
● The user has 5 attempts to guess the number.
● After each guess, calculate the absolute difference using math.fabs() and
display how far the guess is from the correct numbe"""

from random import *
from math import *

a=randint(1,50)
for i in range(1,6):
    n=int(input(f"Enter your {i} guess "))
    d=fabs(a-n)
    if i==5:
        print("Your Guess limit reached")
    
    if d==0:
        print("congratulations Your Guess is Wright")
        break
    else:
        print(f"you are reached in the guess difference is {d}")

    
