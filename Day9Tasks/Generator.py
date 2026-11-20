"""8. Random Number Generator (Generators)
A program is needed to generate numbers for testing purposes. Create a generator
function that produces numbers from 1 to N and prints them one by one when iterated."""

def generator(n):
    for i in range(1,n):
        yield i

n=int(input("ENter a Number "))
for num in generator(n):
    print(num)
