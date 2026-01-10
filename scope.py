"""
scope.py - Variable scope and the LEGB rule.

Learning goals:
- Local, Enclosing, Global, Built-in (LEGB)
- Using nonlocal and global
"""


def show_section(title):
    print("\n" + title)
    print("-" * len(title))


def local_and_global():
    show_section("Local and global")
    color = "red"

    def inner():
        local_color = "blue"
        print("inner local_color:", local_color)

    inner()
    print("outer color:", color)


def nonlocal_example():
    show_section("nonlocal")
    color = "red"

    def outer():
        color = "green"

        def inner():
            nonlocal color
            color = "blue"
            print("inner color:", color)

        inner()
        print("outer color:", color)

    outer()


def global_example():
    show_section("global")
    counter = {"value": 0}

    def increment():
        counter["value"] += 1
        print("counter:", counter["value"])

    increment()
    increment()


NOTES = """
Notes:
- Python resolves names using LEGB: Local, Enclosing, Global, Built-in.
- nonlocal rebinds variables in the nearest enclosing scope.
- global rebinds variables at module scope (use sparingly).
"""


QUESTIONS = """
Questions:
1) What is the LEGB lookup order?
2) When do you need nonlocal?
3) Why is global often discouraged?
4) What is the difference between rebinding a name and mutating an object?
"""


def main():
    local_and_global()
    nonlocal_example()
    global_example()

    print(NOTES.strip())
    print()
    print(QUESTIONS.strip())


if __name__ == "__main__":
    main()
