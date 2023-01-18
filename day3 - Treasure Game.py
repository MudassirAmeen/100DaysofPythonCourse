# This is day three.

# In this day we will make a treasure game

# This is a game that will give you a treasure. But for the treasure you need a password. 

print("Welcome to treasure game. ")
print("There is a box in which some money. But it has a password.")

# First of all we will ask the user if he has a password or not

user = input("If you know the password then type \"yes\" otherwise type \"No\" : ")

password = "MudassirAmeen123"

# If the user told that he has a password then he will put the password to get the money

if user == "Yes" or user == "yes":
    userPassword = input("Type your password : ")
    if userPassword == password:
        print("Congratulation! You have got the money. It will transfor to your bank in 30 days.🎂")
    else:
        print("Your password is incorrect.😢 Please try again.")

# If the user told that he has not a password then he will cross some steps to get the password.

if user == "No" or user == "no":
    print("As you have no password then win the game to get the password.")

# Level 1 to get password

    userBall = input("There are two balls. One is red and second is green. Which one you will chose. \"Red\" or \"Green\"")
    if userBall == "green" or userBall == "Green":

# Level 2 to get password

        print("You have succeessfull passed the level one.")
        print('''
        We will give you three password. Choose one to win.
        1. mudassir123Ameen
        2. MudassirAMeen123
        3. MudassirAmeen123
        ''')

        userPassword = input("Please write one password : ")
        
        if userPassword == "mudassir123Ameen" or userPassword == "MudassirAMeen123" or userPassword =="MudassirAmeen123":
            if userPassword == password:
                print("Congratulation! You have got the money. It will transfor to your bank in 30 days.🎂")
            else:
                print("You choose an incorrect password.😢 Please try again.")
        else:
            print("Your choosen password not exists in above passwords.")
    elif userBall == "Red" or userBall == "red":
        print("You have failed because this was a bomb.")
    else:
        print("Please select a ball.")