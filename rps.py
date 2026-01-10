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


def get_computer_choice():  # Define a function to pick a random choice.
    return random.choice(list(RPS))  # Return a random enum value.


def decide_winner(player, computer):  # Define the winner logic.
    if player == computer:  # Check for a tie.
        return "tie"  # Return a tie result.
    wins = {  # Define which choices beat which.
        RPS.ROCK: RPS.SCISSORS,  # Rock beats scissors.
        RPS.PAPER: RPS.ROCK,  # Paper beats rock.
        RPS.SCISSORS: RPS.PAPER,  # Scissors beats paper.
    }  # End the wins mapping.
    return "win" if wins[player] == computer else "lose"  # Decide win or lose.


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
