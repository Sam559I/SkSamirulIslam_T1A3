"""
Grocery Tracker App

This Python script implements a terminal-based grocery tracking application.
Users can display current stock, search for specific products, order groceries, track
expired perishable food items, and compare prices.

"""
from search import search_product
import csv
from grocery import (
    load_grocery_items,
    display_current_stock,
    quantity_update_groceries,
    display_items_by_category,
    track_expiring_soon,
)

grocery_items = []

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


# Main function
def main():
    load_grocery_items()
    while True:
        print("\n")
        print("╔══════════════════════════════════════════════════════════════════════════╗")
        print("║                       Welcome to the Grocery                             ║")
        print("║                             Tracker App!                                 ║")
        print("╚══════════════════════════════════════════════════════════════════════════╝")
        print("Menu Options:")
        print("1. Display Current Stock")
        print("2. Search for a Product")
        print("3. Update Groceries")
        print("4. Track Expired Perishable Food Items")
        print("5. Price Comparison")
        print("6. Display Items by Category")
        print("7. Place Order")
        print("8. Exit")
        choice = input("Enter your choice: ")
        try:
            choice = int(choice)
            if choice == 1:
                display_current_stock()
            elif choice == 2:
                product_name = input("Enter the name of the product to search: ")
                search_product(product_name)
            elif choice == 3:
                quantity_update_groceries()
            elif choice == 4:
                track_expiring_soon()
            elif choice == 5:
                compare_prices_for_product()
            elif choice == 6:
                display_items_by_category()
            elif choice == 7:
                place_order()
            elif choice == 8:
                print("\nThank you for using the Grocery Tracker App. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()
