inventory = [("shirt", 2, 200), ("pant", 4, 800), ("phone", 1, 18000)]

def calculate_total_cost():
    """Calculate the total cost of all items in the inventory."""
    return sum(qty * price for _, qty, price in inventory)

print("\n-------------- Current Inventory --------------")
for item in inventory:
    print(f"Item: {item[0]}, Quantity: {item[1]}, Price per unit: {item[2]}")


n = int(input("\nEnter the number of items you want to add: "))
for i in range(n):
    name = input("Enter the name of the item: ").strip()
    quantity = int(input("Enter the quantity: "))
    price = int(input("Enter the price per unit: "))
    inventory.append((name, quantity, price))

print("\n-------------- Updated Inventory --------------")
for item in inventory:
    print(f"Item: {item[0]}, Quantity: {item[1]}, Price per unit: {item[2]}")

item_to_remove = input("\nEnter the name of the item you want to remove: ").strip()
found = False
for item in inventory:
    if item[0].lower() == item_to_remove.lower():
        inventory.remove(item)
        found = True
        print(f"Item '{item_to_remove}' has been removed.")
        break

if not found:
    print(f"Item '{item_to_remove}' not found in the inventory.")

total_cost = calculate_total_cost()
print(f"\nTotal cost of inventory: {total_cost}")

if total_cost >= 10000:
    print("10% discount applicable.")
elif 5000 <= total_cost < 10000:
    print("5% discount applicable.")
else:
    print("No discount applicable.")
