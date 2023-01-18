# This is day 2.

# In this day we will make a tip calculator. This will get three inputs from  the user and calculate the total bill on every person.

# It will greet the user by following message

print("Welcome to Tip calculator")

# First of all it will take total bill from the user

total_bill = int(input("What was the total bill? Rs. "))

# Second it will take a tip from the user in percentage

bill_tip = int(input("How much tip would you like to give? 10, 12, 15 "))

# Third it will take number of persons that includes in this tip

total_bill_persons = int(input("How many people to split the bill? "))

# Then we have to calculate the bill with tip
bill_with_tip = bill_tip / 100 * total_bill +total_bill

# After that we can now divide the bill_with_tip by the number of persons

bill_per_person = bill_with_tip / total_bill_persons

print(f"Each person should pay Rs. {bill_per_person}")
