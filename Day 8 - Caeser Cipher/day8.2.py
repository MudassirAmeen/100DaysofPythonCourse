# Day 8.2 
# Caeser Cipher

# In this day we will make a program to decrypt our text. This program will know as Caeser Cipher
list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

# Get some information from the user

user_text = input("Type your text to decode : ").lower()
user_shift = int(input("How much shift you have used : "))

# Function to decrypt text
def decode(text, shift):
    newText = ""
    # hello
    for letter in text:
        position = list.index(letter)
        newPosition = position - shift
        newLetter = list[newPosition]
        newText += newLetter
    print(f"Decoded Text is {newText}")

# Calling the function

decode(text = user_text, shift = user_shift)