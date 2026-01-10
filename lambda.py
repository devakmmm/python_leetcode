"""
lambda.py - Anonymous functions (lambda) in Python.

Learning goals:
- Create lambdas for short, simple functions
- Use map, filter, and reduce
- Use lambdas for sorting keys
"""

from functools import reduce


def show_section(title):
    print("\n" + title)
    print("-" * len(title))


def basic_lambda():
    show_section("Basic lambda")
    squared = lambda num: num * num
    print("squared(5):", squared(5))

    def squared_def(num):
        return num * num

    print("squared_def(5):", squared_def(5))


def closures_with_lambda():
    show_section("Closures with lambda")
    def function_builder(x):
        return lambda num: x + num

    add_five = function_builder(5)
    subtract_three = function_builder(-3)
    print("add_five(10):", add_five(10))
    print("subtract_three(10):", subtract_three(10))


def map_filter_reduce():
    show_section("map, filter, reduce")
    numbers = [1, 2, 3, 4, 5]
    squared_numbers = list(map(lambda n: n * n, numbers))
    odd_numbers = list(filter(lambda n: n % 2 != 0, numbers))
    total = reduce(lambda acc, curr: acc + curr, numbers)

    print("squared_numbers:", squared_numbers)
    print("odd_numbers:", odd_numbers)
    print("total:", total)


def sorting_with_lambda():
    show_section("Sorting with lambda")
    names = ["alice", "Bob", "charlie", "dave"]
    print("case-insensitive:", sorted(names, key=lambda s: s.lower()))

    people = [
        {"name": "Alice", "age": 31},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 29},
    ]
    print("sorted by age:", sorted(people, key=lambda p: p["age"]))


NOTES = """
Notes:
- Lambdas are best for short, single-expression functions.
- Prefer def for complex logic or when you need a docstring.
- map/filter can be replaced by comprehensions for readability.
"""


QUESTIONS = """
Questions:
1) When would you choose a lambda over a def?
2) Rewrite a map call as a list comprehension.
3) What does reduce do, and what is its initial value?
4) How would you sort strings by length using lambda?
5) What is a closure, and how does function_builder create one?
"""


def main():
    basic_lambda()
    closures_with_lambda()
    map_filter_reduce()
    sorting_with_lambda()

    print(NOTES.strip())
    print()
    print(QUESTIONS.strip())


if __name__ == "__main__":
    main()
