"""
closure.py - Closures in Python.

Learning goals:
- A closure remembers variables from its enclosing scope
- Use nonlocal to mutate enclosed variables
"""


def show_section(title):  # Define a helper to label output sections.
    print("\n" + title)  # Print a blank line and the section title.
    print("-" * len(title))  # Print a dashed underline under the title.


def game_factory(person, coins):  # Define a factory that creates a game closure.
    def play_game():  # Define the inner function that uses outer variables.
        nonlocal coins  # Declare that we want to modify the outer coins.
        coins -= 1  # Decrement the coin count each play.
        if coins > 1:  # Check for plural coins.
            print(person + " has " + str(coins) + " coins left.")  # Print plural message.
        elif coins == 1:  # Check for a single coin.
            print(person + " has " + str(coins) + " coin left.")  # Print singular message.
        else:  # Handle zero or negative coins.
            print(person + " has no coins left. Game over!")  # Print game over message.

    return play_game  # Return the inner function as a closure.


EXAMPLE_WALKTHROUGH_GAME_FACTORY = """  # Store a walkthrough for game_factory.
Example Walkthrough: game_factory
- def play_game():
  defines the inner function but does not run it yet.
- nonlocal coins:
  allows play_game to change the coins variable from the outer scope.
- coins -= 1:
  decreases coins by 1 each time play_game runs.
- if coins > 1:
  chooses the plural message path when coins is 2 or more.
- print(person + " has " + str(coins) + " coins left."):
  example output: Tommy has 2 coins left.
- elif coins == 1:
  chooses the singular message path when coins is 1.
- print(person + " has " + str(coins) + " coin left."):
  example output: Tommy has 1 coin left.
- else:
  runs when coins is 0 or less.
- print(person + " has no coins left. Game over!"):
  example output: Tommy has no coins left. Game over!
- return play_game:
  returns the inner function as a closure.
Example usage:
- tommy = game_factory("Tommy", 3) returns a function that remembers coins=3.
- tommy() prints "Tommy has 2 coins left."
"""


def counter_factory(start=0):  # Define a factory that returns a counter closure.
    count = start  # Initialize the enclosed counter value.

    def increment():  # Define a function that updates the counter.
        nonlocal count  # Declare we will rebind the enclosed count.
        count += 1  # Increment the counter.
        return count  # Return the new counter value.

    return increment  # Return the increment function as a closure.


EXAMPLE_WALKTHROUGH_COUNTER_FACTORY = """  # Store a walkthrough for counter_factory.
Example Walkthrough: counter_factory
- count = start:
  initializes the enclosed counter with the start value.
- def increment():
  defines the inner function that will update count.
- nonlocal count:
  allows increment to change the enclosed count variable.
- count += 1:
  increases the counter by 1.
- return count:
  returns the updated counter value.
- return increment:
  returns the inner function as a closure.
Example usage:
- counter = counter_factory(10) creates a counter starting at 10.
- counter() returns 11, then 12 on the next call.
"""


NOTES = """  # Store study notes as a multiline string.
Notes:
- Closures capture variables, not their values at definition time.
- Each call to a factory creates a separate enclosed state.
"""


QUESTIONS = """  # Store practice questions as a multiline string.
Questions:
1) What does nonlocal do inside play_game?
2) Why do tommy and dave not share the same coin count?
3) How could you reset the counter produced by counter_factory?
4) When might a class be better than a closure?
"""


def main():  # Define the script entry point.
    show_section("Coin game")  # Display the coin game header.
    tommy = game_factory("Tommy", 3)  # Create a closure for Tommy.
    tommy()  # Play the game for Tommy once.
    tommy()  # Play the game for Tommy again.
    tommy()  # Play the game for Tommy a third time.

    dave = game_factory("Dave", 2)  # Create a closure for Dave.
    dave()  # Play the game for Dave once.
    dave()  # Play the game for Dave again.

    show_section("Counter")  # Display the counter header.
    counter = counter_factory(10)  # Create a counter starting at 10.
    print(counter())  # Increment and print the counter.
    print(counter())  # Increment and print the counter again.

    print(NOTES.strip())  # Print notes without extra whitespace.
    print()  # Print a blank line between notes and questions.
    print(QUESTIONS.strip())  # Print questions for review.


EXAMPLE_WALKTHROUGH_MAIN = """  # Store a walkthrough for main.
Example Walkthrough: main
- show_section("Coin game"):
  prints the "Coin game" header and underline.
- tommy = game_factory("Tommy", 3):
  creates a closure that tracks coins for Tommy.
- tommy():
  prints "Tommy has 2 coins left."
- tommy():
  prints "Tommy has 1 coin left."
- tommy():
  prints "Tommy has no coins left. Game over!"
- dave = game_factory("Dave", 2):
  creates a closure that tracks coins for Dave.
- dave():
  prints "Dave has 1 coin left."
- dave():
  prints "Dave has no coins left. Game over!"
- show_section("Counter"):
  prints the "Counter" header and underline.
- counter = counter_factory(10):
  creates a counter starting at 10.
- print(counter()):
  prints 11.
- print(counter()):
  prints 12.
- print(NOTES.strip()):
  prints the Notes block.
- print():
  prints a blank line.
- print(QUESTIONS.strip()):
  prints the Questions block.
"""


if __name__ == "__main__":  # Run main only when executed directly.
    main()  # Invoke the entry point.
