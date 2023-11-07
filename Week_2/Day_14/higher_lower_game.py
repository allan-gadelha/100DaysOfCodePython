#From art file importing the variables vs and logo
from art import vs, logo
#From game_data file importanting data variable
from game_data import data
#Importing random function
import random

#Printing Logo
print(logo)

#Setting initial variables
score = 0
compare_a = []
compare_b = []
continue_game = True

#Function to check for a valid input, keeps happening till the users put the valid input that i want and then return that input!
def check_input():
    """Function to check for a valid input from player"""
    while True:
        answer = input(f"Who has more followers? Type 'A' or 'B': ").lower()
        if answer in ['a', 'b']:
            return answer
        print("Invalid input. Please type 'A' or 'B'.")

#Getting the first random data so we can compare later
compare_a = data[random.randint(0,49)]

#While loop to keep the game running till continue_game turns False, when the player gets the compare wrong!
while continue_game:
    
    #So the player can see which is compare_a
    print(f"Compare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}")
    #print(f"Psst A has {compare_a['follower_count']}")

    print(vs)

    #Creating compare_b and printing so the player can see
    compare_b = data[random.randint(0,49)]
    print(f"Compare B: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}")
    #print(f"Psst B has {compare_b['follower_count']}")

    #Getting the user input, thanks to the function, it'll only be a valid input, since i made sure of that in the function
    answer = check_input()

    #In case we get the same compare in both variables, it'll keep running till compare b is different, i've made a while loop
    #because there's still a little chance to get the same one 2 times in a row, that's just how probability works
    while compare_a == compare_b:
        compare_b = data[random.randint(0,49)]


    #Creating a dictionary to save the possible outcomes, at first i've creating a big if, but i've decided to test it out with dictionaries,
    #just to make the code more conscise, but it gets hard to read, since we only got 2 variables it was not necessary, but i've done that way
    #cause i want to practice using dictionaries more!
    answers = {
        'a': compare_a['follower_count'] > compare_b['follower_count'],
        'b': compare_b['follower_count'] > compare_a['follower_count']
    }

    #This get the value from the answers dictionary, the False part was in case the user didn't put a valid input, but i've already made sure that
    #the input will only be a valid one, i've decided to keep it here so my future self can use it in the future in any other project!
    if answers.get(answer, False):
        score += 1
        if answer == 'b':
            compare_a = compare_b
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        continue_game = False
