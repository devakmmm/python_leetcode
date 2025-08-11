import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1 #constant variable always caps, these variables never change   
    PAPER = 2
    SCISSORS = 3

print(RPS(2))  # Accessing enum by value
print(RPS.PAPER)  # Accessing enum by name
print(RPS.PAPER.name)  # Getting the name of the enum member
print(RPS.PAPER.value)  # Getting the value of the enum member

print('')
print("Welcome to Rock, Paper, Scissors!")
print("You will play against the computer.")
print("Enter 1 for Rock, 2 for Paper, or 3 for Scissors.")
print("Let's see who wins!")
print("You can also enter 'exit' to quit the game.")
print("Good luck!")
print("")

print('')

playerchoice = input("Enter ...\n1 for Rock\n2 for Paper\n3 for Scissors\n\n")
player=int(playerchoice)
# if playerchoice == '1':
#     print("You chose Rock.")
# elif playerchoice == '2':
#     print("You chose Paper.")
# elif playerchoice == '3':
#     print("You chose Scissors.")
# else:
#     print("Invalid choice. Please enter 1, 2, or 3.")
# print('')

if player < 1 or player > 3:
    sys.exit("Invalid choice. Please enter 1, 2, or 3.")

computerchoice = random.choice("123")
# computerchoice = random.randint(1, 3)
computer=int(computerchoice)

print('')
print("You chose:" , playerchoice)
print("Computer chose:", computerchoice)

if player == 1 and computer == 2:
    print("You lose! Paper covers Rock.")
elif player == 1 and computer == 3:
    print("You win! Rock crushes Scissors.")
elif player == 2 and computer == 1:
    print("You win! Paper covers Rock.")
elif player == 2 and computer == 3:
    print("You lose! Scissors cut Paper.")
elif player == 3 and computer == 1:
    print("You lose! Rock crushes Scissors.")
elif player == 3 and computer == 2:
    print("You win! Scissors cut Paper.")
else:
    print("It's a tie!")
