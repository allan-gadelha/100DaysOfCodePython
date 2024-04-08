import random
#Importing modules!
from hangman_art import logo, stages
from hangman_words import word_list2

while True:
    #Print LOGO
    (print(logo))

    #Variable for controlling the End of Game trough Game Over or Win Condition
    end_of_game = False

    #Variable of Lives the player has
    lives = 6

    #Randomly choose a word from the word_list and assign it to a variable called chosen_word
    chosen_word = random.choice(word_list2).lower()

    #This one so we can get the length of the chosen_word, it'll help to make the code cleaner
    word_length = len(chosen_word)

    #Debug Option
    #print(f"Solution: {chosen_word}.")

    #Creating Blanks for the players to see what's missing
    #display = []
    #for _ in range(word_length):b
    #    display += "_"

    # Create a list to store the wrong guesses
    wrong_guesses = []

    #Trying to chance the code so i can have numbers also... Ty Escudeiro <3
    display = []
    for char in chosen_word:
        if char == " ":
            display += " "
        else:
            display += "_"

    try:
        #Loop to keep runing the game till end of game
        while not end_of_game:
            #Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
            guess = input("Guess a letter: ").lower()
            
            #Check if the user's input is more than one character
            if len(guess) > 1:
                print("Please, just guess 1 number/letter.")
                continue

            #Check to see if it's a special character
            if not guess.isalnum():
                print("Please guess a letter or a number, not a special character.")
                continue

            #Check to see if it's empty
            if not guess:
                print("You didn't guess anything. Please enter a letter.")
                continue

            #If the player already guessed that letter, just a feedback
            if guess in display:
                print(f"You've already guessed {guess}")

            #Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
            #Loop through each position in the chosen_word
            for position in range(word_length):
                #Since we don't know where the letter is in the chosen_word, we loop through the word using the position index.
                letter = chosen_word[position]
                if letter == " ":
                    continue
                if letter == guess:
                    #Change the display "_" to the letter guessed in the right position
                    display[position] = letter
            
            #if in case the player choose the wrong letter, live goes -1 and if it reach 0, its game over!
            if guess not in chosen_word.lower():
                # Check if the guess is already in the list of wrong guesses
                if guess in wrong_guesses:
                    print(f"You've already guessed {guess} and it's not in the word.")
                    continue
                else:
                    wrong_guesses.append(guess)
                #Feedback for the player:
                print(f"You guessed {guess}, that's not in the word. You lose a life.")
                lives -= 1
                if lives == 0:
                    #End the game
                    end_of_game = True
                    print("You Lose!!")
                    print(f"The word was: {chosen_word}.")

            #Print the Stage / Live you're in
            print(f"{stages[lives]}")
            #join all elements in the list and turn it into a String
            print(f"{' '.join(display)}")

            #Check to see if user got all the letters right! 
            if "_" not in display:
                end_of_game = True
                print("You win.")
    
    except KeyboardInterrupt:
        print("\nGame interrupted by the user. Exiting...")
    except EOFError:
        print("\nNão foi dessa vez Escudeiro")
    except Exception as e:
        print(f"\nNão foi dessa vez Escudeiro, part.2: {e}")

    try:
        play_again = input("Do you want to play again? Type 'y' for yes, or anything else to quit: ").lower()
        if play_again != 'y':
            break
    except KeyboardInterrupt:
        print("\nGame interrupted by the user. Exiting...")
        break
    except EOFError:
        print("\nGame interrupted by the user. Exiting...")
    except Exception as e:
        print(f"\nGame interrupted by the user. Exiting... Error: {e}")