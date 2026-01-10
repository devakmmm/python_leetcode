"""
loops.py - For and while loops, range, enumerate, and break/continue.

Learning goals:
- Iterate over sequences and ranges
- Use break, continue, and loop else
- Nested loops and zip
- Common loop patterns
"""


def show_section(title):
    print("\n" + title)
    print("-" * len(title))


def for_loops():
    show_section("For loops over lists and strings")
    names = ["Alice", "Bob", "Charlie", "Diana"]
    for name in names:
        print("name:", name)

    for ch in "Mississippi":
        print("ch:", ch)


def range_and_enumerate():
    show_section("range and enumerate")
    for i in range(5):
        print("range(5):", i)

    for i in range(1, 10, 2):
        print("range(1,10,2):", i)

    for i in range(5, 0, -1):
        print("countdown:", i)

    names = ["Alice", "Bob", "Charlie"]
    for i, name in enumerate(names, start=1):
        print("enumerate:", i, name)


def break_continue_else():
    show_section("break, continue, and loop else")
    names = ["Alice", "Bob", "Charlie"]
    for name in names:
        if name == "Charlie":
            print("Found Charlie!")
            break
        print("checking:", name)
    else:
        print("Charlie not found")

    for name in names:
        if name.startswith("B"):
            continue
        print("not starting with B:", name)


def nested_and_zip():
    show_section("Nested loops and zip")
    names = ["Eve", "Frank", "Grace"]
    actions = ["runs", "jumps", "swims"]

    for name in names:
        for action in actions:
            print(name, action)

    for name, action in zip(names, actions):
        print("paired:", name, action)


def while_loops():
    show_section("While loops")
    count = 3
    while count > 0:
        print("count:", count)
        count -= 1

    attempts = 0
    while True:
        attempts += 1
        if attempts == 2:
            print("breaking at attempts:", attempts)
            break


NOTES = """
Notes:
- for loops iterate over any iterable (lists, strings, dicts, ranges).
- break exits the loop; continue skips to the next iteration.
- A loop else runs only if the loop did not break.
- zip stops at the shortest iterable.
"""


QUESTIONS = """
Questions:
1) What does range(3, -1, -1) produce?
2) When would you prefer enumerate over a manual index?
3) What is the difference between break and continue?
4) How does loop else behave when a break occurs?
5) What happens if you zip lists of different lengths?
6) Write a loop that collects even numbers from 1 to 10.
7) Convert a for loop into a while loop for counting down from 5.
"""


def main():
    for_loops()
    range_and_enumerate()
    break_continue_else()
    nested_and_zip()
    while_loops()

    print(NOTES.strip())
    print()
    print(QUESTIONS.strip())


if __name__ == "__main__":
    main()
