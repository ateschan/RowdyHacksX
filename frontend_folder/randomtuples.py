import random

# Set the size of the array
size = 10000  # Adjust this number for a larger or smaller array

# Generate the array of tuples
tuples_array = [(i, random.random() * 50) for i in range(size)]

# Example: Print the first 10 tuples
print(tuples_array[:2000])
