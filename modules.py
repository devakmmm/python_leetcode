"""
modules.py - Importing modules and using __name__.

Learning goals:
- Import standard library modules
- Import local modules
- Use aliases and selective imports
- Understand __name__ and module execution
"""

import math
import newyork


def show_section(title):
    print("\n" + title)
    print("-" * len(title))


def stdlib_examples():
    show_section("Standard library")
    print("math.sqrt(16):", math.sqrt(16))
    print("math.pi:", math.pi)


def local_module_examples():
    show_section("Local module (newyork)")
    print("capital:", newyork.capital)
    print("random city:", newyork.random_city())
    print("describe:", newyork.describe())
    print("newyork.__name__:", newyork.__name__)


def name_example():
    show_section("__name__")
    print("__name__ in this file:", __name__)


NOTES = """
Notes:
- Importing a module runs its top-level code once.
- Use if __name__ == "__main__": to make a file runnable and importable.
- Aliases (import math as m) can improve readability when used sparingly.
"""


QUESTIONS = """
Questions:
1) What is the difference between import math and from math import sqrt?
2) When does a module's top-level code run?
3) Why is __name__ == "__main__" a common pattern?
4) How would you avoid name clashes between modules?
"""


def main():
    stdlib_examples()
    local_module_examples()
    name_example()

    print(NOTES.strip())
    print()
    print(QUESTIONS.strip())


if __name__ == "__main__":
    main()
