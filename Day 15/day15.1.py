# Day 15
# In this day we will build coffee machine

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0


def is_resource_sufficient(order_ingredients):
    """Returns true if the order can be made. Else false if the order cannot be made."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Return the total from coins inserted."""
    total = 0
    print("Please insert coins")
    total += int(input("How many quarter? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nikals? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.05
    return total


def is_transection_successfull(money_recieved, cost_on_drink):
    """Rturns True when the payment is accepted, or False if money is insufficent"""
    if money_recieved >= cost_on_drink:
        change = round(money_recieved - cost_on_drink,2)
        print(f"Here is ${change} in change.")
        global profit
        profit += cost_on_drink
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingridents):
    """Deduct the requiered ingridents from the resources."""
    for item in order_ingridents:
        resources[item] -= order_ingridents[item]
    print(f"Here is your {drink_name} ☕")
is_on = True

while is_on:
    choice = input(
        "What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_on = False
    if choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transection_successfull(payment, drink['cost']):
                make_coffee(choice, drink["ingredients"]) 