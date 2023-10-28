print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

step1 = input("The adventure has already begun with choices, a fork in the road, which way will you go, left or right? ")

if step1 == "left" or step1 == "Left":
    step2 = input("\nYou found the right path, but now you've encountered a trap, a large axe is swinging in front of you, will you risk to run or will decide to wait? ")
else:
    print("\nOh no, you chose the wrong path and fell into a pit full of snakes, it's game over for you")

if step2 == "wait" or step2 == "Wait":
    step3 = input("\nA miracle happened; you decided to wait, and the axe came loose, allowing you to pass. However, now you are facing three doors: one red, one green, and one yellow. Which one will you choose? ")
else:
    print("\nYou decided to run, but unfortunately, you were too sedentary, and due to the lack of exercise, you weren't fast enough and got cut in half by the axe. Game Over!")

if step3 == "red" or step3 == "Red":
    print("\nYou entered the red door with great confidence, but the entire room started to catch fire, and within seconds, you were nothing more than a pile of ashes. Game Over!")
elif step3 == "green" or step3 == "Green":
    print("You entered the green door with great composure and found yourself in a serene forest, but the serenity didn't last long because you were attacked by wolves, and now you were nothing more than a pile of bones. Game Over!")
elif step3 == "yellow" or step3 == "Yellow":
    print("\nYou entered the yellow door, and you were almost blinded by the intense brightness emanating from it. However, as your eyes adjusted to the light, you realized that you were in a room filled with treasure, gold everywhere. Congratulations, you found the treasure, and now you are rich!")
else:
    print("\nYou took too long to choose a door, and suddenly, all of them opened at once. You were blinded by a flash of light, and when you realized it, you were being devoured ALIVE BY FLAMING WOLVES!!!! GAME OVER!")