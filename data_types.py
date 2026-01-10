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

import math


def show_section(title):
    print("\n" + title)
    print("-" * len(title))


def string_examples():
    show_section("Strings")
    first = "dev"
    last = str("ops")
    full = first + " " + last

    print("full:", full)
    print("type(full):", type(full))
    print("f-string:", f"{first} works in {last}")

    multiline = """This is a multiline string.
It can span multiple lines."""
    print("multiline:\n" + multiline)

    escaped = "She said, \"Hello!\""
    print("escaped:", escaped)

    print("index 0:", full[0])
    print("last char:", full[-1])
    print("slice [0:3]:", full[0:3])
    print("slice [4:]:", full[4:])

    print("upper:", full.upper())
    print("lower:", full.lower())
    print("title:", full.title())
    print("replace:", full.replace("dev", "devops"))
    print("startswith 'de':", full.startswith("de"))
    print("endswith 'ops':", full.endswith("ops"))
    print("find 'op':", full.find("op"))
    print("split on space:", full.split(" "))
    print("join:", "-".join(["a", "b", "c"]))
    print("strip:", "  spaced  ".strip())

    original = "immutable"
    changed = original.replace("table", "table-ish")
    print("original:", original)
    print("changed:", changed)


def numeric_examples():
    show_section("Numbers")
    a = 10
    b = 3
    pi = 3.14159

    print("a + b:", a + b)
    print("a - b:", a - b)
    print("a * b:", a * b)
    print("a / b:", a / b)
    print("a // b:", a // b)
    print("a % b:", a % b)
    print("a ** b:", a ** b)

    print("abs(-5):", abs(-5))
    print("round(pi):", round(pi))
    print("round(pi, 2):", round(pi, 2))
    print("pow(2, 3):", pow(2, 3))

    print("math.sqrt(16):", math.sqrt(16))
    print("math.factorial(5):", math.factorial(5))
    print("math.pi:", math.pi)
    print("math.ceil(3.14):", math.ceil(3.14))
    print("math.floor(3.14):", math.floor(3.14))


def boolean_examples():
    show_section("Booleans and comparisons")
    print("True and False:", True, False)
    print("5 > 3:", 5 > 3)
    print("5 == 3:", 5 == 3)
    print("5 != 3:", 5 != 3)
    print("True and False:", True and False)
    print("True or False:", True or False)
    print("not True:", not True)

    print("bool(1):", bool(1))
    print("bool(0):", bool(0))
    print("bool(''):", bool(""))
    print("bool('text'):", bool("text"))
    print("bool([]):", bool([]))
    print("bool([0]):", bool([0]))


def none_and_casting():
    show_section("None and type conversion")
    value = None
    print("value is None:", value is None)

    decade = str(2020)
    print("decade as str:", decade, type(decade))

    number_str = "42"
    number_int = int(number_str)
    print("int('42'):", number_int, type(number_int))

    float_str = "3.14"
    number_float = float(float_str)
    print("float('3.14'):", number_float, type(number_float))

    try:
        int("not-a-number")
    except ValueError as exc:
        print("int conversion failed:", exc)


NOTES = """
Notes:
- Strings are immutable; methods like replace return a new string.
- Integer division (//) drops the remainder, modulo (%) keeps it.
- bool(x) uses truthiness; empty containers are False.
- None is a singleton used to represent "no value".
"""


QUESTIONS = """
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


def main():
    string_examples()
    numeric_examples()
    boolean_examples()
    none_and_casting()

    print(NOTES.strip())
    print()
    print(QUESTIONS.strip())


if __name__ == "__main__":
    main()
