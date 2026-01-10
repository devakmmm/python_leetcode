"""
rps.py - Rock, Paper, Scissors (single round).

Learning goals:
- Enum usage
- Input validation
- Simple game logic
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


def get_player_choice():  # Define a function to read valid user input.
    while True:  # Loop until valid input is provided.
        choice = input("Enter 1 for Rock, 2 for Paper, 3 for Scissors: ").strip()  # Read input.
        if choice in CHOICES:  # Validate against known choices.
            return CHOICES[choice]  # Return the matching enum.
        print("Invalid choice. Try again.")  # Prompt again for invalid input.


EXAMPLE_WALKTHROUGH_GET_PLAYER = """  # Store a walkthrough for get_player_choice.
Example Walkthrough: get_player_choice
- while True:
  keeps asking until valid input is entered.
- input(...).strip():
  reads and trims user input.
- if choice in CHOICES:
  checks for "1", "2", or "3".
- return CHOICES[choice]:
  returns the matching enum member.
- print("Invalid choice. Try again."):
  runs only on invalid input.
Example usage:
- input "1" returns RPS.ROCK.
"""


def get_computer_choice():  # Define a function to pick a random choice.
    return random.choice(list(RPS))  # Return a random enum value.


EXAMPLE_WALKTHROUGH_GET_COMPUTER = """  # Store a walkthrough for get_computer_choice.
Example Walkthrough: get_computer_choice
- list(RPS):
  creates a list of enum members.
- random.choice(...):
  selects one member at random.
Example usage:
- returns RPS.PAPER (random).
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
  returns "win" for a player win, otherwise "lose".
Example usage:
- decide_winner(RPS.ROCK, RPS.SCISSORS) returns "win".
- decide_winner(RPS.ROCK, RPS.PAPER) returns "lose".
"""


def main():  # Define the script entry point.
    player = get_player_choice()  # Get the player's choice.
    computer = get_computer_choice()  # Get the computer's choice.

    print("You chose:", player.name)  # Print the player's choice.
    print("Computer chose:", computer.name)  # Print the computer's choice.

    result = decide_winner(player, computer)  # Compute the result.
    if result == "tie":  # Handle a tie result.
        print("It's a tie!")  # Print the tie message.
    elif result == "win":  # Handle a player win.
        print("You win!")  # Print the win message.
    else:  # Handle a player loss.
        print("You lose!")  # Print the loss message.

    print(NOTES.strip())  # Print notes without extra whitespace.
    print()  # Print a blank line between notes and questions.
    print(QUESTIONS.strip())  # Print questions for review.


EXAMPLE_WALKTHROUGH_MAIN = """  # Store a walkthrough for main.
Example Walkthrough: main
- player = get_player_choice():
  reads and validates player input.
- computer = get_computer_choice():
  picks a random computer choice.
- print choices:
  outputs the enum names for each.
- result = decide_winner(player, computer):
  computes win/lose/tie.
- prints outcome message:
  outputs "You win!", "You lose!", or "It's a tie!".
- print(NOTES.strip()) / print(QUESTIONS.strip()):
  prints Notes and Questions blocks.
"""


NOTES = """  # Store study notes as a multiline string.
Notes:
- Enum members are comparable by identity.
- Using a dict for win rules keeps the logic compact.
"""


QUESTIONS = """  # Store practice questions as a multiline string.
Questions:
1) How would you add "Lizard" and "Spock" to the game?
2) Why use Enum instead of plain strings?
3) Where would you track a score across rounds?
"""


if __name__ == "__main__":  # Run main only when executed directly.
    main()  # Invoke the entry point.
