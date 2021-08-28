"""relational operators with inputted values T/F"""

__author__ = "730402890"

left_hand: str = input("Left-hand side: ")
right_hand: str = input("Right-hand side: ")
left_hand_int = int(left_hand)
right_hand_int = int(right_hand)
less_than = str(left_hand_int < right_hand_int)
greater_equal = str(left_hand_int >= right_hand_int)
equal_to = str(left_hand_int == right_hand_int)
not_equal_to = str(left_hand_int != right_hand_int)

print(left_hand + " < " + right_hand + " is " + less_than)
print(left_hand + " >= " + right_hand + " is " + greater_equal)
print(left_hand + " == " + right_hand + " is " + equal_to)
print(left_hand + " != " + right_hand + " is " + not_equal_to)
