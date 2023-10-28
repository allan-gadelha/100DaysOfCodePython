import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer = random.randint(0,2)

if user == 0:
    print(rock)
elif user == 1:
    print(paper)
elif user == 2:
    print(scissors)

print("Computer chose:")

if computer == 0:
    print(rock)
elif computer == 1:
    print(paper)
elif computer == 2:
    print(scissors)

if user == 0:
    if computer == 0:
        print("It's a tie!")
    elif computer == 1:
        print("You lost!")
    elif computer == 2:
        print("You won!")
        
if user == 1:
    if computer == 0:
        print("You lose!")
    elif computer == 1:
        print("It's a tie!")
    elif computer == 2:
        print("You won!")

if user == 2:
    if computer == 0:
        print("You lost!")
    elif computer == 1:
        print("You won!")
    elif computer == 2:
        print("It's a tie!")