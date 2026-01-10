"""
rps.py - Rock, Paper, Scissors (single round).

Learning goals:
- Enum usage
- Input validation
- Simple game logic
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


def get_player_choice():
    while True:
        choice = input("Enter 1 for Rock, 2 for Paper, 3 for Scissors: ").strip()
        if choice in CHOICES:
            return CHOICES[choice]
        print("Invalid choice. Try again.")


def get_computer_choice():
    return random.choice(list(RPS))


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
    player = get_player_choice()
    computer = get_computer_choice()

    print("You chose:", player.name)
    print("Computer chose:", computer.name)

    result = decide_winner(player, computer)
    if result == "tie":
        print("It's a tie!")
    elif result == "win":
        print("You win!")
    else:
        print("You lose!")

    print(NOTES.strip())
    print()
    print(QUESTIONS.strip())


NOTES = """
Notes:
- Enum members are comparable by identity.
- Using a dict for win rules keeps the logic compact.
"""


QUESTIONS = """
Questions:
1) How would you add "Lizard" and "Spock" to the game?
2) Why use Enum instead of plain strings?
3) Where would you track a score across rounds?
"""


if __name__ == "__main__":
    main()
