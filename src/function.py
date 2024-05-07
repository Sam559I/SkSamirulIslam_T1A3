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
