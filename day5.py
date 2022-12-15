# This is day 5

# We have to import some modules
import random

# In this day we will make a password generater. It will ask the user about password and will generate a random password

# First of all it will ask the user to how long password you want to have

password_charactors = int(input("How much letters you want in password : "))+1
password_symbles = int(input("How much symbles you want in password : "))+1
password_numbers = int(input("How much number you want in password : "))+1

charactors = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

symbles = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']

numbers = ["1","2","3","4","5","6","7","8","9","0"]

generated_password_charactors = ""
generated_password_symbles = ""
generated_password_numbers = ""
for charactor in range(0, password_charactors):
    generated_password_charactors += random.choice(charactors)
for symble in range(0, password_symbles):
    generated_password_symbles += random.choice(symbles)
for number in range(0, password_numbers):
    generated_password_numbers += random.choice(numbers)

generated_passowrd = generated_password_charactors + generated_password_numbers +generated_password_symbles

generated_passowrd_shuffled = ''.join(random.sample(generated_passowrd, len(generated_passowrd)))

print(generated_passowrd_shuffled)