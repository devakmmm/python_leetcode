"""
newyork.py - Example module with constants and functions.

Learning goals:
- Module-level constants
- Functions that can be imported
- Using __name__ to make code runnable as a script
"""

from random import choice  # Import choice for random selection.

capital = "Albany"  # Define the state capital.
population = 19453561  # Define population as of 2020 census.
area_sq_miles = 54555  # Define area in square miles.


def random_city():  # Define a function to pick a random city.
    cities = ["New York City", "Buffalo", "Rochester", "Syracuse", "Albany"]  # List cities.
    return choice(cities)  # Return a random city from the list.


def describe():  # Define a function to summarize the data.
    return f"NY: capital={capital}, population={population}, area={area_sq_miles} sq mi"  # Build summary.


NOTES = """  # Store study notes as a multiline string.
Notes:
- When this file is imported, only the top-level statements run.
- Functions are reusable from other modules: import newyork; newyork.random_city().
"""


QUESTIONS = """  # Store practice questions as a multiline string.
Questions:
1) Why is code inside if __name__ == "__main__": useful?
2) How would you test random_city deterministically?
3) What is a good reason to keep constants at module scope?
"""


def main():  # Define the script entry point.
    print("Capital:", capital)  # Print the capital constant.
    print("Random city:", random_city())  # Print a random city.
    print(describe())  # Print the summary line.
    print(NOTES.strip())  # Print notes without extra whitespace.
    print()  # Print a blank line between notes and questions.
    print(QUESTIONS.strip())  # Print questions for review.


if __name__ == "__main__":  # Run main only when executed directly.
    main()  # Invoke the entry point.
