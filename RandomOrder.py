# A simple program to print 1 to 10 in random order
import random

# Store an array with values 1 to 10
my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use random.shuffle function
random.shuffle(my_numbers)

# Print the array with random order
print(my_numbers)