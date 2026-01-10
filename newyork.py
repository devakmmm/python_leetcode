"""
newyork.py - Example module with constants and functions.

Learning goals:
- Module-level constants
- Functions that can be imported
- Using __name__ to make code runnable as a script
"""

from random import choice

capital = "Albany"
population = 19453561  # 2020 census
area_sq_miles = 54555


def random_city():
    cities = ["New York City", "Buffalo", "Rochester", "Syracuse", "Albany"]
    return choice(cities)


def describe():
    return f"NY: capital={capital}, population={population}, area={area_sq_miles} sq mi"


NOTES = """
Notes:
- When this file is imported, only the top-level statements run.
- Functions are reusable from other modules: import newyork; newyork.random_city().
"""


QUESTIONS = """
Questions:
1) Why is code inside if __name__ == "__main__": useful?
2) How would you test random_city deterministically?
3) What is a good reason to keep constants at module scope?
"""


def main():
    print("Capital:", capital)
    print("Random city:", random_city())
    print(describe())
    print(NOTES.strip())
    print()
    print(QUESTIONS.strip())


if __name__ == "__main__":
    main()
