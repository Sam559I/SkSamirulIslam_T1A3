import csv
import datetime

# Global variable to store grocery items
grocery_items = []

# Function to load grocery items
def load_grocery_items():
    global grocery_items
    grocery_items = []
    with open("src/grocery_items.csv", mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            grocery_items.append(row)


# Function to add grocery items
def write_grocery_items():
    with open("grocery_items.csv", mode="w", newline="") as file:
        fieldnames = ["Name", "Category", "Price", "Quantity", "Expiration Date"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for item in grocery_items:
            writer.writerow(item)


# Function to display current stock
def display_current_stock():
    print("\nCurrent Stock of Grocery Items:")
    for item in grocery_items:
        print(
            f"{item['Name']}: {item['Quantity']} {item['Category']} - ${item['Price']}"
        )


# Function to search for a specific product
def search_product(product_name):
    found = False
    for item in grocery_items:
        if item["Name"].lower() == product_name.lower():
            print(f"\nProduct Found:")
            print(f"Name: {item['Name']}")
            print(f"Category: {item['Category']}")
            print(f"Quantity: {item['Quantity']}")
            print(f"Price: ${item['Price']}")
            found = True
            break
    if not found:
        print("\nProduct not found.")


def quantity_update_groceries():
    product_name = input("Enter the name of the product: ")
    quantity_change = int(
        input("Enter the quantity to add (positive) or remove (negative): ")
    )
    for item in grocery_items:
        if item["Name"].lower() == product_name.lower():
            item["Quantity"] = str(int(item["Quantity"]) + quantity_change)
            write_grocery_items()
            print("\nQuantity updated successfully.")
            return
    print("\nProduct not found.")


def display_items_by_category():
    category = input("Enter the category to display items: ").strip().capitalize()
    print(f"\nGrocery Items in the Category '{category}':")
    category_items = [
        item for item in grocery_items if item["Category"].capitalize() == category
    ]
    if category_items:
        for item in category_items:
            print(f"{item['Name']}: {item['Quantity']} - ${item['Price']}")
    else:
        print("No items found in the specified category.")
