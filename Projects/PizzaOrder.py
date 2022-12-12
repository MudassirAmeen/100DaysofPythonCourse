# Day 3

# This program can be used for ordering pizza from pizza shop

# There are some veriables that can be used for the prices of pizza
SmallPizza = 15
MediumPizza = 20
LargePizza = 25

PepperoniForSmallPizza = 2
PepperoniForLargeAndSmallPizza = 3

ExtraCheese = 1

# Now we can take data from the user

PizzaSize = input("What size of Pizza you want? S, M or L : ")
Pepperoni = input("Do you want Pepporoni? Y or N : ")
WantsExtraCheese = input("Do you want extra cheese? Y or N : ")

# Now we can calculate the bill
bill = 0
if PizzaSize == "S" or PizzaSize == "s":
    bill = 15
    if Pepperoni =="Y" or Pepperoni =="y":
        bill += 2
    if WantsExtraCheese == "Y" or WantsExtraCheese == "y":
        bill += 1
    print(f"Your bill will be ${bill}")
if PizzaSize == "M" or PizzaSize == "m":
    bill = 20
    if Pepperoni =="Y" or Pepperoni =="y":
        bill += 3
    if WantsExtraCheese == "Y" or WantsExtraCheese == "y":
        bill += 1
    print(f"Your bill will be ${bill}")
if PizzaSize == "L" or PizzaSize == "l":
    bill = 25
    if Pepperoni =="Y" or Pepperoni =="y":
        bill += 3
    if WantsExtraCheese == "Y" or WantsExtraCheese == "y":
        bill += 1
    print(f"Your bill will be ${bill}")