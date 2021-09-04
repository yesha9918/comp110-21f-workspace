"""Repeating a beat in a loop."""

__author__ = "730402890"


beat: str = input("What beat do you want to repeat? ")
times: int = int(input("How many times do you want to repeat it? "))
beat_string: str = beat
counter: int = 1


while counter < times:
    beat_string = beat_string + " " + beat
    counter = counter + 1

if times <= 0:
    print("No beat...")
else:
    print(beat_string)