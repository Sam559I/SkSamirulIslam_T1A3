from grocery import write_grocery_items
import csv

# Global variable to store grocery items
grocery_items = []

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

