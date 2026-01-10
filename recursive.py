"""
recursive.py - Recursion basics in Python.

Learning goals:
- Base case vs recursive case
- Tracing recursive calls
- Recognizing when recursion is appropriate
"""


def show_section(title):
    print("\n" + title)
    print("-" * len(title))


def add_one(num):
    if num >= 9:
        return num + 1
    total = num + 1
    print("Current total:", total)
    return add_one(total)


def factorial(n):
    if n < 0:
        raise ValueError("n must be >= 0")
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)


def sum_list(nums):
    if not nums:
        return 0
    return nums[0] + sum_list(nums[1:])


NOTES = """
Notes:
- Every recursive function needs a base case to stop.
- Recursion can be elegant but may hit recursion limits for large inputs.
- Iterative solutions are often more memory-efficient.
"""


QUESTIONS = """
Questions:
1) What is the base case in factorial?
2) What happens if you remove the base case from add_one?
3) How would you rewrite sum_list iteratively?
4) Why does recursion use more memory than a loop?
"""


def main():
    show_section("add_one demo")
    result = add_one(5)
    print("Final result:", result)

    show_section("factorial demo")
    print("factorial(5):", factorial(5))

    show_section("sum_list demo")
    print("sum_list([1, 2, 3, 4]):", sum_list([1, 2, 3, 4]))

    print(NOTES.strip())
    print()
    print(QUESTIONS.strip())


if __name__ == "__main__":
    main()
