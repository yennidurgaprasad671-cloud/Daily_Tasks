"""A company wants to organize its Python code using packages.
Create a package named utilities that contains two modules:
● math_operations.py (functions for addition and multiplication)
● string_operations.py (functions to convert string to uppercase and count
characters)
Write a Python program that imports the package and uses functions from both modules"""
from Utilities import math_operations
from Utilities import string_operations

a=int(input("Enter a number "))
b=int(input("Enter a number "))
sum_result = math_operations.add(a, b)
product_result = math_operations.multiply(a, b)
print("Addition:", sum_result)
print("Multiplication:", product_result)
sample_text = input("Enter Text to Convert uppercase ")
upper_text = string_operations.to_uppercase(sample_text)
char_count = string_operations.count_characters(sample_text)
print("Uppercase:", upper_text)
print("Character Count:", char_count)
