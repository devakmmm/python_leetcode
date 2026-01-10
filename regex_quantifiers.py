"""
regex_quantifiers.py - Explain \d and \d+ in Python regular expressions.

Learning goals:
- Understand what \d matches
- Understand what the + quantifier does
- Compare \d vs \d+ results
"""

import re  # Import the regular expression module.


def show_section(title):  # Define a helper to label output sections.
    print("\n" + title)  # Print a blank line and the section title.
    print("-" * len(title))  # Print a dashed underline under the title.


def explain_digit_class():  # Define a demo for the \d digit class.
    show_section(r"\d matches a single digit")  # Display a section title.
    book = "Fahrenheit 451"  # Create a sample string with digits.
    match = re.search(r"\d", book)  # Search for the first digit.
    print("match:", match)  # Show the match object or None.
    if match:  # Check that a match was found.
        print("group:", match.group())  # Print the matched digit.
        print("span:", match.span())  # Print the start/end indices.

    no_digits = "No numbers here"  # Create a string without digits.
    print("no digit match:", re.search(r"\d", no_digits))  # Show no match.


EXAMPLE_WALKTHROUGH_DIGIT = r"""  # Store a walkthrough for the \d section.
Example Walkthrough: explain_digit_class
- show_section(r"\d matches a single digit"):
  prints a header line and underline:
  \d matches a single digit
  ------------------------
- book = "Fahrenheit 451":
  sets book to a string with digits at indices 11, 12, 13.
- match = re.search(r"\d", book):
  finds the first digit; match is <re.Match ... match='4'>.
- print("match:", match):
  outputs: match: <re.Match object; span=(11, 12), match='4'>
- if match:
  condition is True because a match was found.
- print("group:", match.group()):
  outputs: group: 4
- print("span:", match.span()):
  outputs: span: (11, 12)
- no_digits = "No numbers here":
  sets a string that has no digits.
- print("no digit match:", re.search(r"\d", no_digits)):
  outputs: no digit match: None
"""


def explain_plus_quantifier():  # Define a demo for the + quantifier.
    show_section(r"\d+ matches one or more digits")  # Display a section title.
    book = "Fahrenheit 451"  # Create a sample string with digits.
    match = re.search(r"\d+", book)  # Search for one or more digits.
    print("match:", match)  # Show the match object or None.
    if match:  # Check that a match was found.
        print("group:", match.group())  # Print the full digit sequence.
        print("span:", match.span())  # Print the start/end indices.


EXAMPLE_WALKTHROUGH_PLUS = r"""  # Store a walkthrough for the \d+ section.
Example Walkthrough: explain_plus_quantifier
- show_section(r"\d+ matches one or more digits"):
  prints a header line and underline:
  \d+ matches one or more digits
  -----------------------------
- book = "Fahrenheit 451":
  sets book to a string with digits.
- match = re.search(r"\d+", book):
  finds the full digit run; match is <re.Match ... match='451'>.
- print("match:", match):
  outputs: match: <re.Match object; span=(11, 14), match='451'>
- if match:
  condition is True because a match was found.
- print("group:", match.group()):
  outputs: group: 451
- print("span:", match.span()):
  outputs: span: (11, 14)
"""


def compare_findall():  # Define a demo comparing findall results.
    show_section(r"findall: \d vs \d+")  # Display a section title.
    text = "Room 451, Floor 7"  # Create a string with multiple numbers.
    print(r"\d:", re.findall(r"\d", text))  # Each digit as a separate match.
    print(r"\d+:", re.findall(r"\d+", text))  # Each full number as a match.


EXAMPLE_WALKTHROUGH_FINDALL = r"""  # Store a walkthrough for the findall section.
Example Walkthrough: compare_findall
- show_section(r"findall: \d vs \d+"):
  prints a header line and underline:
  findall: \d vs \d+
  ------------------
- text = "Room 451, Floor 7":
  sets text with a multi-digit number and a single-digit number.
- print(r"\d:", re.findall(r"\d", text)):
  outputs: \d: ['4', '5', '1', '7']
- print(r"\d+:", re.findall(r"\d+", text)):
  outputs: \d+: ['451', '7']
"""


NOTES = """  # Store study notes as a multiline string.
Notes:
- \\d is a character class that matches a single digit (0-9).
- \\d+ means one or more digits in a row.
- Use raw strings (r"...") to avoid escape confusion in Python strings.
"""


QUESTIONS = """  # Store practice questions as a multiline string.
Questions:
1) What does \\d* match, and how is it different from \\d+?
2) What would re.findall(r"\\d", "2024") return?
3) Why is r"\\d" preferred over "\\\\d" in Python?
"""


def main():  # Define the script entry point.
    explain_digit_class()  # Run the \\d example.
    explain_plus_quantifier()  # Run the \\d+ example.
    compare_findall()  # Compare \\d vs \\d+ with findall.
    print(NOTES.strip())  # Print notes without extra whitespace.
    print()  # Print a blank line between notes and questions.
    print(QUESTIONS.strip())  # Print questions for review.


if __name__ == "__main__":  # Run main only when executed directly.
    main()  # Invoke the entry point.
