"""
rps3.py - Rock, Paper, Scissors with best-of match logic.

Learning goals:
- Break logic into small functions
- Use a "best of N" loop
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


def play_round():
    player = get_choice()
    computer = random.choice(list(RPS))
    result = decide_winner(player, computer)
    print("You:", player.name, "Computer:", computer.name, "Result:", result)
    return result


def best_of(match_points=2):
    score = {"win": 0, "lose": 0}
    while score["win"] < match_points and score["lose"] < match_points:
        result = play_round()
        if result != "tie":
            score[result] += 1
        print("Score:", score)
    return "win" if score["win"] == match_points else "lose"


NOTES = """
Notes:
- Separating play_round and best_of keeps logic reusable.
- A "best of 3" match ends when one player reaches 2 wins.
"""


QUESTIONS = """
Questions:
1) Why does best_of ignore ties?
2) How would you store the full round history?
3) What change lets the user pick best-of 5 or 7?
"""


def main():
    result = best_of(match_points=2)
    print("Match result:", result)
    print(NOTES.strip())
    print()
    print(QUESTIONS.strip())


if __name__ == "__main__":
    main()
