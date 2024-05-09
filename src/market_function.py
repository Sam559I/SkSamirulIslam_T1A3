

# Global variable to store grocery items
grocery_items = []

# Function to add or adjust quantities of items

def place_order():
    total_cost = 0
    print("\nPlace an Order:")
    num_items = int(input("Enter the number of items: "))
    for i in range(num_items):
        item_name = input(f"Enter the name of item {i + 1}: ")
        quantity = int(input(f"Enter the quantity of {item_name}: "))
        for item in grocery_items:
            if item["Name"].lower() == item_name.lower():
                total_cost += float(item["Price"]) * quantity
                break
    print(f"\nTotal cost of the order: ${total_cost:.2f}")
