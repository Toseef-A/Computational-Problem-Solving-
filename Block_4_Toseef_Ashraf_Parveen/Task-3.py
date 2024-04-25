import matplotlib.pyplot as plt
 
# Memory usage data for Task 1 code
memory_usage_T1 = [
    49.5,  # Average memory usage after creating a new order
    49.6,  # Average memory usage after removing an order
    49.55  # Average memory usage after modifying an order
]

# Line numbers corresponding to memory usage measurements
line_numbers_T1 = [
    57, 
    112, 
    150
]
 
# Memory usage data for the second code snippet
memory_usage_T2 = [
    49.2,  # Average memory usage after creating a new order
    49.3,  # Average memory usage after removing an order
    49.3   # Average memory usage after modifying an order
]
 
# Line numbers corresponding to memory usage measurements
line_numbers_T2 = [
    66, 
    104, 
    136
]
 
# Plotting the memory usage for both snippets
plt.figure(figsize=(10, 6))
 
# Plotting memory usage for the first code snippet
plt.plot(line_numbers_T1, memory_usage_T1, marker='o', linestyle='-', color='skyblue', label='Task 1')
 
# Plotting memory usage for the second code snippet
plt.plot(line_numbers_T2, memory_usage_T2, marker='o', linestyle='-', color='orange', label='Task 2')
 
# Adding labels and legend
plt.title('Comparison of Memory Usage Over Time')
plt.xlabel('Line Number')
plt.ylabel('Average Memory Usage (MiB)')
plt.grid(True)
plt.legend()
 
# Showing the plot
plt.tight_layout()
plt.show()