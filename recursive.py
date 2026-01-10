"""
recursive.py - Recursion basics in Python.

Learning goals:
- Base case vs recursive case
- Tracing recursive calls
- Recognizing when recursion is appropriate
"""


def show_section(title):  # Define a helper to label output sections.
    print("\n" + title)  # Print a blank line and the section title.
    print("-" * len(title))  # Print a dashed underline under the title.


def add_one(num):  # Define a recursive function that increments to 9.
    if num >= 9:  # Check the base case to stop recursion.
        return num + 1  # Return the final incremented value.
    total = num + 1  # Compute the next total.
    print("Current total:", total)  # Show progress for tracing.
    return add_one(total)  # Recurse with the updated value.


def factorial(n):  # Define a factorial function using recursion.
    if n < 0:  # Reject negative inputs.
        raise ValueError("n must be >= 0")  # Signal invalid input.
    if n in (0, 1):  # Check base cases.
        return 1  # Return 1 for 0! and 1!.
    return n * factorial(n - 1)  # Recurse to compute n!.


def sum_list(nums):  # Define a recursive sum for a list.
    if not nums:  # Check for the empty list base case.
        return 0  # Sum of empty list is 0.
    return nums[0] + sum_list(nums[1:])  # Add head to recursive sum of tail.


NOTES = """  # Store study notes as a multiline string.
Notes:
- Every recursive function needs a base case to stop.
- Recursion can be elegant but may hit recursion limits for large inputs.
- Iterative solutions are often more memory-efficient.
"""


QUESTIONS = """  # Store practice questions as a multiline string.
Questions:
1) What is the base case in factorial?
2) What happens if you remove the base case from add_one?
3) How would you rewrite sum_list iteratively?
4) Why does recursion use more memory than a loop?
"""


def main():  # Define the script entry point.
    show_section("add_one demo")  # Display a demo header.
    result = add_one(5)  # Call the recursive add_one function.
    print("Final result:", result)  # Print the final result.

    show_section("factorial demo")  # Display a demo header.
    print("factorial(5):", factorial(5))  # Compute factorial of 5.

    show_section("sum_list demo")  # Display a demo header.
    print("sum_list([1, 2, 3, 4]):", sum_list([1, 2, 3, 4]))  # Sum a list.

    print(NOTES.strip())  # Print notes without extra whitespace.
    print()  # Print a blank line between notes and questions.
    print(QUESTIONS.strip())  # Print questions for review.


if __name__ == "__main__":  # Run main only when executed directly.
    main()  # Invoke the entry point.
