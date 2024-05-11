from current_stock_function import write_grocery_items
import csv

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


def compare_prices_for_product():
    global grocery_items

    product_name = input("Enter the name of the product to compare prices: ")

    marketplace1 = "Marketplace-1.csv"
    marketplace2 = "Marketplace-2.csv"
    marketplace3 = "Marketplace-3.csv"

    marketplace_prices1 = {}
    marketplace_prices2 = {}
    marketplace_prices3 = {}

    with open(marketplace1, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            marketplace_prices1[row["Name"]] = float(row["Price"])

    with open(marketplace2, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            marketplace_prices2[row["Name"]] = float(row["Price"])

    with open(marketplace3, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            marketplace_prices3[row["Name"]] = float(row["Price"])

    print(f"\nPrice Comparison for '{product_name}' with Marketplaces:")
    for item in grocery_items:
        if item["Name"].lower() == product_name.lower():
            price1 = marketplace_prices1.get(item["Name"], "Not Available")
            price2 = marketplace_prices2.get(item["Name"], "Not Available")
            price3 = marketplace_prices3.get(item["Name"], "Not Available")

            print(
                f"{item['Name']}: Our Price - ${item['Price']} | Marketplace 1 Price - ${price1} | Marketplace 2 Price - ${price2} | Marketplace 3 Price - ${price3}"
            )
            return

    print(f"No product named '{product_name}' found in the current stock.")
