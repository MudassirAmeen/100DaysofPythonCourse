# Day 8.1 
# Caeser Cipher

# In this day we will make a program to encode our text. This program will know as Caeser Cipher
list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

# Get some infromation from the user

user_text = input("Type your text to encode : ").lower()
user_shift = int(input("How much shift you want : "))

# Funtion to encrypt the text

def encode(text, shift):
    newText = ""
    # hello
    for letter in text:
        position = list.index(letter)
        newPosition = position + shift
        newLetter = list[newPosition]
        newText += newLetter
    print(f"Encoded Text is {newText}")

# Calling the function

encode(text = user_text, shift = user_shift)