# Day 8

# Import math for the ceil function
import math

# This is Area Calculator. The idea is that we will give him width and height and this will give us the total numbers of cans that will be used to paint that area

# Make a function to calculate the number of cans
def areaCal(w, h, c):
    Area = w * h
    number_of_cans = Area / Coverage
    print(f"You will need {math.ceil(number_of_cans)} cans of paint.")

# Let us say that 1 can of paint can paint 5 meter square.

Coverage = 5

# Firstly get the width and height from the user

width = int(input("width of wall : "))
height = int(input("Height of wall : "))

# Now call the funtion

areaCal(w = width, h = height, c = Coverage)
