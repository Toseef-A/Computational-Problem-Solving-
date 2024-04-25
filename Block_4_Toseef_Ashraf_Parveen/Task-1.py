# Importing the memory_profiler module for profiling memory usage
from memory_profiler import profile

# Dictionary containing item IDs as keys and item names as values
kitdict = {
    1001: "plasters",
    1002: "scissors",
    1003: "anti-biotic spray",
    1004: "thermometer",
    1005: "alcohol spray",
    1006: "eye wash",
    1007: "painkillers",
    1008: "antiseptic cream",
    1009: "sticky tape",
    1010: "tweezers"
}

# Printing available items
print("Available items:")
# Iterating through the kitdict dictionary to print each item ID and its corresponding item name
for item_id, item_name in kitdict.items():
    print(f"{item_id}: {item_name}")

# List to store orders, where each order is represented as a list with the order ID as the first element
orders = []

# Counter to generate unique order IDs
order_id_counter = 1000

# Maximum number of orders
MaxOrders = 20

# Function to generate a unique order ID
def generate_order_id():
    # Accessing the global variable order_id_counter to generate unique order IDs
    global order_id_counter
    # Incrementing the order_id_counter by 1 to generate a new unique order ID
    order_id_counter += 1
    # Returning the newly generated unique order ID
    return order_id_counter

"""
Create_New_Order Function:

1. Generate a unique order ID.
2. Prompt the user to input the item IDs (up to 5) to add to the order.
3. Validate the input to ensure it does not exceed the maximum number of items per order.
4. Check for duplicate items in the new order.
5. Check for duplicates with existing orders.
6. Check if all item IDs are valid.
7. Create a new order list consisting of the order ID and the item IDs.
8. Add the new order to the orders list.
9. Print a success message indicating the creation of the order.
"""

# Function to be profiled
@profile
# Function to add items to a new order
def Create_New_Order(item_ids):
    global orders
    global MaxOrders

    # Check if maximum orders limit has been reached
    if len(orders) >= MaxOrders:
        print("You have reached the maximum limit of 20 orders.")
        return

    # Generate a unique order ID
    order_id = generate_order_id()

    # Check if the number of items to be added exceeds the limit
    if len(item_ids) > 5:
        print("You can only add up to 5 items in one order.")
        return

    # Check for duplicate items in the new order
    if len(set(item_ids)) != len(item_ids):
        print("Duplicate items found in the new order. Please remove duplicates.")
        return

    # Check for duplicates with existing orders
    existing_item_ids = {item for order in orders for item in order[1:]}
    if set(item_ids) & existing_item_ids:
        print("Some items are already in another order.")
        return

    # Check if all item IDs are valid
    if not all(item_id in kitdict for item_id in item_ids):
        print("One or more item IDs are invalid.")
        return

    # Create a new order list
    new_order = [order_id] + item_ids

    # Add the new order to the orders list
    orders.append(new_order)

    # Print success message
    print(f"Added {len(item_ids)} items to your order with Order ID: {order_id}.")

"""
Remove_Order Function:

1. Iterate through each order in the orders list.
2. Check if the order ID matches the specified order_id.
3. If found, remove the order from the orders list.
4. Print a success message indicating the deletion of the order.
5. If not found, print a message indicating that the order ID does not exist.
"""

# Function to be profiled
@profile
# Function to remove an order by its ID
def Remove_Order(order_id):
    # Accessing the global variable orders to remove the specified order by its ID
    global orders
    # Iterating through each order in the orders list
    for order in orders:
        # Checking if the order ID matches the specified order_id
        if order[0] == order_id:
            # Removing the order from the orders list
            orders.remove(order)
            # Printing a success message indicating the deletion of the order
            print(f"Order ID {order_id} deleted successfully.")
            # Exiting the function after deleting the order
            return
    # If the specified order ID is not found in the orders list, print a message indicating it
    print("Order ID not found.")

"""
Modify_Order Function:

1. Iterate through each order in the orders list.
2. Check if the order ID matches the specified order_id.
3. If found, print the current items in the order.
4. Prompt the user to choose whether to add or delete an item.
5. If adding an item:
    - Check if the order already has the maximum number of items.
    - Prompt the user to input the item IDs to add.
    - Check for duplicates between the items to add and the items already in the order.
    - Add the items to the order.
6. If deleting an item:
    - Prompt the user to input the item ID to delete.
    - Remove the item from the order.
7. Print a success message indicating the modification of the order.
8. If the order ID does not exist, print a message indicating it.
"""

# Function to be profiled
@profile
# Function to modify an order
def Modify_Order(order_id):
    # Accessing the global variable orders to modify the specified order by its ID
    global orders

    # Iterating through each order in the orders list
    for order in orders:
        # Checking if the order ID matches the specified order_id
        if order[0] == order_id:
            # Printing the current items in the order for the specified order ID
            print(f"Current items in the order for Order ID {order_id}:")
            for index, item_id in enumerate(order[1:], start=1):
                print(f"{index}. Item ID: {item_id}, Item Name: {kitdict.get(item_id)}")

            # Prompting the user to choose whether to add or delete an item
            choice = input("Do you want to add or delete an item? (add/delete): ")

            # If the user chooses to add an item
            if choice.lower() == "add":

                # Checking if the order already has the maximum number of items
                if len(order) >= 6:
                    print("You can only add up to 5 items per order.")
                    return
                
                else:
                    # Asking the user to input the item IDs (comma-separated) to add to the order
                    items_to_add = input("Enter the item IDs (comma-separated) to add: ").split(",")
                    # Converting the input item IDs to integers and stripping any whitespace
                    items_to_add = [int(item_id.strip()) for item_id in items_to_add]

                    # Checking for duplicates between the items to add and the items already in the order
                    duplicates = set(items_to_add).intersection(order[1:])
                    if duplicates:
                        print(f"The following items are already in the order: {', '.join(map(str, duplicates))}")
                        return
                    
                    # Checking if adding more items would exceed the limit
                    if len(order) + len(items_to_add) > 5:
                        print("Adding these items would exceed the limit of 5 items per order.")
                        return
                    
                    # Adding the items to the order
                    order.extend(items_to_add)
                    # Printing a success message indicating that the items were added to the order
                    print("Items added to the order.")
                    return
                
            # If the user chooses to delete an item from the order
            elif choice.lower() == "delete":
                # Asking for the item ID to delete from the order
                item_to_delete = int(input("Enter the item ID to delete: "))

                # Checking if the item ID exists in the order
                if item_to_delete in order:
                    # Removing the item from the order
                    order.remove(item_to_delete)
                    print(f"Item ID {item_to_delete} deleted from Order ID {order_id}.")

                else:
                    # If the item ID is not found in the order
                    print("Item ID not found in the order. No changes made.")
                return

    # If the order ID doesn't exist
    print(f"Order ID {order_id} does not exist.")

while True:
    # Displaying options for the user
    print("\nOptions:")
    print("1. Create new order")
    print("2. Remove order")
    print("3. Modify order")
    print("4. View order list")
    print("5. Finish and exit")

    # Asking user to input their choice
    choice = input("Enter your choice: ")

    # If the user chooses to add items
    if choice == "1":
        # Asking for item IDs to add to order
        item_input = input("Enter item IDs (separated by comma) to add to order: ")
        # Splitting the input by comma and converting to list of integers
        item_ids = [int(item_id.strip()) for item_id in item_input.split(",")]
        # Call function to add items to order
        Create_New_Order(item_ids)

    # If the user chooses to remove an order
    elif choice == "2":
        # Asking for order ID to remove from order list
        order_id = int(input("Enter Order ID to remove: "))
        Remove_Order(order_id)

    # If the user chooses to modify an order
    elif choice == "3":
        # Asking for the order ID to modify
        order_id = int(input("Enter Order ID to modify: "))
        # Checking if the order ID is valid
        Modify_Order(order_id)

    # If the user chooses to view the current order
    elif choice == "4":
        print("Your current items in order:")
        for order in orders:
            print(f"Order ID: {order[0]}, item IDs: {order[1:]}")

    # If the user chooses to finish and exit
    elif choice == "5":
        print("Thank you for your order.")
        break

    # If the user inputs an invalid choice
    else:
        print("Invalid choice. Please select a valid option.")

