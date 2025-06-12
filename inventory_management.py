# 5. Simple Inventory Management System
# Concepts: Dictionary for storing item name and quantity/price
# Description: Ek dukaan ka inventory banao jisme item ka naam, quantity, aur price ho. User items add/remove/update kar sake.

inventory = {
    "pen": {"price": 10, "quantity": 50},
    "notebook": {"price": 50, "quantity": 100}
}
def display_inventory():
    print("\n=====Inventory=====")
    print("1. View inventory")
    print("2. Add Item")
    print("3. Update Item")
    print("4. Remove Item")
    print("5. searchin items")
    print("6. Calculate Total Inventory Value")
    print("7. items total value")
    print("8. Show items with low stock")
    print("9. Exit")
    print("===================")
while True:
    display_inventory()
    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        print("\n=====Current Inventory=====")
        for item, details in inventory.items():
            print(f"{item.title()}: Price = {details['price']}, Quantity = {details['quantity']}")
    elif choice == '2':
        item_name = input("Enter item name: ").lower()
        price = float(input("Enter item price: "))
        quantity = int(input("Enter item quantity: "))
        inventory[item_name] = {"price": price, "quantity": quantity}
        print(f"Item '{item_name}' added to inventory.")
    elif choice == '3':
        item_name = input("Enter item name to update: ").lower()
        if item_name in inventory:
            price = float(input("Enter new price: "))
            quantity = int(input("Enter new quantity: "))
            inventory[item_name] = {"price": price, "quantity": quantity}
            print(f"Item '{item_name}' updated.")
        else:
            print("Item not found in inventory.")
    elif choice == '4':
        item_name = input("Enter item name to remove: ").lower()
        if item_name in inventory:
            del inventory[item_name]
            print(f"Item '{item_name}' removed from inventory.")
        else:
            print("Item not found in inventory.")
    elif choice == '5':
        item_name = input("Enter item name to search: ").lower()
        if item_name in inventory:
            details = inventory[item_name]
            print(f"Item '{item_name}' found: Price = {details['price']}, Quantity = {details['quantity']}")
        else:
            print("Item not found in inventory.")
    elif choice == '6':
        total_value = sum(details['price'] * details['quantity'] for details in inventory.values())
        print(f"Total inventory value: {total_value}")
    elif choice == '7':
        item_name = input("Enter item name to calculate total value: ").lower()
        if item_name in inventory:
            details = inventory[item_name]
            total_value = details['price'] * details['quantity']
            print(f"Total value for '{item_name}': {total_value}")
        else:
            print("Item not found in inventory.")
    elif choice == '8':
        low_stock_items = {item: details for item, details in inventory.items() if details['quantity'] < 20}
        if low_stock_items:
            print("\n=====Items with Low Stock=====")
            for item, details in low_stock_items.items():
                print(f"{item.title()}: Price = {details['price']}, Quantity = {details['quantity']}")
        else:
            print("No items with low stock.")
    elif choice == '9':
        print("Thank you for using the Inventory Management System.")
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
