# Day 5

# This is FizzBuzz game. This is one of the most popular game

# First of all we can ask from the user to start the game and end the game on his own number

star_at = int(input("Enter starting point : "))
end_at = int(input("Enter ending point : ")) + 1

# Now we will use the range() function and for loop to give the game a logic

for point in range(star_at, end_at):
    if point % 3 != 0 and point % 5 != 0:
        print(point)
    elif point % 3 == 0 and point % 5 != 0:
        print("Fizz")
    elif point % 3 != 0 and point % 5 == 0:
        print("Buzz")
    elif point % 3 == 0 and point % 5 == 0:
        print("FizzBuzz")