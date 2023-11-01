import random
#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
#This one so we can get the length of the chosen_word, it'll help to make the code cleaner
word_length = len(chosen_word)

display = []
for letter in chosen_word:
    display.append("_")

#Debugging code
#print("chosen_word: ", chosen_word)
#print(display)

#Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()

#Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
#Loop through each position in the chosen_word
for position in range(word_length):
    #Since we don't know where the letter is in the chosen_word, we loop through the word using the position index.
    letter = chosen_word[position]
    if letter == guess:
        #Chance de display "_" to the letter guessed in the right position
        display[position] = letter

#Just to check the display
print(display)