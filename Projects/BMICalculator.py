# Day 3

# This calculator will tell you that you are overwieght or normal

# First of all get the user weight and height

height = float(input("what is your height? "))
weight = float(input("What is your weight?"))

# Calculation of BMI and display a message

BMI = round(weight / height ** 2)
if BMI < 18.5:
    print(f"Your BMI is {BMI}, and you are underweight.🤦‍♂️")
elif BMI < 25: 
    print(f"Your BMI is {BMI}, and you are normal.👍")
elif BMI < 30:
    print(f"Your BMI is {BMI}, and you are overweight.🤣")
elif BMI < 35:
    print(f"Your BMI is {BMI}, and you are obase.😁")
else:
    print(f"Your BMI is {BMI}, and your are clinically obase.😂")