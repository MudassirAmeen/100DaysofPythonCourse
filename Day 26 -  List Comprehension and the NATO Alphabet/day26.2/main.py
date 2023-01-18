with open("file1.txt") as file1:
    file1data = file1.readlines()
    
with open("file2.txt") as file2:
    file2data = file2.readlines()
    
result = [int(number) for number in file1data if number in file2data]
print(result)