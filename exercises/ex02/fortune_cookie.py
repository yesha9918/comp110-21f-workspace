"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730402890"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


rng: int = randint(1, 100)

print("Your fortune cookie says...")
if rng < 25:
    print("You will soon get very good news.")
else:
    if rng < 50:
        print("You will soon meet the love of your life.")
    else:
        if rng < 75:
            print("You will live a long and happy life")
        else:
            print("A mansion is in your future.")

print("Now, go spread positive vibes!")
