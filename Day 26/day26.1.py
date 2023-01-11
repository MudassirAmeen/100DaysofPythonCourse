numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

#Write your 1 line code 👇 below:

squared_numbers = [number*number for number in numbers]
even_numbers = [even for even in numbers if even%2 == 0]

#Write your code 👆 above:

print(squared_numbers)
print(even_numbers)


