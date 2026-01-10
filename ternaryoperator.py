"""
ternaryoperator.py - Conditional expressions in Python.

Learning goals:
- Use the ternary operator for concise conditions
- Compare with if/else blocks
"""


def show_section(title):  # Define a helper to label output sections.
    print("\n" + title)  # Print a blank line and the section title.
    print("-" * len(title))  # Print a dashed underline under the title.


def basic_example():  # Define a demo for basic ternary usage.
    show_section("Basic usage")  # Display the section header.
    meaning = 42  # Assign a numeric value to test.
    message = "greater than 10" if meaning > 10 else "10 or less"  # Choose a message.
    print("meaning:", meaning, "message:", message)  # Print the result.


def choose_value():  # Define a demo for selecting a value.
    show_section("Choose a value")  # Display the section header.
    score = 87  # Assign a score for grading.
    grade = "pass" if score >= 60 else "fail"  # Choose pass or fail.
    print("score:", score, "grade:", grade)  # Print the outcome.


NOTES = """  # Store study notes as a multiline string.
Notes:
- A conditional expression is: value_if_true if condition else value_if_false.
- Prefer if/else statements when logic becomes complex.
"""


QUESTIONS = """  # Store practice questions as a multiline string.
Questions:
1) What is the result of "yes" if 0 else "no" and why?
2) When would a full if/else be clearer than a ternary expression?
3) Can you nest ternary expressions, and should you?
"""


def main():  # Define the script entry point.
    basic_example()  # Run the basic ternary demo.
    choose_value()  # Run the value selection demo.
    print(NOTES.strip())  # Print notes without extra whitespace.
    print()  # Print a blank line between notes and questions.
    print(QUESTIONS.strip())  # Print questions for review.


if __name__ == "__main__":  # Run main only when executed directly.
    main()  # Invoke the entry point.
