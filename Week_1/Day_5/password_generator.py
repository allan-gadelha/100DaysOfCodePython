import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#I need some control variable for each one of the inputs:
i_letters = 0
i_symbols = 0
i_numbers = 0

#Trying to make the password as random as possible
new_password = ""

#Getting my total number of characters
char_number = int(nr_letters + nr_symbols + nr_numbers)

#Need to iterate through the total number of characters
for i in range(0, char_number):
    #Need to randomize the choice of the character
    randomizer = random.randint(1,3)
    #Need to check if the character is a letter, symbol or number
    if randomizer == 1 and i_letters <= nr_letters:
        new_password += random.choice(letters)
        i_letters += 1
    elif randomizer == 2 and i_symbols <= nr_symbols:
        new_password += random.choice(symbols)
        i_numbers += 1
    elif randomizer == 3 and i_numbers <= nr_numbers:
        new_password += random.choice(numbers)
        i_numbers +=1

print(new_password)