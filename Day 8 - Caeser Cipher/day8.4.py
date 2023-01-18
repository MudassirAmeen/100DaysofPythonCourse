# Day 8.4 
# Caeser Cipher

# This is the complete version of the program. In this function new things are repeatings the program again and again, logo and other something.

# Logo

print('''
 _______                     ___                                      ____    ____  ______    
|_   __ \                  .' ..]                                    |_   \  /   _||_   _ `.  
  | |__) |_ .--.   .--.   _| |_  .---.  .--.   .--.   .--.   _ .--.    |   \/   |    | | `. \ 
  |  ___/[ `/'`\]/ .'`\ \'-| |-'/ /__\\( (`\] ( (`\]/ .'`\ \[ `/'`\]   | |\  /| |    | |  | | 
 _| |_    | |    | \__. |  | |  | \__., `'.'.  `'.'.| \__. | | |      _| |_\/_| |_  _| |_.' / 
|_____|  [___]    '.__.'  [___]  '.__.'[\__) )[\__) )'.__.' [___]    |_____||_____||______.'  
                                                                                              
''')


list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

# Repeating the function

repeat = True
while repeat:
    # Firstly get the values from the user
    user_method = input("What did you want? Encode or Decode : ").lower()
    user_text = input("Enter your text : ").lower()
    user_shift = int(input("Enter shift you want : "))

    def caeser(text, shift, method):
        newText = ""
        if method == "decode":
            shift *= -1
        for letter in text:
            # If user give anything else of alphabet then this will not change
            if letter in list:
                position = list.index(letter)
                newPosition = position + shift
                newText += list[newPosition]
            else:
                newText += letter
        print(f"The required text is {newText}")

    caeser(text = user_text, shift = user_shift, method = user_method)

    Question = input("Do you want to Continue ? yes or not : ").lower()
    if Question == "no":
        repeat = False
        print("Good Bye. 👋")