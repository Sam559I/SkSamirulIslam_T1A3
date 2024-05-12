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


# Function to track items that will expire in the next  month/ 30 days
def track_expiring_soon():
    today = datetime.date.today()
    one_months_from_now = today + datetime.timedelta(days=30)
    print("\nItems Expiring in the Next 30 days:")
    expiring_items = []
    for item in grocery_items:
        if "Expiration Date" in item:
            expiration_date = datetime.datetime.strptime(
                item["Expiration Date"], "%d/%m/%Y"
            ).date()
            if today <= expiration_date <= one_months_from_now:
                expiring_items.append(item)
    if expiring_items:
        for item in expiring_items:
            print(f"{item['Name']} - Expires on {item['Expiration Date']}")
    else:
        print("No items are expiring in the next 6 months.")
