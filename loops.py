"""
loops.py - For and while loops, range, enumerate, and break/continue.

Learning goals:
- Iterate over sequences and ranges
- Use break, continue, and loop else
- Nested loops and zip
- Common loop patterns
"""


def show_section(title):  # Define a helper to label output sections.
    print("\n" + title)  # Print a blank line and the section title.
    print("-" * len(title))  # Print a dashed underline under the title.


def for_loops():  # Define a demo for basic for loops.
    show_section("For loops over lists and strings")  # Display the section header.
    names = ["Alice", "Bob", "Charlie", "Diana"]  # Create a list of names.
    for name in names:  # Loop over each name.
        print("name:", name)  # Print the current name.

    for ch in "Mississippi":  # Loop over characters in a string.
        print("ch:", ch)  # Print the current character.


def range_and_enumerate():  # Define a demo for range and enumerate.
    show_section("range and enumerate")  # Display the section header.
    for i in range(5):  # Iterate over numbers 0 to 4.
        print("range(5):", i)  # Print each number.

    for i in range(1, 10, 2):  # Iterate over odd numbers.
        print("range(1,10,2):", i)  # Print each odd number.

    for i in range(5, 0, -1):  # Count down from 5 to 1.
        print("countdown:", i)  # Print each countdown value.

    names = ["Alice", "Bob", "Charlie"]  # Create a list for enumerate.
    for i, name in enumerate(names, start=1):  # Enumerate starting at 1.
        print("enumerate:", i, name)  # Print index and name.


def break_continue_else():  # Define a demo for break/continue/else.
    show_section("break, continue, and loop else")  # Display the section header.
    names = ["Alice", "Bob", "Charlie"]  # Create a list for searching.
    for name in names:  # Loop over names.
        if name == "Charlie":  # Check for a target name.
            print("Found Charlie!")  # Print a found message.
            break  # Exit the loop early.
        print("checking:", name)  # Print each checked name.
    else:  # Run only if loop completes without break.
        print("Charlie not found")  # Print not found message.

    for name in names:  # Loop over names again.
        if name.startswith("B"):  # Skip names starting with B.
            continue  # Skip to the next iteration.
        print("not starting with B:", name)  # Print the remaining names.


def nested_and_zip():  # Define a demo for nested loops and zip.
    show_section("Nested loops and zip")  # Display the section header.
    names = ["Eve", "Frank", "Grace"]  # Create a list of names.
    actions = ["runs", "jumps", "swims"]  # Create a list of actions.

    for name in names:  # Outer loop over names.
        for action in actions:  # Inner loop over actions.
            print(name, action)  # Print every combination.

    for name, action in zip(names, actions):  # Pair items with zip.
        print("paired:", name, action)  # Print each paired result.


def while_loops():  # Define a demo for while loops.
    show_section("While loops")  # Display the section header.
    count = 3  # Initialize a counter.
    while count > 0:  # Loop while count is positive.
        print("count:", count)  # Print the current count.
        count -= 1  # Decrement the counter.

    attempts = 0  # Initialize attempt counter.
    while True:  # Start an infinite loop.
        attempts += 1  # Increment attempt count.
        if attempts == 2:  # Break after two attempts.
            print("breaking at attempts:", attempts)  # Print break message.
            break  # Exit the loop.


NOTES = """  # Store study notes as a multiline string.
Notes:
- for loops iterate over any iterable (lists, strings, dicts, ranges).
- break exits the loop; continue skips to the next iteration.
- A loop else runs only if the loop did not break.
- zip stops at the shortest iterable.
"""


QUESTIONS = """  # Store practice questions as a multiline string.
Questions:
1) What does range(3, -1, -1) produce?
2) When would you prefer enumerate over a manual index?
3) What is the difference between break and continue?
4) How does loop else behave when a break occurs?
5) What happens if you zip lists of different lengths?
6) Write a loop that collects even numbers from 1 to 10.
7) Convert a for loop into a while loop for counting down from 5.
"""


def main():  # Define the script entry point.
    for_loops()  # Run for-loop examples.
    range_and_enumerate()  # Run range and enumerate examples.
    break_continue_else()  # Run break/continue/else examples.
    nested_and_zip()  # Run nested loop and zip examples.
    while_loops()  # Run while-loop examples.

    print(NOTES.strip())  # Print notes without extra whitespace.
    print()  # Print a blank line between notes and questions.
    print(QUESTIONS.strip())  # Print questions for review.


if __name__ == "__main__":  # Run main only when executed directly.
    main()  # Invoke the entry point.
