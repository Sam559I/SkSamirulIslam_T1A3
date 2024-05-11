"""
Grocery Tracker App

This Python script implements a terminal-based grocery tracking application.
Users can display current stock, search for specific products, order groceries, track
expired perishable food items, and compare prices.

"""
from market_function import place_order

from current_stock_function import (
    load_grocery_items,
    display_current_stock,
    search_product,
    quantity_update_groceries,
    display_items_by_category,
    track_expiring_soon,
)

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
