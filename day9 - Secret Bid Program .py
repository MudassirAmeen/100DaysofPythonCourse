# Day 9

# In this day we will biuld a Secret Bid program in which no one else can view other bid and finaly it will give us the name and bid that will win.

# Import some modules
# import clear from replit

# Logo
print('''
 _______                     ___                                      ____    ____  ______    
|_   __ \                  .' ..]                                    |_   \  /   _||_   _ `.  
  | |__) |_ .--.   .--.   _| |_  .---.  .--.   .--.   .--.   _ .--.    |   \/   |    | | `. \ 
  |  ___/[ `/'`\]/ .'`\ \'-| |-'/ /__\\( (`\] ( (`\]/ .'`\ \[ `/'`\]   | |\  /| |    | |  | | 
 _| |_    | |    | \__. |  | |  | \__., `'.'.  `'.'.| \__. | | |      _| |_\/_| |_  _| |_.' / 
|_____|  [___]    '.__.'  [___]  '.__.'[\__) )[\__) )'.__.' [___]    |_____||_____||______.'  
                                                                                              
''')

# Make a dictionary
bids = {}

# Make an empty winner list
winner = []

# Make a function that will add the name and bid to the dictionary
def bidsfunction():
    # Take user name and bid
    name = input("What is your name ? ")
    bid = int(input("What is your bid ? $"))
    # Save the name and bid in the Distionary
    bids[name] = bid

    # First time when the winner list empty then it will add the name and bid in the winner list
    if winner == []:
        winner.append(name)
        winner.append(bid)
    
    # We will check that if the new user has more bid then previous user then we will replace the winner name and bid by that user
    for key in bids:
        if bids[key] > winner[1]:
            winner[0] = name
            winner[1] = bid

    question = input("Will you want to bid again ? yes or no : ").lower()
    if question == "yes":
        bidsfunction()
            
bidsfunction()

print(f"The winner is {winner[0]}, which has maximum bid of {winner[1]}.")
