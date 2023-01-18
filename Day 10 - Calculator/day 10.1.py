# Day 10.1

# In this day we will build a calculator
import replit

# Firstly make function for the calculator

# Addition
def add(n1,n2):
    return n1 + n2

# Subtraction
def subtract(n1,n2):
    return n1 - n2

# Multiplication
def multiply(n1,n2):
    return n1 * n2

# Division
def divide(n1,n2):
    return round(n1 / n2, 2)

# Dictionary for calling these funtions
operations = {
    "+" : add,
    "-" : subtract,
    "/" : divide,
    "*" : multiply
}

# Ask some things from the user
def calculator():
    num1 = float(input("What's the first number? : "))
    for key in operations:
        print(key)
    condition = True
    while condition:
        operation = input("Pick an operation : ")
        num2 = float(input("What's the next number? : "))

        calculate = operations[operation]
        answer = calculate(n1 = num1, n2 = num2 )
        print(f"{num1} {operation} {num2} = {answer}")
        question = input(f"Type \"y\" to continue calculation with {answer}, or type \"n\" to exit.").lower()
        if question == "y":
            num1 = answer
        else:
            condition = False
            replit.clear()
            calculator()

calculator()