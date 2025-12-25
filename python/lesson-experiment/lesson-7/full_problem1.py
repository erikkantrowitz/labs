# Inventory Management System
#
# Objective:
# Build a simple inventory management system using lists and tuples to track items in a store.
#
# Requirements:
# - Use a list to store inventory items, where each item is a tuple: (name, quantity, price)
# - Implement functions: add_item(name, qty, price), remove_item(name), update_quantity(name, new_qty), get_total_value()
# - Use loops to iterate through the inventory for calculations
# - Use conditionals to check if items exist
# - The program should run as a command-line interface (CLI) with a menu for user interaction
# - Menu options: Add item, Remove item, Update quantity, View inventory, Get total value, Exit
# - Use input() to get user choices and data
# - Display inventory and results in a user-friendly format
# - Handle invalid inputs gracefully
#
# Hints:
# - Tuples are immutable, so use them for item data
# - Lists are mutable, perfect for the inventory collection
# - Use a while loop for the main menu
#
# Bonus:
# - Add search functionality to find items by name or price range
# - Implement sorting by price or quantity

class Inventory:
    def __init__(self):
        pass
        
    inventory_items = []

    def add_item(self, name, qty, price):
        self.inventory_items.append(name,qty, price)