# Day 3

#  This program will tell you that your typed year is leap year or not

# First of all get an year from the user
year = int(input("Type an year to check : "))

# This is the calculation that will decide weather the typed year is leap year or not
divideBy4 = year % 4
divideBy100 = year % 100
divideBy400 = year % 400
if divideBy4 == 0:
    if divideBy100 != 0:
        if divideBy400 != 0:
            print("This is a leap year.")
        else:
            print("This is not a leap year.")
    else:
        print("This is not a leap year.")
else:
    print("This is not a leap year.")