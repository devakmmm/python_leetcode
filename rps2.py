"""
rps2.py - Rock, Paper, Scissors with a play-again loop.

Learning goals:
- Use a while loop for repeated play
- Keep a running score
"""

import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


CHOICES = {
    "1": RPS.ROCK,
    "2": RPS.PAPER,
    "3": RPS.SCISSORS,
}


def get_choice():
    while True:
        raw = input("Enter 1 for Rock, 2 for Paper, 3 for Scissors: ").strip()
        if raw in CHOICES:
            return CHOICES[raw]
        print("Invalid choice.")


def decide_winner(player, computer):
    if player == computer:
        return "tie"
    wins = {
        RPS.ROCK: RPS.SCISSORS,
        RPS.PAPER: RPS.ROCK,
        RPS.SCISSORS: RPS.PAPER,
    }
    return "win" if wins[player] == computer else "lose"


def main():
    score = {"win": 0, "lose": 0, "tie": 0}
    while True:
        player = get_choice()
        computer = random.choice(list(RPS))
        result = decide_winner(player, computer)

        print("You:", player.name, "Computer:", computer.name, "Result:", result)
        score[result] += 1
        print("Score:", score)

        again = input("Play again? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            break

    print("Thanks for playing!")
    print(NOTES.strip())
    print()
    print(QUESTIONS.strip())


NOTES = """
Notes:
- A loop lets you keep game state like a score.
- Lowercasing input makes comparisons simpler.
"""


QUESTIONS = """
Questions:
1) How would you add input validation for yes/no?
2) How could you store a history of rounds?
3) How would you refactor this to reuse rps.py functions?
"""


if __name__ == "__main__":
    main()
