#closure is a function having access to scope of its parent function even after the parent function has finished executing
#output:
# Inner function: blue
# Outer function: blue

def parent_function(person,coins):
    


    def play_game():
        nonlocal coins
        coins -= 1
        if coins > 1:
            print(person + " has " + str(coins) + " coins left.")
        elif coins == 1:
            print(person + " has " + str(coins) + " coin left.")
        else:
            print(person + " has no coins left. Game over!")

    return play_game

tommy = parent_function("Tommy",3)
tommy()  # Tommy has 2 coins left.
tommy()  # Tommy has 1 coin left.
tommy()  # Tommy has no coins left. Game over!

dave = parent_function("Dave",5)
dave()  # Dave has 2 coins left.
dave()  # Dave has 1 coin left.
dave()  # Dave has no coins left. Game over!
# This code demonstrates how a closure can maintain access to the variables of its parent function even after the parent function has finished executing.
# The inner function `play_game` modifies the `coins` variable defined in the outer function `parent_function`, showing how closures work in Python.
# The output will show the remaining coins for each player as they play the game.
# The closure allows each player to have their own independent game state, even though they share the same function definition.
