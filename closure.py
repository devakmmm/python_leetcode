"""
closure.py - Closures in Python.

Learning goals:
- A closure remembers variables from its enclosing scope
- Use nonlocal to mutate enclosed variables
"""


def show_section(title):
    print("\n" + title)
    print("-" * len(title))


def game_factory(person, coins):
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


def counter_factory(start=0):
    count = start

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


NOTES = """
Notes:
- Closures capture variables, not their values at definition time.
- Each call to a factory creates a separate enclosed state.
"""


QUESTIONS = """
Questions:
1) What does nonlocal do inside play_game?
2) Why do tommy and dave not share the same coin count?
3) How could you reset the counter produced by counter_factory?
4) When might a class be better than a closure?
"""


def main():
    show_section("Coin game")
    tommy = game_factory("Tommy", 3)
    tommy()
    tommy()
    tommy()

    dave = game_factory("Dave", 2)
    dave()
    dave()

    show_section("Counter")
    counter = counter_factory(10)
    print(counter())
    print(counter())

    print(NOTES.strip())
    print()
    print(QUESTIONS.strip())


if __name__ == "__main__":
    main()
