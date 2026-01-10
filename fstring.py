"""
fstring.py - String formatting with f-strings.

Learning goals:
- Basic f-string usage
- Formatting numbers and alignment
- Accessing dict values inside f-strings
- Comparing with older formatting styles
"""

from datetime import datetime  # Import datetime for date formatting examples.


def show_section(title):  # Define a helper to label output sections.
    print("\n" + title)  # Print a blank line and the section title.
    print("-" * len(title))  # Print a dashed underline for the title.


def basic_examples():  # Define a demo for basic f-string usage.
    show_section("Basics")  # Display the section header.
    person = "Dave"  # Assign a name to format into strings.
    coins = 3  # Assign a number to embed in a string.
    print(f"{person} has {coins} coins left.")  # Use f-string interpolation.

    player = {"person": "Alice", "coins": 5}  # Build a dict of values.
    print(f"{player['person']} has {player['coins']} coins left.")  # Access dict in f-string.


def formatting_examples():  # Define a demo for formatting numbers and dates.
    show_section("Formatting")  # Display the section header.
    num = 10  # Store a number for math examples.
    print(f"2.25 times {num} is {2.25 * num:.2f}")  # Format a float to 2 decimals.
    print(f"2.25 divided by {num} is {2.25 / num:.2%}")  # Format as a percent.
    print(f"padded: |{num:>6}| |{num:<6}| |{num:^6}|")  # Align within 6 chars.

    today = datetime(2024, 1, 15)  # Create a specific date instance.
    print(f"date: {today:%Y-%m-%d}")  # Format the date using strftime syntax.


def other_styles():  # Define a demo for older formatting styles.
    show_section("Other formatting styles")  # Display the section header.
    person = "Dave"  # Store a name for formatting examples.
    coins = 3  # Store a number for formatting examples.
    old = "%s has %s coins left." % (person, coins)  # Use percent formatting.
    newer = "{} has {} coins left.".format(person, coins)  # Use str.format.
    print("percent:", old)  # Print the percent-formatted string.
    print("format:", newer)  # Print the format-formatted string.


NOTES = """  # Store study notes as a multiline string.
Notes:
- F-strings evaluate expressions at runtime and are easy to read.
- Format specifiers like .2f or :>6 control precision and alignment.
- Use double quotes around f-strings when you need single quotes inside.
"""


QUESTIONS = """  # Store practice questions as a multiline string.
Questions:
1) What does :.2f do in an f-string?
2) How do you right-align a number in 10 characters?
3) Why might you still see .format() in older codebases?
4) How would you format a number as a percentage with 1 decimal?
5) What is the output of f"{2 + 3=}" in Python 3.8+?
"""


def main():  # Define the script entry point.
    basic_examples()  # Run the basic f-string examples.
    formatting_examples()  # Run the formatting examples.
    other_styles()  # Run the alternative formatting examples.

    print(NOTES.strip())  # Print notes without extra whitespace.
    print()  # Print a blank line between notes and questions.
    print(QUESTIONS.strip())  # Print questions for review.


if __name__ == "__main__":  # Run main only when executed directly.
    main()  # Invoke the entry point.
