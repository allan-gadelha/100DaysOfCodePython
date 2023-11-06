############DEBUGGING#####################

# Describe Problem
#Range only goes from 1 - 19, so to fix it just need to increase the range so 20 gets in.
#def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
#my_function()

# Reproduce the Bug
#Randint goes from initial number till final number, final number is inclusive, so in this case the dice 1 and dice 6 will never be printed out.
#from random import randint, just need to chance to (0,5)
#dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
#dice_num = randint(0, 5)
#print(dice_imgs[dice_num])

# Play Computer
#1994 gets no return and neither -=1980
#year = int(input("What's your year of birth?"))
#if year >= 1980 and year < 1994:
#   print("You are a millenial.")
#elif year >= 1994:
#   print("You are a Gen Z.")

# Fix the Errors
#Input  gets in as a Str, need the int() to chance it
#age = int(input("How old are you?"))
#if age > 18:
# print("You can drive at age {age}.")

# #Print is Your Friend
#Doulble == in word_per_page, just need to delete 1 of it
#pages = 0
#word_per_page = 0
#pages = int(input("Number of pages: "))
#word_per_page = int(input("Number of words per page: "))
#total_words = pages * word_per_page
#print(total_words)

#Use a Debugger
#The append was outside the for loop, so it was just getting the last result, that was 13*2, insted of everything
#the fix was to put append inside the for loop
#def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)
#   print(b_list)

#mutate([1,2,3,5,8,13])