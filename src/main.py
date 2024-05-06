"""
Grocery Tracker App

This Python script implements a terminal-based grocery tracking application.
Users can display current stock, search for specific products, order groceries, track
expired perishable food items, and compare prices.

Author: 
Date:

"""

import csv
import datetime

# Global variable to store grocery items
grocery_items = []

# Function to load grocery items 
def load_grocery_items():
    global grocery_items
    grocery_items = []
    with open("src/grocery_items.csv", mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            grocery_items.append(row)

# Function to add grocery items 
def write_grocery_items():
    with open("grocery_items.csv", mode='w', newline='') as file:
        fieldnames = ["Name", "Category", "Price", "Quantity", "Expiration Date"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for item in grocery_items:
            writer.writerow(item)

# Function to display current stock
def display_current_stock():
    print("\nCurrent Stock of Grocery Items:")
    for item in grocery_items:
        print(f"{item['Name']}: {item['Quantity']} {item['Category']} - ${item['Price']}")


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
        choice = input("Enter your choice: ")
        if choice == "1":
            display_current_stock()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()