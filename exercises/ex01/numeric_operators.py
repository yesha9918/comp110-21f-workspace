"""numerical operations on two inputted values."""

__author__ = "730402890"

left_hand: str = input("Left-hand side: ")
right_hand: str = input("Right-hand side: ")
left_hand_int = int(left_hand)
right_hand_int = int(right_hand)
expo = str(left_hand_int ** right_hand_int)
divide = str(left_hand_int / right_hand_int)
divide_int = str(left_hand_int // right_hand_int)
remainder = str(left_hand_int % right_hand_int)

print(left_hand + " ** " + right_hand + " is " + expo)
print(left_hand + " / " + right_hand + " is " + divide)
print(left_hand + " // " + right_hand + " is " + divide_int)
print(left_hand + " % " + right_hand + " is " + remainder)
