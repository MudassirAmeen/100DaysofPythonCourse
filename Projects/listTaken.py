# Day 4

# This program will take some names from the user (comma Separated) and will make a list from the names

# Importing the random module

import random

# First of all it will take a list from the user

names = input("Write names by comma separated : ")

# Make a list of names by using split() function

list_of_names = names.split(", ")

# Randomly take a name from the list and display it with a message

# For this we have to use len() function to find the length of list

list_length = len(list_of_names)

# After taking a length of list, we can use randint() to randomly take a name from the list

random_name = list_of_names[random.randint(0, list_length-1)]

# We can use random.choice() function to choose a value from the list

random_name_1 = random.choice(list_of_names)

print(f"Welcome to 100 days of Python course {random_name}.")
print(f"Welcome to 100 days of Python course {random_name_1}.")

