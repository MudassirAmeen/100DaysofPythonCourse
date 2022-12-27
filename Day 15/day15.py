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
    "water": 500,
    "milk": 500,
    "coffee": 200,
    "money": 0
}

water = resources["water"]
coffee = resources["coffee"]
milk = resources["milk"]
money = resources["money"]

repeat = True


def ask_user():
    global repeat
    user_answer = input(
        "What would you like? (espresso/latte/cappuccino): ").lower()
    if user_answer == "espresso":
        return "espresso"
    elif user_answer == "cappuccino":
        return "cappuccino"
    elif user_answer == "latte":
        return "latte"
    elif user_answer == "report":
        return "report"
    elif user_answer == "off":
        return "off"
    else:
        return "Invalid choice"


def check_resources(Water, Milk, Coffee, answers):
    if answers == "espresso":
        if Water < 50 and Coffee < 18:
            return "resources"
        elif Water < 50:
            return "water"
        elif Coffee < 18:
            return "Coffee"
        else:
            return 1
    elif answer == "latte" or answer == "cappuccino":
        if Water < 200 and Coffee < 100 and Milk < 24:
            return "resources"
        elif Water <= 0:
            return "water"
        elif Coffee <= 0:
            return "Coffee"
        elif Milk <= 0:
            return "milk"
        else:
            return 1
    else:
        return 0


def make_coffee(answer):
    global water, coffee, money, milk, repeat

    if answer == "report":
        report = f"Water : {water}ml\nMilk : {milk}ml\nCoffee : {coffee}g\nMoney : ${money}"
        return print(report)
    elif answer == "off":
        repeat = False
        return repeat

    total = 0
    total += int(input("How many quarter? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nikals? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.05
    check = check_resources(Water=water, Coffee=coffee,
                            Milk=milk, answers=answer)
    if check == 1:
        if answer == "espresso":
            if total >= 1.5:
                water -= 50
                coffee -= 18
                money += 1.5
                remaining_money = ""
                if total > 1.5:
                    remaining_money = total - 1.5
                print(f"Here is your ☕ espresso refund ${round(remaining_money, 1)}.")
            else:
                print(
                    f"You don't have sufficent money. Refund ${round(total, 1)}")
        elif answer == "latte":
            if total >= 2.5:
                water -= 200
                coffee -= 24
                milk -= 150
                money += 2.5
                remaining_money = ""
                if total > 2.5:
                    remaining_money = total - 2.5
                print(
                    f"Here is your ☕ latte refund ${round(remaining_money, 1)}.")
            else:
                print(
                    f"You don't have sufficent money. Refund ${round(total, 1)}")
        elif answer == "cappuccino":
            if total >= 3.0:
                water -= 250
                milk -= 100
                coffee -= 24
                money += 3.0
                remaining_money = ""
                if total > 3.0:
                    remaining_money = total - 3.0
                print(
                    f"Here is your cappuccino ☕ refund ${round(remaining_money, 1)}.")
            else:
                print(
                    f"You don't have sufficent money. Refund ${round(total, 1)}")
    elif check == 0:
        print("Invalid Choice")
    else:
        print(f"Sorry there is not enough {check}")


while repeat:
    answer = ask_user()
    make_coffee(answer=answer)
