"""3. Shopping Cart System
Scenario: A user adds items to a shopping cart.
Task:
● Store items in a list
● Convert to set to remove duplicates
● Use loop + condition to calculate total cost
● Handle invalid input using try-except"""
price_catalog = {
    "apple": 1.50,
    "banana": 0.75,
    "milk": 3.20,
    "bread": 2.50,
    "eggs": 4.00,
}

cart_items = []

print("Available items:", ", ".join(price_catalog.keys()))
print("Enter item names to add to cart (type 'done' to finish):")

while True:
  try:
    item = input("Add item: ").strip().lower()
    if item == "done":
      break
    if not item or item.isdigit():
      raise ValueError("Item name cannot be empty or numeric.")
    cart_items.append(item)
  except ValueError as e:
    print(f"Invalid input: {e}")

# Convert to set to remove duplicates
unique_items = set(cart_items)

# Use loop + condition to calculate total cost
total_cost = 0.0
for item in unique_items:
  if item in price_catalog:
    total_cost += price_catalog[item]
  else:
    print(f"Warning: '{item}' is not in catalog and was skipped.")

print(f"\nUnique Items in Cart: {unique_items}")
print(f"Total Cost: ${total_cost:.2f}")
