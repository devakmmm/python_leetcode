"""
lambda.py - Anonymous functions (lambda) in Python.

Learning goals:
- Create lambdas for short, simple functions
- Use map, filter, and reduce
- Use lambdas for sorting keys
"""

from functools import reduce  # Import reduce for aggregation examples.


def show_section(title):  # Define a helper to label output sections.
    print("\n" + title)  # Print a blank line and the section title.
    print("-" * len(title))  # Print a dashed underline under the title.


def basic_lambda():  # Define a demo for basic lambda usage.
    show_section("Basic lambda")  # Display the section header.
    squared = lambda num: num * num  # Create a lambda that squares a number.
    print("squared(5):", squared(5))  # Call the lambda and print the result.

    def squared_def(num):  # Define an equivalent named function.
        return num * num  # Return the square of the input.

    print("squared_def(5):", squared_def(5))  # Call the named function.


EXAMPLE_WALKTHROUGH_BASIC = """  # Store a walkthrough for basic_lambda.
Example Walkthrough: basic_lambda
- show_section("Basic lambda"):
  prints the "Basic lambda" header and underline.
- squared = lambda num: num * num:
  defines a lambda that squares its input.
- print("squared(5):", squared(5)):
  outputs: squared(5): 25
- def squared_def(num):
  defines a named function that squares its input.
- print("squared_def(5):", squared_def(5)):
  outputs: squared_def(5): 25
"""


def closures_with_lambda():  # Define a demo for lambda closures.
    show_section("Closures with lambda")  # Display the section header.

    def function_builder(x):  # Define a factory function that closes over x.
        return lambda num: x + num  # Return a lambda that adds x to num.

    add_five = function_builder(5)  # Build a closure that adds five.
    subtract_three = function_builder(-3)  # Build a closure that subtracts three.
    print("add_five(10):", add_five(10))  # Use the closure.
    print("subtract_three(10):", subtract_three(10))  # Use the closure.


EXAMPLE_WALKTHROUGH_CLOSURES = """  # Store a walkthrough for closures_with_lambda.
Example Walkthrough: closures_with_lambda
- show_section("Closures with lambda"):
  prints the "Closures with lambda" header and underline.
- def function_builder(x):
  defines a factory that captures x.
- return lambda num: x + num:
  returns a lambda that adds x to num.
- add_five = function_builder(5):
  creates a closure that adds 5.
- subtract_three = function_builder(-3):
  creates a closure that subtracts 3.
- print("add_five(10):", add_five(10)):
  outputs: add_five(10): 15
- print("subtract_three(10):", subtract_three(10)):
  outputs: subtract_three(10): 7
"""


def map_filter_reduce():  # Define a demo for map, filter, and reduce.
    show_section("map, filter, reduce")  # Display the section header.
    numbers = [1, 2, 3, 4, 5]  # Create a list of numbers.
    squared_numbers = list(map(lambda n: n * n, numbers))  # Map to squares.
    odd_numbers = list(filter(lambda n: n % 2 != 0, numbers))  # Filter odds.
    total = reduce(lambda acc, curr: acc + curr, numbers)  # Reduce to a sum.

    print("squared_numbers:", squared_numbers)  # Show mapped results.
    print("odd_numbers:", odd_numbers)  # Show filtered results.
    print("total:", total)  # Show reduced result.


EXAMPLE_WALKTHROUGH_MFR = """  # Store a walkthrough for map_filter_reduce.
Example Walkthrough: map_filter_reduce
- show_section("map, filter, reduce"):
  prints the "map, filter, reduce" header and underline.
- numbers = [1, 2, 3, 4, 5]:
  creates the list of numbers.
- squared_numbers = list(map(lambda n: n * n, numbers)):
  produces [1, 4, 9, 16, 25].
- odd_numbers = list(filter(lambda n: n % 2 != 0, numbers)):
  produces [1, 3, 5].
- total = reduce(lambda acc, curr: acc + curr, numbers):
  produces 15.
- print("squared_numbers:", squared_numbers):
  outputs: squared_numbers: [1, 4, 9, 16, 25]
- print("odd_numbers:", odd_numbers):
  outputs: odd_numbers: [1, 3, 5]
- print("total:", total):
  outputs: total: 15
"""


def sorting_with_lambda():  # Define a demo for sorting with lambdas.
    show_section("Sorting with lambda")  # Display the section header.
    names = ["alice", "Bob", "charlie", "dave"]  # Create a list of names.
    print("case-insensitive:", sorted(names, key=lambda s: s.lower()))  # Sort ignoring case.

    people = [  # Build a list of dictionaries representing people.
        {"name": "Alice", "age": 31},  # Add a person entry.
        {"name": "Bob", "age": 25},  # Add a person entry.
        {"name": "Charlie", "age": 29},  # Add a person entry.
    ]  # Close the list of people.
    print("sorted by age:", sorted(people, key=lambda p: p["age"]))  # Sort by age.


EXAMPLE_WALKTHROUGH_SORTING = """  # Store a walkthrough for sorting_with_lambda.
Example Walkthrough: sorting_with_lambda
- show_section("Sorting with lambda"):
  prints the "Sorting with lambda" header and underline.
- names = ["alice", "Bob", "charlie", "dave"]:
  creates a list of names with mixed case.
- print("case-insensitive:", sorted(names, key=lambda s: s.lower())):
  outputs: case-insensitive: ['alice', 'Bob', 'charlie', 'dave']
- people = [{...}, {...}, {...}]:
  creates a list of dicts with name and age.
- print("sorted by age:", sorted(people, key=lambda p: p["age"])):
  outputs list ordered by age: Bob, Charlie, Alice.
"""


NOTES = """  # Store study notes as a multiline string.
Notes:
- Lambdas are best for short, single-expression functions.
- Prefer def for complex logic or when you need a docstring.
- map/filter can be replaced by comprehensions for readability.
"""


QUESTIONS = """  # Store practice questions as a multiline string.
Questions:
1) When would you choose a lambda over a def?
2) Rewrite a map call as a list comprehension.
3) What does reduce do, and what is its initial value?
4) How would you sort strings by length using lambda?
5) What is a closure, and how does function_builder create one?
"""


def main():  # Define the script entry point.
    basic_lambda()  # Run the basic lambda demo.
    closures_with_lambda()  # Run the closure demo.
    map_filter_reduce()  # Run map/filter/reduce demo.
    sorting_with_lambda()  # Run the sorting demo.

    print(NOTES.strip())  # Print notes without extra whitespace.
    print()  # Print a blank line between notes and questions.
    print(QUESTIONS.strip())  # Print questions for review.


EXAMPLE_WALKTHROUGH_MAIN = """  # Store a walkthrough for main.
Example Walkthrough: main
- basic_lambda():
  runs the basic lambda section.
- closures_with_lambda():
  runs the closures section.
- map_filter_reduce():
  runs the map/filter/reduce section.
- sorting_with_lambda():
  runs the sorting section.
- print(NOTES.strip()):
  prints the Notes block.
- print():
  prints a blank line.
- print(QUESTIONS.strip()):
  prints the Questions block.
"""


if __name__ == "__main__":  # Run main only when executed directly.
    main()  # Invoke the entry point.
