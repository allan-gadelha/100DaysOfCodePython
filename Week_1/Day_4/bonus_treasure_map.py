#The map should be read as columns A,B and C and Row as 1,2,3 for better understanding of this code
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]

map = [line1, line2, line3]

print("Hiding your treasure! X marks the spot.")

position = input("Where do you want to put the treasure? ")

#Getting first "value" of the user input and putting it in lowercase
letter = position[0].lower()
#Creating a list so i can get the index to use it later, to make it simple
abc = ["a","b","c"]
letter_index = abc.index(letter)
#Doing the same for number but there's a catch, -1 because of number 3
number_index = int(position[1]) - 1
#Numbe_Index first cause we're choosing the line first because of the method used to navigate in nested lists
map[number_index][letter_index] = "X"

print(f"{line1}\n{line2}\n{line3}")