"""
scope.py - Variable scope and the LEGB rule.

Learning goals:
- Local, Enclosing, Global, Built-in (LEGB)
- Using nonlocal and global
"""


def show_section(title):  # Define a helper to label output sections.
    print("\n" + title)  # Print a blank line and the section title.
    print("-" * len(title))  # Print a dashed underline under the title.


def local_and_global():  # Define a demo for local vs global scope.
    show_section("Local and global")  # Display the section header.
    color = "red"  # Define a local variable in this function.

    def inner():  # Define an inner function with its own scope.
        local_color = "blue"  # Create a variable local to inner.
        print("inner local_color:", local_color)  # Print inner's local value.

    inner()  # Call the inner function.
    print("outer color:", color)  # Print the outer variable.


EXAMPLE_WALKTHROUGH_LOCAL = """  # Store a walkthrough for local_and_global.
Example Walkthrough: local_and_global
- show_section("Local and global"):
  prints the "Local and global" header and underline.
- color = "red":
  sets a local variable in local_and_global.
- def inner():
  defines an inner function with its own scope.
- local_color = "blue":
  sets a variable local to inner.
- print("inner local_color:", local_color):
  outputs: inner local_color: blue
- inner():
  calls the inner function.
- print("outer color:", color):
  outputs: outer color: red
"""


def nonlocal_example():  # Define a demo for nonlocal usage.
    show_section("nonlocal")  # Display the section header.
    color = "red"  # Define an outer-scope variable.

    def outer():  # Define an enclosing function.
        color = "green"  # Shadow the outer variable.

        def inner():  # Define an inner function.
            nonlocal color  # Rebind the enclosing color variable.
            color = "blue"  # Update the enclosing variable.
            print("inner color:", color)  # Print the updated value.

        inner()  # Call the inner function.
        print("outer color:", color)  # Print the modified enclosing value.

    outer()  # Call the enclosing function.


EXAMPLE_WALKTHROUGH_NONLOCAL = """  # Store a walkthrough for nonlocal_example.
Example Walkthrough: nonlocal_example
- show_section("nonlocal"):
  prints the "nonlocal" header and underline.
- color = "red":
  sets a variable in nonlocal_example scope.
- def outer():
  defines an enclosing function.
- color = "green":
  shadows the outer variable inside outer.
- def inner():
  defines an inner function.
- nonlocal color:
  allows inner to rebind outer's color.
- color = "blue":
  changes color in the enclosing scope.
- print("inner color:", color):
  outputs: inner color: blue
- print("outer color:", color):
  outputs: outer color: blue
"""


def global_example():  # Define a demo that mutates a global-like object.
    show_section("global")  # Display the section header.
    counter = {"value": 0}  # Use a dict to mutate without global.

    def increment():  # Define a function that updates the counter.
        counter["value"] += 1  # Increment the stored counter value.
        print("counter:", counter["value"])  # Print the updated value.

    increment()  # Call increment once.
    increment()  # Call increment again.


EXAMPLE_WALKTHROUGH_GLOBAL = """  # Store a walkthrough for global_example.
Example Walkthrough: global_example
- show_section("global"):
  prints the "global" header and underline.
- counter = {"value": 0}:
  creates a dict used as a mutable counter.
- def increment():
  defines a function that mutates the dict.
- counter["value"] += 1:
  increments the counter value.
- print("counter:", counter["value"]):
  outputs the updated count.
- increment():
  outputs: counter: 1
- increment():
  outputs: counter: 2
"""


NOTES = """  # Store study notes as a multiline string.
Notes:
- Python resolves names using LEGB: Local, Enclosing, Global, Built-in.
- nonlocal rebinds variables in the nearest enclosing scope.
- global rebinds variables at module scope (use sparingly).
"""


QUESTIONS = """  # Store practice questions as a multiline string.
Questions:
1) What is the LEGB lookup order?
2) When do you need nonlocal?
3) Why is global often discouraged?
4) What is the difference between rebinding a name and mutating an object?
"""


def main():  # Define the script entry point.
    local_and_global()  # Run the local/global demo.
    nonlocal_example()  # Run the nonlocal demo.
    global_example()  # Run the global demo.

    print(NOTES.strip())  # Print notes without extra whitespace.
    print()  # Print a blank line between notes and questions.
    print(QUESTIONS.strip())  # Print questions for review.


EXAMPLE_WALKTHROUGH_MAIN = """  # Store a walkthrough for main.
Example Walkthrough: main
- local_and_global():
  runs the local vs global example.
- nonlocal_example():
  runs the nonlocal example.
- global_example():
  runs the global example.
- print(NOTES.strip()):
  prints the Notes block.
- print():
  prints a blank line.
- print(QUESTIONS.strip()):
  prints the Questions block.
"""


if __name__ == "__main__":  # Run main only when executed directly.
    main()  # Invoke the entry point.
