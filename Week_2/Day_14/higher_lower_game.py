from art import vs, logo
from game_data import data
import random

print(logo)

score = 0
compare_a = []
compare_b = []
continue_game = True

def check_input():
    """Function to check for a valid input from player"""
    while True:
        answer = input(f"Who has more followers? Type 'A' or 'B': ").lower()
        if answer in ['a', 'b']:
            return answer
        print("Invalid input. Please type 'A' or 'B'.")


compare_a = data[random.randint(0,49)]

while continue_game:
    print(f"Compare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}")
    print(f"Psst A has {compare_a['follower_count']}")

    print(vs)

    compare_b = data[random.randint(0,49)]
    print(f"Compare B: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}")
    print(f"Psst B has {compare_b['follower_count']}")

    answer = check_input()

    while compare_a == compare_b:
        compare_b = data[random.randint(0,49)]

    if answer == 'a':
        if compare_a['follower_count'] > compare_b['follower_count']:
            score += 1
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            continue_game = False

    if answer == 'b':
        if compare_b['follower_count'] > compare_a['follower_count']:
            score += 1
            compare_a = compare_b
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            continue_game = False
