"""
Grocery Tracker App

This Python script implements a terminal-based grocery tracking application.
Users can display current stock, search for specific products, order groceries, track
expired perishable food items, and compare prices.

"""

from function import (
    load_grocery_items,
    display_current_stock,
    search_product,
    quantity_update_groceries,
)

# Global variable to store grocery items


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
        print("3. Update current Stock")
        print("4. Track Expired Perishable Food Items")
        print("5. Price Comparison")
        print("6. Exit")
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
            elif choice == 6:
                print("╔══════════════════════════════════════════════════════════════════════════╗")
                print("║                       Thank you for using the Grocery                    ║")
                print("║                                Tracker App!                              ║")
                print("╚══════════════════════════════════════════════════════════════════════════╝")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid Value. Please enter a number.")


if __name__ == "__main__":
    main()
