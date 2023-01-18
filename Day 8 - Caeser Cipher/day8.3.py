# Day 8.3 
# Caeser Cipher

# In this day we will make our Caeser Cipher. We will combine the encoding and decoding funtions in one function

# Now without something else start our code

list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

# Firstly get the values from the user

repeat = True
while repeat:
    user_method = input("What did you want? Encode or Decode : ").lower()
    user_text = input("Enter your text : ").lower()
    user_shift = int(input("Enter shift you want : "))

    def caeser(text, shift, method):
        newText = ""
        for letter in text:
            position = list.index(letter)
            if method == "encode":
                newPosition = position + shift
            elif method == "decode":
                newPosition = position - shift
            else:
                print("You have selected wrong method")
            newText += list[newPosition]
        print(f"The required text is {newText}")
        
    caeser(text = user_text, shift = user_shift, method = user_method)
    Question = input("Do you want to Continue ? yes or not : ").lower()
    if Question == "no":
        repeat = False