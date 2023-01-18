# Day 14

# Now we will make a complete game of higher and lower

# First import something that we will need
from art import higherLower, vs
from people import famous_people
import random,replit

# For formating the data in printable form we need a function
def format_data(person):
    """For the format of data in printable data"""
    personName = person["name"]
    personCountry = person["country"]
    personProfession = person["profession"]
    return f"Name: {personName}, Profession: {personProfession}, From {personCountry}"

# Funtion to check the user answer
def check_answer(Guess, person_Afollowers, person_Bfollowers):
    """This funtion will check that either user has correct answer or not"""
    # # There are two ways for the checking of correct answer
    # # Way 1
    # if Guess == "a":
    #     if person_Afollowers > person_Bfollowers:
    #         return True
    #     else:
    #         return False
    # if Guess == "b":
    #     if person_Bfollowers > person_Afollowers:
    #         return True
    #     else:
    #         return False
    # # Way 2
    if person_Afollowers > person_Bfollowers:
        return Guess == "a"
    else:
        return Guess == "b"

# Display Art
print(higherLower)

score = 0
is_game_over = True
person_B = random.choice(famous_people)

while is_game_over:
    # Generate random Person from the People module
    person_A = person_B
    person_B = random.choice(famous_people)

    # If the generated person is equal to second person then we have to generate the person_B again
    if person_A == person_B:
        person_B = random.choice(famous_people)

    # We have to display our persons
    print(f"Compare A: {format_data(person_A)}")
    print(vs)
    print(f"Against B: {format_data(person_B)}")

    # Ask from the user to guess
    guess = input("Who has more followers? Typr 'A' or 'B' : ").lower()

    # Check that if the user has correct answer or not
    ## We need followers for that so
    person_A_Followers = person_A["followers"]
    person_B_Followers = person_B["followers"]
    is_correct = check_answer(Guess = guess, person_Afollowers = person_A_Followers, person_Bfollowers = person_B_Followers)

    # Clear the screen after user answer
    replit.clear()
    print(higherLower)    
    # We need to give the user a feedback on the basis of his answer
    if is_correct:
        # If the user is right then socre will increament by 1
        score += 1
        print(f"You are right. Current score is {score}")
    else:
        is_game_over = False
        print(f"Sorry, that's wrong. Final score is {score}")
