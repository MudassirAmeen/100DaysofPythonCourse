# Day 4

# This program can be used in deciding the toss. 

# Importing the random module

import random

# First of all we will ask the user to select Head or Tail

userDicide = input("What is your choice? Tail or Head : ")

# Then we have to generate a random number of 1 or 2 using random module

tossWin = random.randint(0,1)

# Now we have to decide that the user won the toss or not

if userDicide == "head" or userDicide == "Head":
    if tossWin == 0:
        print("You lose the toss. There is Tail.")
    elif tossWin == 1:
        print("You win the toss.")

elif userDicide == "Tail" or userDicide == "tail":
    if tossWin == 0:
        print("You lose the toss. There is Head.")
    elif tossWin == 1:
        print("You win the toss.")

else:
    print("Please select Head or Tail.")