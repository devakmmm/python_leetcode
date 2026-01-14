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


EXAMPLE_WALKTHROUGH_BASIC = """  # Store a walkthrough for basic_example.
Example Walkthrough: basic_example
- show_section("Basic usage"):
  prints the "Basic usage" header and underline.
- meaning = 42:
  sets meaning to 42.
- message = "greater than 10" if meaning > 10 else "10 or less":
  chooses "greater than 10" because 42 > 10.
- print("meaning:", meaning, "message:", message):
  outputs: meaning: 42 message: greater than 10
"""


def choose_value():  # Define a demo for selecting a value.
    show_section("Choose a value")  # Display the section header.
    score = 87  # Assign a score for grading.
    grade = "pass" if score >= 60 else "fail"  # Choose pass or fail.
    print("score:", score, "grade:", grade)  # Print the outcome.


EXAMPLE_WALKTHROUGH_CHOOSE = """  # Store a walkthrough for choose_value.
Example Walkthrough: choose_value
- show_section("Choose a value"):
  prints the "Choose a value" header and underline.
- score = 87:
  sets score to 87.
- grade = "pass" if score >= 60 else "fail":
  chooses "pass" because 87 >= 60.
- print("score:", score, "grade:", grade):
  outputs: score: 87 grade: pass
"""


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


EXAMPLE_WALKTHROUGH_MAIN = """  # Store a walkthrough for main.
Example Walkthrough: main
- basic_example():
  runs the basic usage section.
- choose_value():
  runs the choose value section.
- print(NOTES.strip()):
  prints the Notes block.
- print():
  prints a blank line.
- print(QUESTIONS.strip()):
  prints the Questions block.
"""


if __name__ == "__main__":  # Run main only when executed directly.
    main()  # Invoke the entry point.
