#Write a program using break to stop printing numbers when the number reaches 5

num = int(input("Enter a number to break the sequence"))
for i in range (1,100):
    if(i==num):
        break
    print(i)
    
