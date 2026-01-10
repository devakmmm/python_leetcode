"""
fstring.py - String formatting with f-strings.

Learning goals:
- Basic f-string usage
- Formatting numbers and alignment
- Accessing dict values inside f-strings
- Comparing with older formatting styles
"""

from datetime import datetime


def show_section(title):
    print("\n" + title)
    print("-" * len(title))


def basic_examples():
    show_section("Basics")
    person = "Dave"
    coins = 3
    print(f"{person} has {coins} coins left.")

    player = {"person": "Alice", "coins": 5}
    print(f"{player['person']} has {player['coins']} coins left.")


def formatting_examples():
    show_section("Formatting")
    num = 10
    print(f"2.25 times {num} is {2.25 * num:.2f}")
    print(f"2.25 divided by {num} is {2.25 / num:.2%}")
    print(f"padded: |{num:>6}| |{num:<6}| |{num:^6}|")

    today = datetime(2024, 1, 15)
    print(f"date: {today:%Y-%m-%d}")


def other_styles():
    show_section("Other formatting styles")
    person = "Dave"
    coins = 3
    old = "%s has %s coins left." % (person, coins)
    newer = "{} has {} coins left.".format(person, coins)
    print("percent:", old)
    print("format:", newer)


NOTES = """
Notes:
- F-strings evaluate expressions at runtime and are easy to read.
- Format specifiers like .2f or :>6 control precision and alignment.
- Use double quotes around f-strings when you need single quotes inside.
"""


QUESTIONS = """
Questions:
1) What does :.2f do in an f-string?
2) How do you right-align a number in 10 characters?
3) Why might you still see .format() in older codebases?
4) How would you format a number as a percentage with 1 decimal?
5) What is the output of f"{2 + 3=}" in Python 3.8+?
"""


def main():
    basic_examples()
    formatting_examples()
    other_styles()

    print(NOTES.strip())
    print()
    print(QUESTIONS.strip())


if __name__ == "__main__":
    main()
