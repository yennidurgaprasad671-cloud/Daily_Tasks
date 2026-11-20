"""15. Infinite Even Number Generator (Generators)
Create a generator function that continuously generates even numbers starting from
2. The program should print the first N even numbers using this generator."""
def infinite_even_numbers():
    num = 2
    while True:
        yield num
        num += 2

# Input: Number of even numbers to generate
n = int(input("Enter the value of N: "))

# Initialize the generator
even_gen = infinite_even_numbers()

# Print the first N even numbers
print(f"First {n} even numbers:")
for _ in range(n):
    print(next(even_gen), end=" ")
