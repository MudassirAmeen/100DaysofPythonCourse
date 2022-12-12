# Day 3

# This is a calculator to calculate love between you and your partener. 

# First of all get the names from the user
name1 = input("Your Name : ").lower()
name2 = input("Your Partener Name : ").lower()

# Now we have to calulate the love between them

# We have to find the "TRUE LOVE" in the both names and there count

T = name1.count("t") + name2.count("t")
R = name1.count("r") + name2.count("r")
U = name1.count("u") + name2.count("u")
E = name1.count("e") + name2.count("e")
L = name1.count("l") + name2.count("l")
O = name1.count("o") + name2.count("o")
V = name1.count("v") + name2.count("v")
E = name1.count("e") + name2.count("e")

leftNumber = str(T + R + U + E)
rightNumber = str(L + O + V + E)

totalPercentage = int(leftNumber + rightNumber)

if totalPercentage < 10 and totalPercentage > 90:
    print(f"Your score is {totalPercentage}, you go together like coke and mentos.")

if totalPercentage >= 40 and totalPercentage <= 50:
    print(f"Yout score is {totalPercentage}, you are alright together.")

else:
    print(f"Your score is {totalPercentage}.")