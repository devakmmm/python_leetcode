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


EXAMPLE_WALKTHROUGH_RANDOM_CITY = """  # Store a walkthrough for random_city.
Example Walkthrough: random_city
- cities = [...]:
  creates a list of city names.
- return choice(cities):
  returns one random city from the list.
Example usage:
- random_city() might return "Buffalo".
"""


def describe():  # Define a function to summarize the data.
    return f"NY: capital={capital}, population={population}, area={area_sq_miles} sq mi"  # Build summary.


EXAMPLE_WALKTHROUGH_DESCRIBE = """  # Store a walkthrough for describe.
Example Walkthrough: describe
- return f"NY: capital=...":
  builds a summary string from module constants.
Example usage:
- describe() returns "NY: capital=Albany, population=19453561, area=54555 sq mi".
"""


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


EXAMPLE_WALKTHROUGH_MAIN = """  # Store a walkthrough for main.
Example Walkthrough: main
- print("Capital:", capital):
  outputs: Capital: Albany
- print("Random city:", random_city()):
  outputs a random city name.
- print(describe()):
  outputs the summary string.
- print(NOTES.strip()):
  prints the Notes block.
- print():
  prints a blank line.
- print(QUESTIONS.strip()):
  prints the Questions block.
"""


if __name__ == "__main__":  # Run main only when executed directly.
    main()  # Invoke the entry point.
