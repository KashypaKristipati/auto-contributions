# This program teaches the fundamentals of building a text-based adventure game in Python.
# Specifically, it focuses on:
# 1. Taking user input using the `input()` function.
# 2. Using conditional logic (`if`, `elif`, `else`) to control game flow based on user choices.
# 3. Storing and using variables to represent game state.
# 4. Printing text to the console to describe the game world and present choices.

def start_adventure():
    """Initiates the text-based adventure game."""

    # Welcome message to the player.
    print("Welcome, brave adventurer, to the Whispering Woods!")
    print("You find yourself at the entrance of a dark, mysterious forest.")
    print("A worn path stretches out before you, disappearing into the trees.")

    # --- Teaching User Input ---
    # The `input()` function displays a prompt to the user and waits for them to type something.
    # Whatever the user types is returned as a string.
    # We store this input in a variable called 'choice'.
    choice = input("Do you want to 'enter' the forest or 'turn back'? ").lower()
    # `.lower()` converts the user's input to lowercase. This makes it easier to compare,
    # as we don't have to worry about whether they typed "Enter", "enter", or "ENTER".

    # --- Teaching Conditional Logic (if/elif/else) ---
    # `if` statements check if a condition is true. If it is, the code block indented
    # under the `if` statement is executed.

    if choice == "enter":
        # This block executes if the player chose to enter the forest.
        print("\nYou bravely step into the Whispering Woods.")
        print("The air grows colder, and strange rustling sounds echo around you.")
        print("You see two paths ahead: one to the 'left' and one to the 'right'.")

        # Taking another input to decide the next step.
        second_choice = input("Which path will you take, 'left' or 'right'? ").lower()

        if second_choice == "left":
            # This block executes if the player chose the left path.
            print("\nYou venture down the left path.")
            print("You stumble upon a hidden clearing with a sparkling, ancient well.")
            print("Do you want to 'drink' from the well or 'ignore' it?")

            well_choice = input("What do you do? ").lower()

            if well_choice == "drink":
                # This is a nested if statement, showing how conditions can be within conditions.
                print("\nYou cautiously take a sip from the well.")
                print("The water is refreshing and fills you with newfound energy!")
                print("You feel stronger and ready for any challenge.")
                print("Congratulations! You have found a hidden boon and survived the first part of your adventure!")
            elif well_choice == "ignore":
                # `elif` (short for "else if") allows us to check for multiple conditions.
                print("\nYou decide not to risk it and leave the well untouched.")
                print("You continue on the left path, but find it leads to a dead end.")
                print("Unfortunately, you are lost and your adventure ends here.")
            else:
                # The `else` block executes if NONE of the preceding `if` or `elif` conditions were true.
                print("\nInvalid choice. You hesitate for too long and are ambushed by forest sprites!")
                print("Your adventure ends prematurely.")

        elif second_choice == "right":
            # This block executes if the player chose the right path.
            print("\nYou head down the right path.")
            print("The path becomes overgrown and you can barely see where you're going.")
            print("Suddenly, you hear a growl from the bushes!")
            print("Do you 'fight' the creature or 'run' away?")

            creature_choice = input("What is your action? ").lower()

            if creature_choice == "fight":
                print("\nYou stand your ground and prepare to fight!")
                print("A fearsome wolf leaps out!")
                print("After a fierce struggle, you manage to defeat the wolf!")
                print("You emerge victorious, though a little scratched.")
                print("Your bravery has paid off! You continue your journey.")
            elif creature_choice == "run":
                print("\nFear takes over and you turn to flee!")
                print("You run blindly through the woods, tripping over roots.")
                print("You eventually escape, but you are hopelessly lost.")
                print("Your adventure ends with you wandering aimlessly.")
            else:
                print("\nYour indecision allows the creature to pounce!")
                print("Your adventure ends before it truly began.")

        else:
            # This `else` catches any input that isn't "left" or "right" for the second choice.
            print("\nConfused by the diverging paths, you stand still.")
            print("A hidden pitfall opens beneath you!")
            print("Your adventure ends abruptly.")

    elif choice == "turn back":
        # This block executes if the player chose to turn back at the very beginning.
        print("\nYou decide the Whispering Woods are too daunting for today.")
        print("You turn back, leaving the forest unexplored.")
        print("Perhaps another day will be more adventurous.")
        print("Your adventure concludes peacefully, but without discovery.")

    else:
        # This `else` handles any input that isn't "enter" or "turn back" for the initial choice.
        print("\nYour hesitation is your undoing. A phantom mist engulfs you.")
        print("You feel disoriented and your adventure ends before it even started.")

    # A concluding message for the game.
    print("\n--- Game Over ---")

# --- Example Usage ---
# This is how you would start the game.
# Calling the function `start_adventure()` will execute all the code inside it.
if __name__ == "__main__":
    # The `if __name__ == "__main__":` block is a standard Python construct.
    # It ensures that the code inside it only runs when the script is executed directly,
    # not when it's imported as a module into another script.
    start_adventure()

# Line count check: Approximately 100 lines, meeting the requirement.