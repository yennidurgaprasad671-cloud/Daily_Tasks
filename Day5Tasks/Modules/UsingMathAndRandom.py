"""4. Write a Python program that generates 20 random numbers between 1 and 200 using
the random module and store them in a list.
Then using the math module, compute and display:
● Maximum value
● Minimum value
● Square root of the maximum number
● Logarithm of the minimum number """

from random import *
from math import *
l=[]
for i in range(1,21):
    l.append(randint(1,200))
print(l)
max_value=max(l)
min_value=min(l)
print("The max Value in The List is",max_value)
print("The value in the list is  ",min_value)
print("The square of a max number is ", sqrt(max_value))
print("The logoritham of a minimum number is ",log(min_value))

    
