# Day 5 

# This program will give us highest score from the given score

# First of all we will take some score from the user

score_list = input("Write some score : ").split()

# Now we can use max() and min() function to get maximum and minimum score from the score list 

print(f"Maximum score through max() function is {max(score_list)}.")
print(f"Minimum score through min() function is {min(score_list)}.")

# Now use the for loop to make it

# Make a maximum_score veriable that will take the maximum score

maximum_score = "0"
minimum_score = "100000000000000000000000000000000000000000000000000000000000000000000000000"

print(len(minimum_score))

for score in score_list:
    if score >= maximum_score:
        maximum_score = score

    if minimum_score > score:
        minimum_score = score

print(f"Maximum score through for loop is {maximum_score}")
print(f"Minimum score through for loop is {minimum_score}")