# Day 14

# In this day we will make a Higher Lower Game.

import random, replit
import art, people

person1 = random.choice(people.famous_people)
person2 = random.choice(people.famous_people)

person1Name = person1["name"]
person1Country = person1["country"]
person1Profession = person1["profession"]
person1Followers = person1["followers"]

person2Name = person2["name"]
person2Country = person2["country"]
person2Profession = person2["profession"]
person2Followers = person2["followers"]

score = 0

# FUnction to update the values of persons
def updateValues():
    global person1,person2
    person1 = person2
    person2 = random.choice(people.famous_people)

# Funtion to Decide win or lose
def decide(AFollwers, BFollowers, Answer):
    global score
    if Answer == "a":
        if AFollwers > BFollowers:
            score += 1
            return 1
        else:
            return 0
    elif Answer == "b":
        if AFollwers < BFollowers:
            score += 1
            return 1
        else:
            return 0
    else:
        return 3

# Play Game function
def play_game():
    print(art.higherLower)
    print(f"Your score is {score}")
    print(f"Compare A: Name {person1Name}, Profession {person1Profession}, From {person1Country}")
    print(art.vs)
    print(f"Against B: Name {person2Name}, Profession {person2Profession}, From {person2Country}")
    question = input("Who has more followers? Typr 'A' or 'B' : ").lower()
    result = decide(AFollwers = person1Followers, BFollowers = person2Followers, Answer = question)
    if result == 1:
        updateValues()
        return "You win"
    elif result == 0:
        return "You Win"
    else:
        return "Invalid Choice"

print (play_game())  
