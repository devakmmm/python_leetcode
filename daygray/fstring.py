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


EXAMPLE_WALKTHROUGH_BASIC = """  # Store a walkthrough for basic_examples.
Example Walkthrough: basic_examples
- show_section("Basics"):
  prints the "Basics" header and underline.
- person = "Dave":
  sets person to "Dave".
- coins = 3:
  sets coins to 3.
- print(f"{person} has {coins} coins left."):
  outputs: Dave has 3 coins left.
- player = {"person": "Alice", "coins": 5}:
  creates a dict with a name and coins.
- print(f"{player['person']} has {player['coins']} coins left."):
  outputs: Alice has 5 coins left.
"""


def formatting_examples():  # Define a demo for formatting numbers and dates.
    show_section("Formatting")  # Display the section header.
    num = 10  # Store a number for math examples.
    print(f"2.25 times {num} is {2.25 * num:.2f}")  # Format a float to 2 decimals.
    print(f"2.25 divided by {num} is {2.25 / num:.2%}")  # Format as a percent.
    print(f"padded: |{num:>6}| |{num:<6}| |{num:^6}|")  # Align within 6 chars.

    today = datetime(2024, 1, 15)  # Create a specific date instance.
    print(f"date: {today:%Y-%m-%d}")  # Format the date using strftime syntax.


EXAMPLE_WALKTHROUGH_FORMATTING = """  # Store a walkthrough for formatting_examples.
Example Walkthrough: formatting_examples
- show_section("Formatting"):
  prints the "Formatting" header and underline.
- num = 10:
  sets num to 10.
- print(f"2.25 times {num} is {2.25 * num:.2f}"):
  outputs: 2.25 times 10 is 22.50
- print(f"2.25 divided by {num} is {2.25 / num:.2%}"):
  outputs: 2.25 divided by 10 is 22.50%
- print(f"padded: |{num:>6}| |{num:<6}| |{num:^6}|"):
  outputs: padded: |    10| |10    | |  10  |
- today = datetime(2024, 1, 15):
  creates a date object.
- print(f"date: {today:%Y-%m-%d}"):
  outputs: date: 2024-01-15
"""


def other_styles():  # Define a demo for older formatting styles.
    show_section("Other formatting styles")  # Display the section header.
    person = "Dave"  # Store a name for formatting examples.
    coins = 3  # Store a number for formatting examples.
    old = "%s has %s coins left." % (person, coins)  # Use percent formatting.
    newer = "{} has {} coins left.".format(person, coins)  # Use str.format.
    print("percent:", old)  # Print the percent-formatted string.
    print("format:", newer)  # Print the format-formatted string.


EXAMPLE_WALKTHROUGH_OTHER = """  # Store a walkthrough for other_styles.
Example Walkthrough: other_styles
- show_section("Other formatting styles"):
  prints the "Other formatting styles" header and underline.
- person = "Dave":
  sets person to "Dave".
- coins = 3:
  sets coins to 3.
- old = "%s has %s coins left." % (person, coins):
  builds a percent-formatted string.
- newer = "{} has {} coins left.".format(person, coins):
  builds a format() string.
- print("percent:", old):
  outputs: percent: Dave has 3 coins left.
- print("format:", newer):
  outputs: format: Dave has 3 coins left.
"""


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


EXAMPLE_WALKTHROUGH_MAIN = """  # Store a walkthrough for main.
Example Walkthrough: main
- basic_examples():
  runs the basic f-string section.
- formatting_examples():
  runs the formatting section.
- other_styles():
  runs the alternative formatting section.
- print(NOTES.strip()):
  prints the Notes block.
- print():
  prints a blank line.
- print(QUESTIONS.strip()):
  prints the Questions block.
"""


if __name__ == "__main__":  # Run main only when executed directly.
    main()  # Invoke the entry point.
