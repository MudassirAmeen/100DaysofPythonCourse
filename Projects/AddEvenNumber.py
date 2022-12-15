# Day 5 

# In this program we will calculate all even numbers between a range

# First of all we will ask the user to enter a range of number

Start_from = int(input("Enter starting point : "))
To_end = int(input("Enter ending point : "))+1

# Now we have starting and ending number so we can use range funtion and for loop to get total result of even numbers

total = 0
for number in range(Start_from, To_end):
    if number % 2 == 0:
        total += number
print(f"Total of all even number is {total}")
