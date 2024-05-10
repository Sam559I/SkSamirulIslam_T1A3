from current_stock_function import write_grocery_items
import csv

# Global variable to store grocery items
grocery_items = []


# Function to add or adjust quantities of items
def place_order():
    global grocery_items
    total_cost = 0
    print("\nPlace an Order:")
    marketplace_number = input("Enter the marketplace number to order from: ")
    marketplace_file = f"Marketplace-{marketplace_number}.csv"

   