"""Counting letters in a string."""

__author__ = "730402890"


letter: str = input("What letter do you want to search for? ")
word: str = input("Enter a word: ")
i: int = 0
letter_counter: int = 0

while i < len(word):
    if word[i] == letter:
        letter_counter = letter_counter + 1
    i = i + 1

print("Count: " + str(letter_counter))