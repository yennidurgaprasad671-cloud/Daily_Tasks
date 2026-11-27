"""2. Random Number Analyzer
Scenario:
A system generates random numbers for testing.
Task:
● Use random to generate 10 numbers
● Store in a list
● Use loop + condition to count even/odd numbers
● Use set to remove duplicates
"""
import random

# 1. Use random to generate 10 numbers and store in a list
# (Using range 1 to 10 so duplicates are likely to appear)
random_numbers = [random.randint(1, 10) for _ in range(10)]

# 2. Use loop + condition to count even and odd numbers
even_count = 0
odd_count = 0

for num in random_numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# 3. Use set to remove duplicates
unique_numbers = set(random_numbers)

# Display the results
print("Generated Numbers:", random_numbers)
print("Even Numbers Count:", even_count)
print("Odd Numbers Count:", odd_count)
print("Unique Numbers (No Duplicates):", unique_numbers)
