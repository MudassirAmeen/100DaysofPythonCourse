# Day 7.1 => Only make a list of word, take random word and check if the user entered right or wrong word
# Day 7.2 => Make a list of underscore("_") and if the user guess right word then replace the underscore by that word
# Day 7.3 => Make a loop that will run and get a word from the user untill the length of random words end
# Day 7.4 => Make stages that will decrease if the user guess wrong word
# Day 7.5 => Make the game more useful. If the user enter a word that is already used by this user then notify him.

# Import modules
import random

# In this day we will build a hangman game. This is simple game and this will get a random number from the list and ask the user to guess it.
# If he guess right then he will have 5 lives but if he guess wrong then he will lose one live.
# And that is how this game will work.

# First of all we will get a word from the list.
# For testing purpose we only give one word in the list
words = ["wordwww"]
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

lives = 6
# Chose a random word
random_word = random.choice(words).lower()

# Make a list of undrscore

list = []
wordlength = len(random_word)
for _ in range(wordlength):
    list += "_"

# Make a while loop that will run untill either user win or lose
game_end = False

while not game_end:
    print(f"You have find the word \n{list}")
    # Now we have to ask the user to guess the word one by one
    guessWord = input("Guess a word : ").lower()
    if guessWord in list:
        print(list)
        print(f"You have alreay use that word. {guessWord}")
    else:
        for position in range(wordlength):
            if guessWord == random_word[position]:
                list[position] = guessWord
        
        print(stages[lives])
        print(list)
        if guessWord not in random_word:
            lives -= 1
            if lives <= 0:
                game_end = True
                print("You lose. 😔")
        if "_" not in list:
            game_end = True
            print("You win. 😄")
        print(f"Your remaing lives is {lives}")
