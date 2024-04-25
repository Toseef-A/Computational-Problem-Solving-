# Importing the memory_profiler module for profiling memory usage
from memory_profiler import profile

# Importing the deque module from the collections module
from collections import deque

# Tuple containing item IDs and item names
kit_items = (
    (1001, "plasters"),
    (1002, "scissors"),
    (1003, "anti-biotic spray"),
    (1004, "thermometer"),
    (1005, "alcohol spray"),
)

# Printing available items
print("Available items inside the kit:")
for item_id, item_name in kit_items:
    print(f"{item_id}: {item_name}")

# Queue to store orders, where each order is a tuple (order ID, count of kits)
orders_queue = deque()

# Counter to generate unique order IDs
order_id_counter = 1000

# Maximum number of kits per order
MaxKitsPerOrder = 5

# Maximum total number of kits across all orders
MaxTotalKits = 100


# Function to generate a unique order ID
def generate_order_id():
    # Access the global order_id_counter variable
    global order_id_counter
    # Increment the order_id_counter to generate a new unique order ID
    order_id_counter += 1
    # Return the newly generated unique order ID
    return order_id_counter

# Function to calculate the total number of kits across all orders
def calculate_total_kits():
    # Initialize a variable to store the total number of kits
    total_kits = 0
    # Iterate through each order in the orders_queue
    for order in orders_queue:
        # Add the number of kits in the current order to the total number of kits
        total_kits += order[1]
    # Return the total number of kits across all orders
    return total_kits

"""
create_order Function:

1. Check if the maximum total kits limit has been reached.
2. Generate a unique order ID.
3. Prompt the user to input the number of kits to add to the order.
4. Validate the input to ensure it does not exceed the maximum number of kits per order.
5. Append the order (order ID, kits count) to the deque.
6. Print a success message indicating the creation of the order.
"""

# Function to be profiled
@profile
# Function to create an order with a specified number of kits
def create_order():
    global orders_queue
    # Check if maximum total kits limit has been reached
    if calculate_total_kits() >= MaxTotalKits:
        # Print a message if the maximum total kits limit has been reached
        print("You have reached the maximum limit of 100 kits.")
        # Exit the function
        return
    
    # Generate a unique order ID
    order_id = generate_order_id()
    # Ask the user how many kits they want to add to the order
    kits_count = int(input("Enter the number of kits to add to the order (maximum 5): "))
    # Validate maximum kits per order
    if kits_count > MaxKitsPerOrder:
        # Print a message if the number of kits exceeds the maximum kits per order
        print("Maximum number of kits per order allowed is 5.")
        # Exit the function
        return
    
    # Append the order to the queue
    orders_queue.append((order_id, kits_count))
    # Print a message indicating the creation of the order
    print(f"Order ID {order_id} for {kits_count} kits created.")

"""
delete_order Function:

1. Iterate through each order in the orders queue.
2. Check if the order ID matches the specified order_id.
3. If found, remove the order from the orders queue.
4. Print a success message indicating the deletion of the order.
5. If not found, print a message indicating that the order ID does not exist.
"""

# Function to be profiled
@profile
# Function to delete an order
def delete_order(order_id):
    global orders_queue
    # Iterate through each order in the orders_queue
    for order in orders_queue:
        # Check if the order ID matches the specified order_id
        if order[0] == order_id:
            # If a match is found, remove the order from the orders_queue
            orders_queue.remove(order)
            # Print a success message indicating the deletion of the order
            print(f"Order with ID {order_id} deleted successfully.")
            # Exit the function after deleting the order
            return
    # If the specified order ID is not found in the orders_queue, print a message indicating it
    print(f"Order with ID {order_id} does not exist.")


"""
modify_order Function:

1. Iterate through each order in the orders queue.
2. Check if the order ID matches the specified order_id.
3. If found, print the current number of kits in the order.
4. Prompt the user to enter the new number of kits.
5. Validate the input to ensure it does not exceed the maximum number of kits per order.
6. Update the number of kits in the order.
7. Print a success message indicating the modification of the order.
8. If the order ID does not exist, print a message indicating it.
"""

# Function to be profiled
@profile
# Function to modify an order by changing the count of kits
def modify_order(order_id):
    global orders_queue
    # Iterate through each order in the orders_queue using enumerate to track the index
    for index, order in enumerate(orders_queue):
        # Check if the order ID matches the specified order_id
        if order[0] == order_id:
            # Print the current number of kits in the order for the specified order ID
            print(f"Current number of kits in the order for Order ID {order_id}: {order[1]}")
            # Ask the user to enter the new number of kits
            new_count = int(input("Enter the new number of kits (maximum 5): "))
            # Validate maximum kits per order
            if new_count > MaxKitsPerOrder:
                print("Maximum number of kits per order allowed is 5.")
                return
            
            # Update the number of kits in the order
            orders_queue[index] = (order_id, new_count)
            # Print a success message indicating the modification of the order
            print(f"Order ID {order_id} modified successfully.")
            # Exit the function after modifying the order
            return
    # If the specified order ID is not found in the orders_queue, print a message indicating it
    print(f"Order ID {order_id} does not exist.")

# Loop for managing orders
while True:
    # Displaying options for the user
    print("\nOptions:")
    print("1. Create new order")
    print("2. Delete order")
    print("3. Modify order")
    print("4. View order list")
    print("5. Finish and exit")

    # Asking user to input their choice
    choice = input("Enter your choice: ")

    if choice == "1":
        # Call the create_order() function to create a new order
        create_order()

    elif choice == "2":
        # ask the user to enter the order ID to delete
        order_id = int(input("Enter order ID to delete: "))
        # Call the delete_order() function to delete the specified order
        delete_order(order_id)

    elif choice == "3":
        # ask the user to enter the Order ID to modify
        order_id = int(input("Enter Order ID to modify: "))
        # Call the modify_order() function to modify the specified order
        modify_order(order_id)

    elif choice == "4":
        # Print the current order list with order ID and kits count
        print("Current order list:")
        for order_id, kits_count in orders_queue:
            print(f"Order ID: {order_id}, Kits Count: {kits_count}")

    elif choice == "5":
        # Exit the program when the user chooses to finish
        print("Thank you for using our service. Goodbye!")
        break

    else:
        # Print a message for invalid choices
        print("Invalid choice. Please select a valid option.")
