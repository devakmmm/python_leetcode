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
- input "3" returns RPS.SCISSORS.
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
- decide_winner(RPS.SCISSORS, RPS.PAPER) returns "win".
"""


def play_round():  # Define a function to play one round.
    player = get_choice()  # Get the player's choice.
    computer = random.choice(list(RPS))  # Pick a random computer choice.
    result = decide_winner(player, computer)  # Determine the round result.
    print("You:", player.name, "Computer:", computer.name, "Result:", result)  # Show result.
    return result  # Return the result to the caller.


EXAMPLE_WALKTHROUGH_PLAY_ROUND = """  # Store a walkthrough for play_round.
Example Walkthrough: play_round
- player = get_choice():
  reads the player's choice.
- computer = random.choice(list(RPS)):
  picks a random computer choice.
- result = decide_winner(player, computer):
  computes win/lose/tie.
- print(...):
  prints the round result.
- return result:
  returns the result string.
"""


def best_of(match_points=2):  # Define a best-of match.
    score = {"win": 0, "lose": 0}  # Track wins and losses.
    while score["win"] < match_points and score["lose"] < match_points:  # Continue match.
        result = play_round()  # Play a round and get result.
        if result != "tie":  # Ignore ties for score.
            score[result] += 1  # Increment win or lose count.
        print("Score:", score)  # Print the current score.
    return "win" if score["win"] == match_points else "lose"  # Return match result.


EXAMPLE_WALKTHROUGH_BEST_OF = """  # Store a walkthrough for best_of.
Example Walkthrough: best_of
- score = {"win": 0, "lose": 0}:
  initializes match score.
- while score["win"] < match_points and score["lose"] < match_points:
  continues until someone reaches match_points.
- result = play_round():
  plays one round and gets the result.
- if result != "tie":
  ignores ties in the score.
- score[result] += 1:
  increments win or lose.
- return "win" if score["win"] == match_points else "lose":
  returns the match outcome.
"""


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


EXAMPLE_WALKTHROUGH_MAIN = """  # Store a walkthrough for main.
Example Walkthrough: main
- result = best_of(match_points=2):
  plays a best-of-3 match (first to 2 wins).
- print("Match result:", result):
  outputs "Match result: win" or "Match result: lose".
- print(NOTES.strip()) / print(QUESTIONS.strip()):
  prints Notes and Questions blocks.
"""


if __name__ == "__main__":  # Run main only when executed directly.
    main()  # Invoke the entry point.
