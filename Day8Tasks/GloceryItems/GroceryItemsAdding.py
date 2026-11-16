n=int(input("Enter how many Items to add"))

with open("grocery.txt","w") as file:
    for i in range(n):
        item=input(f"Enter {i} Item Name: ")
        file.write(item+"\n")
print("GroceryItems Added Successfully ")

