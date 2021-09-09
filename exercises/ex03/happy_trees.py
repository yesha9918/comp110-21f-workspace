"""Drawing forests in a loop."""

__author__ = "730402890"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

depth: int = int(input("Depth: "))
tree_string: str = TREE
counter: int = 0


while counter < depth and depth > 0:
    print(tree_string)
    tree_string = tree_string + TREE
    counter = counter + 1
