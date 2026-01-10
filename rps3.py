"""
rps3.py - Rock, Paper, Scissors with best-of match logic.

Learning goals:
- Break logic into small functions
- Use a "best of N" loop
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


def decide_winner(player, computer):  # Define the winner logic.
    if player == computer:  # Check for a tie.
        return "tie"  # Return a tie result.
    wins = {  # Define which choices beat which.
        RPS.ROCK: RPS.SCISSORS,  # Rock beats scissors.
        RPS.PAPER: RPS.ROCK,  # Paper beats rock.
        RPS.SCISSORS: RPS.PAPER,  # Scissors beats paper.
    }  # End the wins mapping.
    return "win" if wins[player] == computer else "lose"  # Decide win or lose.


def play_round():  # Define a function to play one round.
    player = get_choice()  # Get the player's choice.
    computer = random.choice(list(RPS))  # Pick a random computer choice.
    result = decide_winner(player, computer)  # Determine the round result.
    print("You:", player.name, "Computer:", computer.name, "Result:", result)  # Show result.
    return result  # Return the result to the caller.


def best_of(match_points=2):  # Define a best-of match.
    score = {"win": 0, "lose": 0}  # Track wins and losses.
    while score["win"] < match_points and score["lose"] < match_points:  # Continue match.
        result = play_round()  # Play a round and get result.
        if result != "tie":  # Ignore ties for score.
            score[result] += 1  # Increment win or lose count.
        print("Score:", score)  # Print the current score.
    return "win" if score["win"] == match_points else "lose"  # Return match result.


NOTES = """  # Store study notes as a multiline string.
Notes:
- Separating play_round and best_of keeps logic reusable.
- A "best of 3" match ends when one player reaches 2 wins.
"""


QUESTIONS = """  # Store practice questions as a multiline string.
Questions:
1) Why does best_of ignore ties?
2) How would you store the full round history?
3) What change lets the user pick best-of 5 or 7?
"""


def main():  # Define the script entry point.
    result = best_of(match_points=2)  # Play a best-of match.
    print("Match result:", result)  # Print the match outcome.
    print(NOTES.strip())  # Print notes without extra whitespace.
    print()  # Print a blank line between notes and questions.
    print(QUESTIONS.strip())  # Print questions for review.


if __name__ == "__main__":  # Run main only when executed directly.
    main()  # Invoke the entry point.
