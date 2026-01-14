"""
hello.py - A minimal Python program.

Learning goals:
- Variables and simple output
- Basic function usage
"""


def greet(name):  # Define a function that returns a greeting.
    return f"Hello, {name}!"  # Build and return the greeting string.


EXAMPLE_WALKTHROUGH_GREET = """  # Store a walkthrough for greet.
Example Walkthrough: greet
- def greet(name):
  defines a function that accepts a name string.
- return f"Hello, {name}!":
  returns a greeting with the name inserted.
Example usage:
- greet("world") returns "Hello, world!"
"""


def main():  # Define the main entry point for this script.
    greeting = "hello"  # Store a simple greeting message.
    print("greeting:", greeting)  # Print the greeting with a label.
    print(greet("world"))  # Call greet and print the returned string.


EXAMPLE_WALKTHROUGH_MAIN = """  # Store a walkthrough for main.
Example Walkthrough: main
- greeting = "hello":
  sets greeting to "hello".
- print("greeting:", greeting):
  outputs: greeting: hello
- print(greet("world")):
  outputs: Hello, world!
"""


if __name__ == "__main__":  # Run only when executed directly.
    main()  # Invoke the main function.
