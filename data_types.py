"""
data_types.py - Core Python data types and conversions.

Learning goals:
- Strings: literals, slicing, methods, immutability
- Numbers: int/float, arithmetic, rounding
- Booleans and comparisons
- None and truthiness
- Converting between types
- math module highlights
"""

import math  # Import the standard math module.


def show_section(title):  # Define a helper to label output sections.
    print("\n" + title)  # Print a blank line and the section title.
    print("-" * len(title))  # Print a dashed underline under the title.


def string_examples():  # Define a demo for string usage.
    show_section("Strings")  # Display the section header.
    first = "dev"  # Assign a string literal.
    last = str("ops")  # Use the str constructor for a string.
    full = first + " " + last  # Concatenate strings with a space.

    print("full:", full)  # Print the combined string.
    print("type(full):", type(full))  # Show the type of the string.
    print("f-string:", f"{first} works in {last}")  # Format using f-string.

    multiline = """This is a multiline string.
It can span multiple lines."""  # Define a multiline string literal.
    print("multiline:\n" + multiline)  # Print the multiline string.

    escaped = "She said, \"Hello!\""  # Use escape characters in a string.
    print("escaped:", escaped)  # Print the escaped string.

    print("index 0:", full[0])  # Access the first character.
    print("last char:", full[-1])  # Access the last character.
    print("slice [0:3]:", full[0:3])  # Slice the first three characters.
    print("slice [4:]:", full[4:])  # Slice from index 4 to the end.

    print("upper:", full.upper())  # Convert to uppercase.
    print("lower:", full.lower())  # Convert to lowercase.
    print("title:", full.title())  # Convert to title case.
    print("replace:", full.replace("dev", "devops"))  # Replace a substring.
    print("startswith 'de':", full.startswith("de"))  # Check prefix.
    print("endswith 'ops':", full.endswith("ops"))  # Check suffix.
    print("find 'op':", full.find("op"))  # Find substring index.
    print("split on space:", full.split(" "))  # Split on spaces.
    print("join:", "-".join(["a", "b", "c"]))  # Join a list with a separator.
    print("strip:", "  spaced  ".strip())  # Trim surrounding whitespace.

    original = "immutable"  # Store an original string.
    changed = original.replace("table", "table-ish")  # Create a new string.
    print("original:", original)  # Show the original string.
    print("changed:", changed)  # Show the changed string.


def numeric_examples():  # Define a demo for numeric operations.
    show_section("Numbers")  # Display the section header.
    a = 10  # Assign an integer.
    b = 3  # Assign another integer.
    pi = 3.14159  # Assign a float.

    print("a + b:", a + b)  # Add two numbers.
    print("a - b:", a - b)  # Subtract two numbers.
    print("a * b:", a * b)  # Multiply two numbers.
    print("a / b:", a / b)  # Divide two numbers.
    print("a // b:", a // b)  # Integer division.
    print("a % b:", a % b)  # Modulo operation.
    print("a ** b:", a ** b)  # Exponentiation.

    print("abs(-5):", abs(-5))  # Compute absolute value.
    print("round(pi):", round(pi))  # Round to nearest int.
    print("round(pi, 2):", round(pi, 2))  # Round to two decimals.
    print("pow(2, 3):", pow(2, 3))  # Raise 2 to the power of 3.

    print("math.sqrt(16):", math.sqrt(16))  # Compute square root.
    print("math.factorial(5):", math.factorial(5))  # Compute factorial.
    print("math.pi:", math.pi)  # Print the constant pi.
    print("math.ceil(3.14):", math.ceil(3.14))  # Round up.
    print("math.floor(3.14):", math.floor(3.14))  # Round down.


def boolean_examples():  # Define a demo for booleans and comparisons.
    show_section("Booleans and comparisons")  # Display the section header.
    print("True and False:", True, False)  # Print boolean literals.
    print("5 > 3:", 5 > 3)  # Compare greater than.
    print("5 == 3:", 5 == 3)  # Compare equality.
    print("5 != 3:", 5 != 3)  # Compare inequality.
    print("True and False:", True and False)  # Logical AND.
    print("True or False:", True or False)  # Logical OR.
    print("not True:", not True)  # Logical NOT.

    print("bool(1):", bool(1))  # Convert 1 to True.
    print("bool(0):", bool(0))  # Convert 0 to False.
    print("bool(''):", bool(""))  # Convert empty string to False.
    print("bool('text'):", bool("text"))  # Convert non-empty string to True.
    print("bool([]):", bool([]))  # Convert empty list to False.
    print("bool([0]):", bool([0]))  # Convert non-empty list to True.


def none_and_casting():  # Define a demo for None and casting.
    show_section("None and type conversion")  # Display the section header.
    value = None  # Assign the None singleton.
    print("value is None:", value is None)  # Check None with is.

    decade = str(2020)  # Cast an int to a string.
    print("decade as str:", decade, type(decade))  # Show value and type.

    number_str = "42"  # Define a numeric string.
    number_int = int(number_str)  # Convert string to int.
    print("int('42'):", number_int, type(number_int))  # Show int and type.

    float_str = "3.14"  # Define a float string.
    number_float = float(float_str)  # Convert string to float.
    print("float('3.14'):", number_float, type(number_float))  # Show float and type.

    try:  # Start a protected block for invalid conversion.
        int("not-a-number")  # Attempt a failing conversion.
    except ValueError as exc:  # Catch the conversion error.
        print("int conversion failed:", exc)  # Report the error message.


NOTES = """  # Store study notes as a multiline string.
Notes:
- Strings are immutable; methods like replace return a new string.
- Integer division (//) drops the remainder, modulo (%) keeps it.
- bool(x) uses truthiness; empty containers are False.
- None is a singleton used to represent "no value".
"""


QUESTIONS = """  # Store practice questions as a multiline string.
Questions:
1) What is the difference between / and // for integers?
2) Why does "abc".upper() not modify the original string?
3) What values are considered falsy in Python?
4) How would you safely convert a string to int if it might be invalid?
5) What is the difference between is and == for None checks?
6) How do you format a float to 2 decimal places with an f-string?
7) When would you use math.floor vs round?
8) What is the output of bool([0]) and why?
"""


def main():  # Define the script entry point.
    string_examples()  # Run the string examples.
    numeric_examples()  # Run the numeric examples.
    boolean_examples()  # Run the boolean examples.
    none_and_casting()  # Run the None and casting examples.

    print(NOTES.strip())  # Print notes without extra whitespace.
    print()  # Print a blank line between notes and questions.
    print(QUESTIONS.strip())  # Print questions for review.


if __name__ == "__main__":  # Run main only when executed directly.
    main()  # Invoke the entry point.
