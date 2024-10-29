#!/usr/bin/env python3

# Data Structure(Built-in Data Structure) Basics

# Create an empty list called my_list
my_list = []

# Append the following elements to my_list: 10, 20, 30, 40.
[my_list.append(v) for v in [10, 20, 30,40]]

# Insert the value 15 at the second position in the list.
my_list.insert(1, 15)

# Extend my_list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])

# Remove the last element from my_list.
my_list.pop()

# Sort my_list in ascending order
my_list.sort()

# Find and print the index of the value 30 in my_list.
print(my_list.index(30))
