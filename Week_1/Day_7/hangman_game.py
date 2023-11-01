import random
#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
display = []
for letter in chosen_word:
    display.append("_")

#Debugging code
#print("chosen_word: ", chosen_word)
#print(display)

#Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()

#Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
#Creating a variable for controlling the index of display
i = 0
for letter in chosen_word:
    if letter == guess:
        print("Right")
        display[i] = letter
        i += 1
    else:
        print("Wrong")
        i += 1

#Just to check the display
print(display)