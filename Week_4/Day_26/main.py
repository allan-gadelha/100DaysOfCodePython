import pandas

nato = pandas.read_csv("Week_4/Day_26/nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
#Using this way i don't get the format that i want!
#nato_dict = {letter:code for (letter,code) in nato.items()}

#Using this way i do
nato_dict = {row.letter: row.code for (index, row) in nato.iterrows()}
print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Choose a word:").upper()

user_list = [letter for letter in user_input]

# Create a list of phonetic code words corresponding to the user's input
phonetic_list = [nato_dict[letter] for letter in user_list]

#For better visualization of the list comprehension
#phonetic_list = []
#for letter in user_list:
#    phonetic_list.append(nato_dict[letter])

# Print the list
print(phonetic_list)
