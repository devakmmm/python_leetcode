"""
ternaryoperator.py - Conditional expressions in Python.

Learning goals:
- Use the ternary operator for concise conditions
- Compare with if/else blocks
"""


def show_section(title):
    print("\n" + title)
    print("-" * len(title))


def basic_example():
    show_section("Basic usage")
    meaning = 42
    message = "greater than 10" if meaning > 10 else "10 or less"
    print("meaning:", meaning, "message:", message)


def choose_value():
    show_section("Choose a value")
    score = 87
    grade = "pass" if score >= 60 else "fail"
    print("score:", score, "grade:", grade)


NOTES = """
Notes:
- A conditional expression is: value_if_true if condition else value_if_false.
- Prefer if/else statements when logic becomes complex.
"""


QUESTIONS = """
Questions:
1) What is the result of "yes" if 0 else "no" and why?
2) When would a full if/else be clearer than a ternary expression?
3) Can you nest ternary expressions, and should you?
"""


def main():
    basic_example()
    choose_value()
    print(NOTES.strip())
    print()
    print(QUESTIONS.strip())


if __name__ == "__main__":
    main()
