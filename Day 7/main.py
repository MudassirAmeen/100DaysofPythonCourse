# Day 7

# In this day we will make a hangman game.

import stages
import random
import word
import logo

print(logo.logo)
print("Welcome to Hangame. Created by Mudassir Ameen.")
# words = ["words"]
lives = 6

random_word = random.choice(word.words).lower()

list = []
wordLenght = len(random_word)

for _ in range(wordLenght):
    list += "_"

end_game = False
while not end_game:
    user_guess = input("Guess a word : ").lower()
    print(f"Your word must be similar to that {list}")
    if user_guess in list:
        print(f"You have already enter this {user_guess}.")
        print(f"Your remaining lives are : {lives}.")
    else:
        if user_guess == "":
            print("Plese enter a word.")
        else:
            for index in range(wordLenght):
                if user_guess in random_word[index]:
                    list[index] = user_guess
            print(stages.stages[lives])
            print(list)
            if user_guess not in random_word:
                lives -= 1
                if lives <= 0:
                    print("Alas! You are lose. 😭")
                    print(f"The word was {random_word}")
                    end_game = True
            if "_" not in list:
                end_game = True
                print("Congratulation! You win. 🥇")
            print(f"Your remaining lives are : {lives}.")
