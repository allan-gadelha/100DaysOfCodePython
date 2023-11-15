import os

with open("C:/Users/deimo/Desktop/100DaysOfCodePython/Week_4/Day_24/Input/Names/invited_names.txt") as file:
    names = file.readlines()

for name in names:
    print(f"Dear {name.strip()},\nYou are cordially invited to my party!\n")

with open("C:/Users/deimo/Desktop/100DaysOfCodePython/Week_4/Day_24/Input/Letters/starting_letter.txt") as file:
    text = file.read()
    for name in names:
        new_text = text.replace("[name]", f"{name.strip()}")
        with open(f"C:/Users/deimo/Desktop/100DaysOfCodePython/Week_4/Day_24/Output/ReadyToSend/{name.strip()}.txt", 'w') as output_file:
            output_file.write(new_text)