"""
Grocery Tracker App

This Python script implements a terminal-based grocery tracking application.
Users can display current stock, search for specific products, order groceries, track
expired perishable food items, and compare prices.

"""

from function import load_grocery_items,display_current_stock

# Global variable to store grocery items
grocery_items = []


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
        print("3. Order Groceries")
        print("4. Track Expired Perishable Food Items")
        print("5. Price Comparison")
        print("6. Exit")
        choice = input("Enter your choice: ")
        try:
            if choice == "1":
                display_current_stock()

            elif choice == "6":
                print("\nThank you for using the Grocery Tracker App. Goodbye!")
                break
            
        except ValueError:
            print("Invalid Value. Please try again.")
        except AttributeError:
            print("Invalid Attribute. Please try again.")

if __name__ == "__main__":
    main()