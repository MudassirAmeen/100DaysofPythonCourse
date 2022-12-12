# Day 4

# This is treasure game where you can put your own number to add your point

# First give the user a map

row1  = ["⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛"]
row2  = ["⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛"]
row3  = ["⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛"]
row4  = ["⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛"]
row5  = ["⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛"]
row6  = ["⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛"]
row7  = ["⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛"]
row8  = ["⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛"]
row9  = ["⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛"]
row10 = ["⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛","⬛"]

map = [row1, row2, row3, row4, row5, row6, row7, row8, row9, row10]

print(f"{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}\n{row9}\n{row10}")

# After showing map, we will ask the user to tell us two number and we will place there his point

place = input("Where you want to place your point? Tell us in your choice in two numbers : ")

# After taking the number we will place his point in that place
if int(place) > int("100"):
    print("Please make sure that number is two digits or equal to 100.")
else:
    if place != "100" :

        horizontal = int(place[0])

        vertical = int(place[1])

        list1 = [1,2,3,4,5,6,7,8,9,0]

        if horizontal in list1 and vertical == 0:

            horizontal = int(place[0]) - 1

        vertical = int(place[1]) - 1

        map[horizontal][vertical] = "X"

    elif place == "100":

        map[9][9] = "X"

    print(f"{row1}\n{row2}\n{row3}\n{row4}\n{row5}\n{row6}\n{row7}\n{row8}\n{row9}\n{row10}")