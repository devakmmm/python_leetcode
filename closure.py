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


def counter_factory(start=0):  # Define a factory that returns a counter closure.
    count = start  # Initialize the enclosed counter value.

    def increment():  # Define a function that updates the counter.
        nonlocal count  # Declare we will rebind the enclosed count.
        count += 1  # Increment the counter.
        return count  # Return the new counter value.

    return increment  # Return the increment function as a closure.


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


if __name__ == "__main__":  # Run main only when executed directly.
    main()  # Invoke the entry point.
