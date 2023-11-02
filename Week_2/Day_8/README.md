Today we learned about Function with Inputs, Positional vs Keyword Arguments and the project for this day is to create a Caesar Cipher! 

Doing the exercises i've noticed that i need to use booleans more we had one where we need to see if a number is a prime number or not, my code was huge, with multiple for and multiples ifs and didn't quite work at all too, and when i saw the teacher's code it was just 8 lines using boolean, and 1 for and if.

The code for future refernce!

def prime_checker(number):
  is_prime = True
  for i in range(2,number):
    if number % i == 0:
      is_prime = False
  if is_prime:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")

I did the first part of the Cesar Cipher, the encrypt part and i was surprise, it took me some time, but now i saw the solution and managed to debug on my OWN, i'm seeing finally some progress in my code.