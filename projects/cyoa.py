"""Buzzfeed quiz for which UNC website you are."""

__author__ = "730402890"

player: str = ""
points: int = 0
user_guess: int = 0
cc_counter: int = 0
sakai_counter: int = 0
zoom_counter: int = 0
gradescope_counter: int = 0
WIZARD: str = '\U0001F9B9'
CLOWN: str = '\U0001F921'
SKULL: str = '\U0001F480'
NERD: str = '\U0001F913'
WACK: str = '\U0001F92A'


def main() -> None:
    """Where the experience begins."""
    greet()
    print("First up is an intuition test.")
    global intuition
    user_guess = int(input("Pick a number between 1 and 10. "))
    intuition(user_guess)
    print("Choose your next move. ")
    choice = str(input("continue, restart, or exit? "))
    global points
    while choice != "exit":
        if choice == "continue":
            quiz(points)
        elif choice == "restart":
            print("Starting over...")
            restart()
            points = points - 1
        points = points + 1
        print(f"{player} has completed {points} turn(s)!")
        choice = str(input("continue, restart, or exit? "))
    if choice == "exit":
        print("Game Over.")
        print(f"{player} completed {points} turn(s)!")
        print(results())
    return


def greet() -> None:
    """Welcome message for user."""
    print("Welcome to FuzzBeed!")
    print("Determine which UNC used website you are!")
    global player
    player = str(input("What is your name? "))
    print(f"Welcome {player}!")
    return


def restart() -> None:
    """Procedure to restart the quiz."""
    global cc_counter
    global sakai_counter
    global zoom_counter
    global gradescope_counter
    global points
    global intuition
    points = 0
    cc_counter = 0
    sakai_counter = 0
    zoom_counter = 0
    gradescope_counter = 0
    print("Your progress has been reset.")
    print(f"{player} has completed {points} turns!")
    print("First up is an intuition test.")
    user_guess = int(input("Pick a number between 1 and 10. "))
    intuition(user_guess)
    return


def intuition(x: int) -> None:
    """Random guessing game."""
    global cc_counter
    from random import randint
    rng: int = randint(1, 10)
    if x == rng:
        print("Great intuition!")
        print(f"Ten points to Gryffindor! {WIZARD}")
    else:
        print("Sorry, I hate to break it to you, but you might be leaning towards ConnectCarolina...")
        cc_counter = cc_counter + 1


def quiz(x: int) -> None:
    """Quiz questions for user."""
    global cc_counter
    global sakai_counter
    global zoom_counter
    global gradescope_counter
    if x == 0:
        love = str(input("What is your love language? touch, time, gifts, words, or service "))
        if love == "touch":
            zoom_counter = zoom_counter + 1
        elif love == "time":
            cc_counter = cc_counter + 1
        elif love == "gifts":
            zoom_counter = zoom_counter + 1
        elif love == "words":
            gradescope_counter = gradescope_counter + 1
        elif love == "service":
            sakai_counter = sakai_counter + 1
    elif x == 1:
        others = str(input("How would others describe you? smart, funny, selfless, honest "))
        if others == "smart":
            sakai_counter = sakai_counter + 1
        elif others == "funny":
            cc_counter = cc_counter + 1
        elif others == "selfless":
            zoom_counter = zoom_counter + 1
        elif others == "honest":
            gradescope_counter = gradescope_counter + 1
    elif x == 2:
        island = str(input("If you were put on a deserted island, what would you bring? phone, flares, gear, food "))
        if island == "phone":
            cc_counter = cc_counter + 1
        elif island == "flares":
            sakai_counter = sakai_counter + 1
        elif island == "gear":
            gradescope_counter = gradescope_counter + 1
        elif island == "food":
            zoom_counter = zoom_counter + 1
    else:
        print("You've completed the quiz! Here are your results:")
        print(results())


def results() -> str:
    """Results from quiz."""
    if cc_counter == sakai_counter == gradescope_counter == zoom_counter == 0:
        return "results inconclusive."
    elif cc_counter > sakai_counter and cc_counter > gradescope_counter and cc_counter > zoom_counter:
        return f"Yikes... {CLOWN} you're ConnectCarolina... maybe consider upgrading your personality... or at least your user interface?"
    elif sakai_counter > cc_counter and sakai_counter > gradescope_counter and sakai_counter > zoom_counter:
        return f"Sakai! {NERD} Not bad at all! You've made some recent improvements in your life and you still get the job done! You might be causing stress on others though..."
    elif gradescope_counter > cc_counter and gradescope_counter > sakai_counter and gradescope_counter > zoom_counter:
        return f"You're GradeScope! {SKULL} You're honest and informative to those who interact with you. Sometimes people need the cold, hard truth."
    elif zoom_counter > cc_counter and zoom_counter > sakai_counter and zoom_counter > gradescope_counter:
        return f"ZOOOOOM! {WACK} You've come to the rescue! You love helping others in a time of need and always turn eyes when you walk into a room."
    else:
        return "results inconclusive... probably ConnectCarolina though.. let's be honest."
        

if __name__ == "__main__":
    main()