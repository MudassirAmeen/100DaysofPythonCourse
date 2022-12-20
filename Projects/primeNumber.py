# Day 8

# This is day 8. We will build a program to find that weither this is a prime number or not.

# Make a function to find prime number

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print(f"{number} is a prime number!")
    elif not is_prime:
        print(f"{number} is not a prime number!")
    else:
        return

number = int(input("Check a number : "))
prime_checker(number=number)