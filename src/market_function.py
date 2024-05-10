from current_stock_function import write_grocery_items
import csv
import 

# Global variable to store grocery items
grocery_items = []


# Function to place an order
def place_order():
    global grocery_items
    total_cost = 0
    print("\nPlace an Order:")
    marketplace_number = input("Enter the marketplace number to order from: ")
    marketplace_file = f"Marketplace-{marketplace_number}.csv"

    # Load grocery items from the selected marketplace CSV file
    marketplace_items = []
    with open(marketplace_file, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            marketplace_items.append(row)

    num_items = int(input("Enter the number of items: "))
    for i in range(num_items):
        item_name = input(f"Enter the name of item {i + 1}: ")
        quantity = int(input(f"Enter the quantity of {item_name}: "))
        for item in marketplace_items:
            if item["Name"].lower() == item_name.lower():
                total_cost += float(item["Price"]) * quantity
                break

    # Update quantities in the current stock
    for item in grocery_items:
        for order_item in marketplace_items:
            if item["Name"].lower() == order_item["Name"].lower():
                item["Quantity"] = str(int(item["Quantity"]) + quantity)
                break

    # Write updated grocery items to CSV
    write_grocery_items()
