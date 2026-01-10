"""
modules.py - Importing modules and using __name__.

Learning goals:
- Import standard library modules
- Import local modules
- Use aliases and selective imports
- Understand __name__ and module execution
"""

import math  # Import the standard math module.
import newyork  # Import the local newyork module.


def show_section(title):  # Define a helper to label output sections.
    print("\n" + title)  # Print a blank line and the section title.
    print("-" * len(title))  # Print a dashed underline under the title.


def stdlib_examples():  # Define a demo for standard library imports.
    show_section("Standard library")  # Display the section header.
    print("math.sqrt(16):", math.sqrt(16))  # Call a math function.
    print("math.pi:", math.pi)  # Print the pi constant.


def local_module_examples():  # Define a demo for local module usage.
    show_section("Local module (newyork)")  # Display the section header.
    print("capital:", newyork.capital)  # Access a module-level constant.
    print("random city:", newyork.random_city())  # Call a module function.
    print("describe:", newyork.describe())  # Call another module function.
    print("newyork.__name__:", newyork.__name__)  # Show the module name.


def name_example():  # Define a demo for __name__.
    show_section("__name__")  # Display the section header.
    print("__name__ in this file:", __name__)  # Show this module's name.


NOTES = """  # Store study notes as a multiline string.
Notes:
- Importing a module runs its top-level code once.
- Use if __name__ == "__main__": to make a file runnable and importable.
- Aliases (import math as m) can improve readability when used sparingly.
"""


QUESTIONS = """  # Store practice questions as a multiline string.
Questions:
1) What is the difference between import math and from math import sqrt?
2) When does a module's top-level code run?
3) Why is __name__ == "__main__" a common pattern?
4) How would you avoid name clashes between modules?
"""


def main():  # Define the script entry point.
    stdlib_examples()  # Run standard library examples.
    local_module_examples()  # Run local module examples.
    name_example()  # Run the __name__ demo.

    print(NOTES.strip())  # Print notes without extra whitespace.
    print()  # Print a blank line between notes and questions.
    print(QUESTIONS.strip())  # Print questions for review.


if __name__ == "__main__":  # Run main only when executed directly.
    main()  # Invoke the entry point.
