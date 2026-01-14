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


EXAMPLE_WALKTHROUGH_HELLO = """  # Store a walkthrough for hello.
Example Walkthrough: hello
- print("Hello, World!"):
  outputs: Hello, World!
"""


def sum_numbers(a, b):  # Define a function that sums two numbers.
    if not isinstance(a, int) or not isinstance(b, int):  # Validate inputs are ints.
        return None  # Return None to signal invalid input types.
    return a + b  # Return the sum of the two integers.


EXAMPLE_WALKTHROUGH_SUM_NUMBERS = """  # Store a walkthrough for sum_numbers.
Example Walkthrough: sum_numbers
- if not isinstance(a, int) or not isinstance(b, int):
  checks both inputs are integers.
- return None:
  returns None for invalid types.
- return a + b:
  returns the integer sum.
Example usage:
- sum_numbers(5, 10) returns 15.
- sum_numbers("5", 10) returns None.
"""


def greet(name="friend", punctuation="!"):  # Define a function with default args.
    return f"Hello, {name}{punctuation}"  # Build and return a greeting.


EXAMPLE_WALKTHROUGH_GREET = """  # Store a walkthrough for greet.
Example Walkthrough: greet
- return f"Hello, {name}{punctuation}":
  returns a greeting string.
Example usage:
- greet() returns "Hello, friend!"
- greet("Alice", "?") returns "Hello, Alice?"
"""


def multiple_items(*args):  # Define a function that accepts variable args.
    print("args tuple:", args)  # Print the collected positional arguments.


EXAMPLE_WALKTHROUGH_MULTIPLE_ITEMS = """  # Store a walkthrough for multiple_items.
Example Walkthrough: multiple_items
- *args collects all positional arguments into a tuple.
- print("args tuple:", args):
  prints the tuple of arguments.
Example usage:
- multiple_items(1, 2, "a") outputs: args tuple: (1, 2, 'a')
"""


def keyword_arguments(**kwargs):  # Define a function that accepts keyword args.
    print("kwargs dict:", kwargs)  # Print the collected keyword arguments.


EXAMPLE_WALKTHROUGH_KEYWORD_ARGUMENTS = """  # Store a walkthrough for keyword_arguments.
Example Walkthrough: keyword_arguments
- **kwargs collects keyword arguments into a dict.
- print("kwargs dict:", kwargs):
  prints the dict of keyword arguments.
Example usage:
- keyword_arguments(name="Alice", age=30) outputs: kwargs dict: {'name': 'Alice', 'age': 30}
"""


def functions_demo():  # Define a demo that calls basic functions.
    show_section("Basic functions")  # Print the section header.
    hello()  # Call the greeting function.

    result = sum_numbers(5, 10)  # Compute a valid sum.
    print("sum_numbers(5, 10):", result)  # Show the valid result.
    print("sum_numbers('5', 10):", sum_numbers("5", 10))  # Show invalid input.

    print(greet())  # Call greet with defaults.
    print(greet("Alice", "?"))  # Call greet with custom args.


EXAMPLE_WALKTHROUGH_FUNCTIONS_DEMO = """  # Store a walkthrough for functions_demo.
Example Walkthrough: functions_demo
- show_section("Basic functions"):
  prints the "Basic functions" header and underline.
- hello():
  outputs: Hello, World!
- result = sum_numbers(5, 10):
  sets result to 15.
- print("sum_numbers(5, 10):", result):
  outputs: sum_numbers(5, 10): 15
- print("sum_numbers('5', 10):", sum_numbers("5", 10)):
  outputs: sum_numbers('5', 10): None
- print(greet()):
  outputs: Hello, friend!
- print(greet("Alice", "?")):
  outputs: Hello, Alice?
"""


def args_kwargs_demo():  # Define a demo for *args and **kwargs.
    show_section("*args and **kwargs")  # Print the section header.
    multiple_items(1, 2, 3, "Hello", True)  # Pass mixed positional args.
    keyword_arguments(name="Alice", age=30, city="New York")  # Pass keywords.


EXAMPLE_WALKTHROUGH_ARGS_KWARGS = """  # Store a walkthrough for args_kwargs_demo.
Example Walkthrough: args_kwargs_demo
- show_section("*args and **kwargs"):
  prints the "*args and **kwargs" header and underline.
- multiple_items(1, 2, 3, "Hello", True):
  outputs: args tuple: (1, 2, 3, 'Hello', True)
- keyword_arguments(name="Alice", age=30, city="New York"):
  outputs: kwargs dict: {'name': 'Alice', 'age': 30, 'city': 'New York'}
"""


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


EXAMPLE_WALKTHROUGH_MAIN = """  # Store a walkthrough for main.
Example Walkthrough: main
- functions_demo():
  runs the basic functions section.
- args_kwargs_demo():
  runs the *args and **kwargs section.
- print(NOTES.strip()):
  prints the Notes block.
- print():
  prints a blank line.
- print(QUESTIONS.strip()):
  prints the Questions block.
"""


if __name__ == "__main__":  # Run main only when executed directly.
    main()  # Invoke the entry point.
