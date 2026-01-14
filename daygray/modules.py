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


EXAMPLE_WALKTHROUGH_STDLIB = """  # Store a walkthrough for stdlib_examples.
Example Walkthrough: stdlib_examples
- show_section("Standard library"):
  prints the "Standard library" header and underline.
- print("math.sqrt(16):", math.sqrt(16)):
  outputs: math.sqrt(16): 4.0
- print("math.pi:", math.pi):
  outputs: math.pi: 3.141592653589793
"""


def local_module_examples():  # Define a demo for local module usage.
    show_section("Local module (newyork)")  # Display the section header.
    print("capital:", newyork.capital)  # Access a module-level constant.
    print("random city:", newyork.random_city())  # Call a module function.
    print("describe:", newyork.describe())  # Call another module function.
    print("newyork.__name__:", newyork.__name__)  # Show the module name.


EXAMPLE_WALKTHROUGH_LOCAL = """  # Store a walkthrough for local_module_examples.
Example Walkthrough: local_module_examples
- show_section("Local module (newyork)"):
  prints the section header.
- print("capital:", newyork.capital):
  outputs: capital: Albany
- print("random city:", newyork.random_city()):
  outputs a random city name from the list.
- print("describe:", newyork.describe()):
  outputs: NY: capital=Albany, population=19453561, area=54555 sq mi
- print("newyork.__name__:", newyork.__name__):
  outputs: newyork.__name__: newyork
"""


def name_example():  # Define a demo for __name__.
    show_section("__name__")  # Display the section header.
    print("__name__ in this file:", __name__)  # Show this module's name.


EXAMPLE_WALKTHROUGH_NAME = """  # Store a walkthrough for name_example.
Example Walkthrough: name_example
- show_section("__name__"):
  prints the "__name__" header and underline.
- print("__name__ in this file:", __name__):
  outputs __main__ when run directly, or the module name if imported.
"""


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


EXAMPLE_WALKTHROUGH_MAIN = """  # Store a walkthrough for main.
Example Walkthrough: main
- stdlib_examples():
  runs the standard library section.
- local_module_examples():
  runs the local module section.
- name_example():
  runs the __name__ section.
- print(NOTES.strip()):
  prints the Notes block.
- print():
  prints a blank line.
- print(QUESTIONS.strip()):
  prints the Questions block.
"""


if __name__ == "__main__":  # Run main only when executed directly.
    main()  # Invoke the entry point.
