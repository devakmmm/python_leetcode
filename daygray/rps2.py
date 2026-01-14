"""
rps2.py - Rock, Paper, Scissors with a play-again loop.

Learning goals:
- Use a while loop for repeated play
- Keep a running score
"""

import random  # Import random for computer choice.
from enum import Enum  # Import Enum for symbolic choices.


class RPS(Enum):  # Define an enum for the game choices.
    ROCK = 1  # Represent rock as 1.
    PAPER = 2  # Represent paper as 2.
    SCISSORS = 3  # Represent scissors as 3.


CHOICES = {  # Map input strings to enum values.
    "1": RPS.ROCK,  # Map "1" to ROCK.
    "2": RPS.PAPER,  # Map "2" to PAPER.
    "3": RPS.SCISSORS,  # Map "3" to SCISSORS.
}  # End the choices mapping.


def get_choice():  # Define a function to read valid user input.
    while True:  # Loop until valid input is provided.
        raw = input("Enter 1 for Rock, 2 for Paper, 3 for Scissors: ").strip()  # Read input.
        if raw in CHOICES:  # Validate against known choices.
            return CHOICES[raw]  # Return the matching enum.
        print("Invalid choice.")  # Prompt again for invalid input.


EXAMPLE_WALKTHROUGH_GET_CHOICE = """  # Store a walkthrough for get_choice.
Example Walkthrough: get_choice
- while True:
  keeps asking until valid input is entered.
- input(...).strip():
  reads and trims user input.
- if raw in CHOICES:
  checks for "1", "2", or "3".
- return CHOICES[raw]:
  returns the matching enum member.
- print("Invalid choice."):
  runs only on invalid input.
Example usage:
- input "2" returns RPS.PAPER.
"""


def decide_winner(player, computer):  # Define the winner logic.
    if player == computer:  # Check for a tie.
        return "tie"  # Return a tie result.
    wins = {  # Define which choices beat which.
        RPS.ROCK: RPS.SCISSORS,  # Rock beats scissors.
        RPS.PAPER: RPS.ROCK,  # Paper beats rock.
        RPS.SCISSORS: RPS.PAPER,  # Scissors beats paper.
    }  # End the wins mapping.
    return "win" if wins[player] == computer else "lose"  # Decide win or lose.


EXAMPLE_WALKTHROUGH_DECIDE = """  # Store a walkthrough for decide_winner.
Example Walkthrough: decide_winner
- if player == computer:
  returns "tie" when both choices are the same.
- wins mapping:
  defines which choice beats which.
- return "win" if wins[player] == computer else "lose":
  returns "win" or "lose".
Example usage:
- decide_winner(RPS.PAPER, RPS.ROCK) returns "win".
"""


def main():  # Define the script entry point.
    score = {"win": 0, "lose": 0, "tie": 0}  # Initialize the score tracker.
    while True:  # Loop until the player chooses to stop.
        player = get_choice()  # Get the player's choice.
        computer = random.choice(list(RPS))  # Pick a random computer choice.
        result = decide_winner(player, computer)  # Determine the round result.

        print("You:", player.name, "Computer:", computer.name, "Result:", result)  # Show result.
        score[result] += 1  # Update the score for the result type.
        print("Score:", score)  # Print the updated score.

        again = input("Play again? (yes/no): ").strip().lower()  # Ask to play again.
        if again not in ("yes", "y"):  # Exit if the user does not want to continue.
            break  # Break out of the loop.

    print("Thanks for playing!")  # Print a goodbye message.
    print(NOTES.strip())  # Print notes without extra whitespace.
    print()  # Print a blank line between notes and questions.
    print(QUESTIONS.strip())  # Print questions for review.


EXAMPLE_WALKTHROUGH_MAIN = """  # Store a walkthrough for main.
Example Walkthrough: main
- score = {"win": 0, "lose": 0, "tie": 0}:
  initializes the score dictionary.
- while True:
  repeats rounds until the user quits.
- player = get_choice():
  reads the player's choice.
- computer = random.choice(list(RPS)):
  picks a random computer choice.
- result = decide_winner(...):
  computes win/lose/tie.
- score[result] += 1:
  updates the score.
- again = input(...):
  asks to play again.
- if again not in ("yes", "y"):
  breaks the loop.
- print("Thanks for playing!"):
  outputs the goodbye message.
- print(NOTES.strip()) / print(QUESTIONS.strip()):
  prints Notes and Questions blocks.
"""


NOTES = """  # Store study notes as a multiline string.
Notes:
- A loop lets you keep game state like a score.
- Lowercasing input makes comparisons simpler.
"""


QUESTIONS = """  # Store practice questions as a multiline string.
Questions:
1) How would you add input validation for yes/no?
2) How could you store a history of rounds?
3) How would you refactor this to reuse rps.py functions?
"""


if __name__ == "__main__":  # Run main only when executed directly.
    main()  # Invoke the entry point.
