In this day we learned about Random Module, IndexError and Nested Lists!

I've put a bonus file on this day because of a exercise before the project of day 4, i had a lot of trouble trying to figure a method.

I could've brute force it using a lot of IF's i've done like that, but i really didn't liked the code was use and boring, so for the first time i watched the teaches videos before "finishing" the exercise and the method was amazing.

It used position[] to get the "A","B" or "C", put it in lower cause so there's no problem if the user put A or a, creating a new list so we could use .index later and also the -1 on the number index, this exercise was really eye opener.

The Project os this day is a Rock, Paper and Scissors game! 

I made it, it was kind of simply, and i was happy with how fast i've made it, but after seeing the code from the teacher i saw how i'm still not using everything that i've learned till now. I'm still just using lots of ifs and elifs and not using nested. There's so much to pack from this code, the list for the "imgs" the if including only the optimal results i need to start seeing the problem from afar, so i could simplify the solution, instead of trying to code every possibility, it was a good learning experience, i'm hoping that i'll aplly it on the nexts days.


The code from the teacher:

game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice >= 3 or user_choice < 0: 
 print("You typed an invalid number, you lose!")
else:
 print(game_images[user_choice])

 computer_choice = random.randint(0, 2)
 print("Computer chose:")
 print(game_images[computer_choice])

 if user_choice == 0 and computer_choice == 2:
     print("You win!")
 elif computer_choice == 0 and user_choice == 2:
     print("You lose")
 elif computer_choice > user_choice:
     print("You lose")
 elif user_choice > computer_choice:
     print("You win!")
 elif computer_choice == user_choice:
     print("It's a draw")


I've found some other solutions that i thought it was really clever.

pics = [rock, paper, scissors]
 
your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if your_choice < 0 or your_choice > 2 :
  print("Don\'t enter numbers out of scope!'")
  exit()
 
print(pics[your_choice])
 
comp_choice = random.randint(0,2)
print(f"Computer chose:\n{pics[comp_choice]}")
 
choice_matrix = [ ["It\'s a draw", "You lose", "You win"], ["You win", "It\'s a draw", "You lose"], ["You lose", "You win", "It\'s a draw"] ]

In this one using nested list, you just need to see every possibility and write the outcome, 0-0, 0-1, 0-2, a clever way to do it, simple for this case, but i guess when there's mores possiblity it would become more complicated doing that way.