"""
functions.py - Defining and calling functions in Python.

Learning goals:
- Define functions and return values
- Default arguments and keyword arguments
- *args and **kwargs
- Basic input validation
"""


def show_section(title):  # Define a helper to label output sections.
    print("\n" + title)  # Print a blank line and the section title.
    print("-" * len(title))  # Print a line of dashes matching title length.


def hello():  # Define a simple greeting function.
    print("Hello, World!")  # Output a greeting to the console.


def sum_numbers(a, b):  # Define a function that sums two numbers.
    if not isinstance(a, int) or not isinstance(b, int):  # Validate inputs are ints.
        return None  # Return None to signal invalid input types.
    return a + b  # Return the sum of the two integers.


def greet(name="friend", punctuation="!"):  # Define a function with default args.
    return f"Hello, {name}{punctuation}"  # Build and return a greeting.


def multiple_items(*args):  # Define a function that accepts variable args.
    print("args tuple:", args)  # Print the collected positional arguments.


def keyword_arguments(**kwargs):  # Define a function that accepts keyword args.
    print("kwargs dict:", kwargs)  # Print the collected keyword arguments.


def functions_demo():  # Define a demo that calls basic functions.
    show_section("Basic functions")  # Print the section header.
    hello()  # Call the greeting function.

    result = sum_numbers(5, 10)  # Compute a valid sum.
    print("sum_numbers(5, 10):", result)  # Show the valid result.
    print("sum_numbers('5', 10):", sum_numbers("5", 10))  # Show invalid input.

    print(greet())  # Call greet with defaults.
    print(greet("Alice", "?"))  # Call greet with custom args.


def args_kwargs_demo():  # Define a demo for *args and **kwargs.
    show_section("*args and **kwargs")  # Print the section header.
    multiple_items(1, 2, 3, "Hello", True)  # Pass mixed positional args.
    keyword_arguments(name="Alice", age=30, city="New York")  # Pass keywords.


NOTES = """  # Store study notes as a multiline string.
Notes:
- A function without an explicit return returns None.
- Default arguments are evaluated at function definition time.
- Use *args for variable positional arguments, **kwargs for keyword arguments.
"""


QUESTIONS = """  # Store practice questions as a multiline string.
Questions:
1) Why does sum_numbers return None for invalid types?
2) What is the difference between parameters and arguments?
3) How would you make greet require a keyword-only argument?
4) What happens if you pass the same key twice in **kwargs?
5) What is a common pitfall with mutable default arguments?
"""


def main():  # Define the script entry point.
    functions_demo()  # Run the basic functions demo.
    args_kwargs_demo()  # Run the *args/**kwargs demo.

    print(NOTES.strip())  # Print the notes block without extra whitespace.
    print()  # Print a blank line between notes and questions.
    print(QUESTIONS.strip())  # Print the questions block.


if __name__ == "__main__":  # Run main only when executed directly.
    main()  # Invoke the entry point.
