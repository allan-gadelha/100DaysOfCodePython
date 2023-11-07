from art import vs, logo
from game_data import data
import random

print(logo)

score = 0
compare_a = []
compare_b = []

def comparing():
    #Getting a random item from data
    compare_a = data[random.randint(0,49)]
    print(f"Compare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}")

    print(vs)

    #Getting a random item from data
    compare_b = data[random.randint(0,49)]
    print(f"Compare B: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}")



comparing()