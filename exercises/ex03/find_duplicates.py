"""Finding duplicate letters in a word."""

__author__ = "730402890"

word: str = input("Enter a word: ")
other_letters: int = 0
i: int = 0
duplicate: str = "False"

while i < len(word):
    other_letters = i + 1
    while other_letters < len(word):
        if word[i] == word[other_letters]:
            duplicate = "True"
        other_letters = other_letters + 1
    i = i + 1

print("Found duplicate: " + duplicate)