'''Q2: Develop a Python program for a small shop to process customer purchases. Store product 
names and prices in a dictionary, items added to the cart in a list, product categories in a set, 
and product details using tuples. Create functions to display products, add items to the cart, and 
calculate the total bill. Use a recursive function to compute the total price of all items in the cart. 
Include exception handling to manage ValueError (invalid quantity input), ZeroDivisionError 
(calculation errors), TypeError (wrong data types in the cart), and NameError (when a product 
name entered by the user does not exist).'''

# 1. Store products in a dictionary
products = {"Pen": 10, "Notebook": 50, "Pencil": 5}

# 2. Store product categories in a set
categories = {"Stationery", "Writing Supplies", "Office Essentials"}

# 3. Store product details using tuples (Name, Price, Category)
product_details = (
    ("Pen", 10, "Stationery"),
    ("Notebook", 50, "Office Essentials"),
    ("Pencil", 5, "Writing Supplies")
)

# Store items added to the cart globally or pass them around
cart = []


def display_products():
    """Displays all available products and their prices."""
    print("\n--- Available Products ---")
    for name, price in products.items():
        print(f"Product: {name} | Price: ${price}")
    print("--------------------------")


def add_to_cart():
    """Allows the user to add items and quantities to the cart with error handling."""
    display_products()
    try:
        item = input("\nEnter the item name you want to buy: ").strip()
        
        # Check for NameError if the product does not exist in our dictionary
        if item not in products:
            raise NameError(f"Error: The product '{item}' does not exist in the store.")
            
        qty_input = input("Enter quantity: ")
        
        # Check for ValueError if quantity is not a valid integer
        try:
            qty = int(qty_input)
        except ValueError:
            raise ValueError("Error: Invalid quantity input. Please enter a valid integer.")
            
        if qty <= 0:
            raise ValueError("Error: Quantity must be greater than zero.")

        # Append item details as a tuple (item_name, quantity) to the cart list
        cart.append((item, qty))
        print(f"Successfully added {qty} x {item}(s) to your cart.")
        
    except NameError as ne:
        print(ne)
    except ValueError as ve:
        print(ve)


def calculate_recursive_total(cart_items, index=0):
    """Recursive function to compute the total price of all items in the cart."""
    # Base case: if we reach the end of the cart list, return 0
    if index >= len(cart_items):
        return 0
    
    try:
        item_name, quantity = cart_items[index]
        
        # Check for TypeError if data types inside the cart tuple are incorrect
        if not isinstance(item_name, str) or not isinstance(quantity, (int, float)):
            raise TypeError("Error: Wrong data types found in the cart tuple.")
            
        if item_name not in products:
            raise NameError(f"Error: Product '{item_name}' in cart does not exist.")
            
        item_price = products[item_name]
        
        # Calculate subtotal for the current item
        subtotal = item_price * quantity
        
        # Simulate a division check or handling to explicitly incorporate ZeroDivisionError safety
        if quantity == 0:
            raise ZeroDivisionError("Error: Division error encountered during calculation.")
            
        # Recursive step: add current subtotal to the result of the rest of the cart
        return subtotal + calculate_recursive_total(cart_items, index + 1)
        
    except (TypeError, NameError, ZeroDivisionError) as e:
        print(e)
        # Skip the invalid item and continue calculating the rest of the cart
        return calculate_recursive_total(cart_items, index + 1)


def calculate_total_bill():
    """Calculates and displays the final total bill for the cart."""
    if not cart:
        print("\nYour cart is empty.")
        return
        
    print("\n--- Generating Bill ---")
    total_bill = calculate_recursive_total(cart)
    print(f"Total Bill Amount: ${total_bill}")
    print("-----------------------")


# --- Main Menu / Execution Flow ---
if __name__ == "__main__":
    while True:
        print("\n=== Store Menu ===")
        print("1. Display Products")
        print("2. Add Item to Cart")
        print("3. View Total Bill")
        print("4. Exit")
        
        choice = input("Enter choice: ").strip()
        
        if choice == '1':
            display_products()
        elif choice == '2':
            add_to_cart()
        elif choice == '3':
            calculate_total_bill()
        elif choice == '4':
            print("\nThank you for shopping with us. Goodbye!")
            break
        else:
            print("\nInvalid choice! Please enter a number between 1 and 4.")
    
    
