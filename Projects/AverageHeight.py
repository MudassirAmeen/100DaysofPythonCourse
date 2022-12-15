# Day 5

# This program will give average height of students based on the number of students.

# Fisrt of all it will ask students height. SO the user must enter some heights to run the program

Student_heights = input("Enter some heights of students : ").split()

# Now we have to make every item of list an integer.
for i in range(0, len(Student_heights)):
    Student_heights[i] = int(Student_heights[i])

# Now we have list of heights. So we have to use the for loop to calculate the average height

# Formula for average height be like this
# avg_height = Sum_of_all_height / total_heigts

# We can use len() and sum() function to take average of height

print(f"Average height through len() and sum() functions is {round(sum(Student_heights) / len(Student_heights), 5)}.")

# We have initiolize some veriables to use them


totalHeight = 0
totalNumberOfHeight = 0
for height in Student_heights:
    totalHeight += int(height)
    totalNumberOfHeight += 1

# Now we have to calculate the average height
ave_height = round(totalHeight / totalNumberOfHeight, 5)

print(f"Average height through only for loop is {ave_height}.")

