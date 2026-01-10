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


def closures_with_lambda():  # Define a demo for lambda closures.
    show_section("Closures with lambda")  # Display the section header.

    def function_builder(x):  # Define a factory function that closes over x.
        return lambda num: x + num  # Return a lambda that adds x to num.

    add_five = function_builder(5)  # Build a closure that adds five.
    subtract_three = function_builder(-3)  # Build a closure that subtracts three.
    print("add_five(10):", add_five(10))  # Use the closure.
    print("subtract_three(10):", subtract_three(10))  # Use the closure.


def map_filter_reduce():  # Define a demo for map, filter, and reduce.
    show_section("map, filter, reduce")  # Display the section header.
    numbers = [1, 2, 3, 4, 5]  # Create a list of numbers.
    squared_numbers = list(map(lambda n: n * n, numbers))  # Map to squares.
    odd_numbers = list(filter(lambda n: n % 2 != 0, numbers))  # Filter odds.
    total = reduce(lambda acc, curr: acc + curr, numbers)  # Reduce to a sum.

    print("squared_numbers:", squared_numbers)  # Show mapped results.
    print("odd_numbers:", odd_numbers)  # Show filtered results.
    print("total:", total)  # Show reduced result.


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


if __name__ == "__main__":  # Run main only when executed directly.
    main()  # Invoke the entry point.
