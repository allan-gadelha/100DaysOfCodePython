import random

logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""

print(logo)

tries = 0

def ask_for_difficulty():
    """Function so there's no way the player put a invalid character"""
    difficulties = {
        "easy" : 10,
        "hard" : 5,
    }
    while True:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if difficulty in difficulties:
            return difficulties[difficulty]
        print("Invalid input. Please type 'easy' or 'hard'.")

print("Welcome to the Number Guessing Game!")

print("I'm thinking of a number between 1 and 100.")

answer = random.randint(1,100)

print(f"Psst, the correct answer is {answer}")

tries = ask_for_difficulty()

while tries > 0:
    try:
        guess = int(input("Make a guess: "))
        if guess < answer:
            tries -= 1
            print(f"Too low.\nGuess again.\nYou have {tries} attempts remaining to guess the number.")
            if tries == 0:
                print("You've run out of guesses, you lose.")
        elif guess > answer:
            tries -= 1
            print(f"Too high.\nGuess again.\nYou have {tries} attempts remaining to guess the number.")
            if tries == 0:
                print("You've run out of guesses, you lose.")
        elif guess == answer:
            print(f"You got it! The answer was {answer}.")
            break
    except ValueError:
          print("Invalid input. Please enter a number.")


