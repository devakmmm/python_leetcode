"""
lists.py - Guided examples for Python lists and tuples.

Learning goals:
- Membership tests, indexing, and slicing
- List mutation methods and slice assignment
- Sorting vs sorted, shallow copies, and aliasing
- List concatenation, nesting, and comprehensions
- Tuple creation, unpacking, and immutability
"""


def show_section(title):
    print("\n" + title)
    print("-" * len(title))


def membership_and_indexing():
    show_section("Membership and indexing")
    users = ["dev", "ops", "admin"]
    data = ["23", "45", "devops"]

    print("users:", users)
    print("'dev' in users:", "dev" in users)
    print("'dev' not in users:", "dev" not in users)
    print("data:", data)
    print("'23' in data:", "23" in data)
    print("'devops' not in data:", "devops" not in data)

    print("last user:", users[-1])
    print("first data item:", data[0])
    print("users[1:3]:", users[1:3])
    print("data[:2]:", data[:2])
    print("users[1:]:", users[1:])
    print("data[-2:]:", data[-2:])
    print("users[:-1]:", users[:-1])


def mutation_examples():
    show_section("Mutation: append, insert, and slice assignment")
    users = ["dev", "ops", "admin"]

    users.append("guest")
    print("after append:", users)

    users.insert(1, "superuser")
    print("after insert:", users)

    users[2:2] = ["tester", "developer"]
    print("after slice insert:", users)

    users[1:3] = ["sysadmin"]
    print("after slice replace:", users)


def removal_examples():
    show_section("Removal: remove, pop, del, clear")
    users = ["dev", "ops", "admin", "guest"]

    if "dev" in users:
        users.remove("dev")
    print("after remove:", users)

    last = users.pop()
    print("popped:", last, "remaining:", users)

    del users[0]
    print("after del index 0:", users)

    users.clear()
    print("after clear:", users)


def extend_and_concat():
    show_section("Extend, concatenate, and nest lists")
    users = ["dev", "ops"]
    users.extend(["admin", "manager"])
    print("after extend:", users)

    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    combined = list1 + list2
    print("combined:", combined)

    nested = [users, list2]
    print("nested list:", nested)


def sort_and_reverse():
    show_section("Sorting and reversing")
    users = ["dev", "ops", "admin", "guest"]
    print("original:", users)
    print("sorted copy:", sorted(users))

    users.sort()
    print("sorted in place:", users)

    users.sort(reverse=True)
    print("sorted reverse:", users)

    users.sort(key=len)
    print("sorted by length:", users)

    users.reverse()
    print("reversed in place:", users)
    print("reversed copy:", list(reversed(users)))


def copy_and_alias():
    show_section("Copying vs aliasing (shallow copies)")
    users = ["dev", "ops", "admin"]
    alias = users
    copy1 = users.copy()
    copy2 = users[:]
    copy3 = list(users)

    users.append("guest")
    print("original:", users)
    print("alias:", alias)
    print("copy1:", copy1)
    print("copy2:", copy2)
    print("copy3:", copy3)


def plus_equals_demo():
    show_section("+= with lists")
    users = ["dev", "ops"]
    users += ["newuser"]
    print("+= list:", users)

    users = ["dev", "ops"]
    users += "newuser"
    print("+= string (each char added):", users)


def comprehension_examples():
    show_section("List comprehensions")
    squares = [n * n for n in range(1, 6)]
    print("squares:", squares)

    even_squares = [n * n for n in range(1, 11) if n % 2 == 0]
    print("even squares:", even_squares)

    upper_users = [name.upper() for name in ["dev", "ops", "admin"]]
    print("upper case:", upper_users)


def tuple_examples():
    show_section("Tuples")
    mytuple = ("dev", "ops", "admin")
    another_tuple = (1, 2, 3, 4, 5, 6, 7, 7)

    print("mytuple:", mytuple)
    print("another_tuple:", another_tuple)
    print("count of 7:", another_tuple.count(7))
    print("index of 3:", another_tuple.index(3))

    one, two, *three = another_tuple
    print("unpacked:", one, two, three)

    newlist = list(mytuple)
    newlist.append("guest")
    print("tuple -> list -> appended:", newlist)


NOTES = """
Notes:
- Lists are mutable dynamic arrays. Appending to the end is amortized O(1).
- Inserting or removing in the middle is O(n) because elements shift.
- Slicing creates a new list; slice assignment mutates the original list.
- list.sort() sorts in place and returns None; sorted() returns a new list.
- Copies are shallow; nested lists still share inner objects.
"""


QUESTIONS = """
Questions:
1) What does users[1:3] = ["sysadmin"] do to the list length, and why?
2) Explain the difference between append() and extend().
3) Why does users += "newuser" add characters instead of a single string?
4) Write a list comprehension that keeps only names longer than 3 characters.
5) How would you remove all occurrences of "dev" from a list?
6) What prints here, and why? list1 = [1, 2]; list2 = list1; list1.append(3)
7) How do you sort a list of dicts by a key like "age"?
8) When would you choose a tuple over a list?
9) What is the difference between reverse() and reversed()?
"""


def main():
    membership_and_indexing()
    mutation_examples()
    removal_examples()
    extend_and_concat()
    sort_and_reverse()
    copy_and_alias()
    plus_equals_demo()
    comprehension_examples()
    tuple_examples()

    print(NOTES.strip())
    print()
    print(QUESTIONS.strip())


if __name__ == "__main__":
    main()
