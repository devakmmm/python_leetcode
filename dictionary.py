"""
dictionary.py - Dictionaries and sets review.

Learning goals:
- Create dictionaries with literals and dict()
- Access and update values safely
- Use common dictionary methods
- Loop with keys, values, items, and enumerate
- Create and operate on sets
- Review standard library imports and __name__ guard
"""

import math


def show_section(title):
    print("\n" + title)
    print("-" * len(title))


def dict_syntax_and_constructor():
    show_section("Dictionaries: literals and dict()")
    dictionary = {"key1": "value1", "key2": "value2"}
    print("literal:", dictionary)

    pizza = dict(
        [
            ("name", "Margherita Pizza"),
            ("price", 8.9),
            ("calories_per_slice", 250),
            ("toppings", ["mozzarella", "basil"]),
        ]
    )
    print("dict constructor:", pizza)
    print("bracket access:", pizza["name"])
    print("get with default:", pizza.get("total_time", 0))

    try:
        bad_key = [1, 2]
        bad_dict = {bad_key: "nope"}
        print(bad_dict)
    except TypeError as exc:
        print("list key error:", exc)

    ok_key = (1, 2)
    ok_dict = {ok_key: "tuple key ok"}
    print("tuple key:", ok_dict)


def dict_methods():
    show_section("Common dictionary methods")
    pizza = {
        "name": "Margherita Pizza",
        "price": 8.9,
        "calories_per_slice": 250,
    }

    keys_view = pizza.keys()
    values_view = pizza.values()
    items_view = pizza.items()
    print("keys view:", keys_view)
    print("values view:", values_view)
    print("items view:", items_view)

    pizza.update({"price": 15, "total_time": 25})
    print("after update:", pizza)
    print("keys after update:", list(keys_view))

    removed_price = pizza.pop("price", 10)
    print("pop price:", removed_price)

    try:
        pizza.pop("total_price")
    except KeyError as exc:
        print("pop missing key:", exc)

    last_key, last_value = pizza.popitem()
    print("popitem:", last_key, last_value)

    temp = {"a": 1, "b": 2}
    temp.clear()
    print("clear:", temp)


def dict_looping():
    show_section("Looping over dictionaries")
    products = {
        "Laptop": 990,
        "Smartphone": 600,
        "Tablet": 250,
        "Headphones": 70,
    }

    for price in products.values():
        print("value:", price)

    for product in products.keys():
        print("key:", product)

    for product in products:
        print("key (implicit):", product)

    for product in products.items():
        print("item tuple:", product)

    for product, price in products.items():
        print("item unpacked:", product, price)

    for index, item in enumerate(products.items()):
        print("enumerate:", index, item)

    for index, item in enumerate(products.items(), 1):
        print("enumerate start=1:", index, item)


def nested_dict_and_comprehension():
    show_section("Nested dictionaries and comprehensions")
    bands = {
        "The Beatles": {
            "members": ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Starr"],
            "genre": "Rock",
        },
        "Queen": {
            "members": ["Freddie Mercury", "Brian May", "Roger Taylor", "John Deacon"],
            "genre": "Rock",
        },
        "Nirvana": {
            "members": ["Kurt Cobain", "Krist Novoselic", "Dave Grohl"],
            "genre": "Grunge",
        },
    }

    print("Queen members:", bands["Queen"]["members"])
    member_counts = {name: len(data["members"]) for name, data in bands.items()}
    print("member counts:", member_counts)


def dict_copying():
    show_section("Copying vs aliasing (shallow copy)")
    original = {"a": 1, "b": {"nested": 2}}
    alias = original
    shallow = original.copy()

    original["a"] = 10
    original["b"]["nested"] = 99

    print("original:", original)
    print("alias:", alias)
    print("shallow:", shallow)


def set_basics():
    show_section("Sets: creation and methods")
    my_set = {1, 2, 3, 4, 5}
    empty_set = set()
    print("set literal:", my_set)
    print("empty set:", empty_set, type(empty_set))

    my_set.add(6)
    print("after add:", my_set)

    my_set.remove(4)
    print("after remove:", my_set)

    try:
        my_set.remove(42)
    except KeyError as exc:
        print("remove missing:", exc)

    my_set.discard(42)
    print("after discard missing:", my_set)

    temp = my_set.copy()
    temp.clear()
    print("clear:", temp)


def set_operations():
    show_section("Set operations")
    my_set = {1, 2, 3, 4, 5}
    your_set = {2, 3, 4, 6}

    print("issubset:", {2, 3}.issubset(my_set))
    print("issuperset:", my_set.issuperset({2, 3}))
    print("isdisjoint:", {7, 8}.isdisjoint(my_set))

    print("union |:", my_set | your_set)
    print("intersection &:", my_set & your_set)
    print("difference -:", my_set - your_set)
    print("symmetric difference ^:", my_set ^ your_set)

    print("5 in my_set:", 5 in my_set)


def standard_library_imports():
    show_section("Python standard library imports")
    import math as m
    from math import radians, sin, cos

    print("math.sqrt(36):", math.sqrt(36))
    print("m.sqrt(36):", m.sqrt(36))

    angle_degrees = 40
    angle_radians = radians(angle_degrees)
    print("sin:", sin(angle_radians))
    print("cos:", cos(angle_radians))


def name_guard_example():
    show_section("__name__ and main guard")
    print("__name__ in this module:", __name__)
    if __name__ == "__main__":
        print("Running as a script")
    else:
        print("Imported as a module")


NOTES = """
Notes:
- Dictionary keys must be hashable (immutable types like str, int, tuple).
- dict.get(key, default) avoids KeyError and provides a fallback.
- keys(), values(), items() return live views that update when the dict changes.
- popitem() removes the last inserted item in Python 3.7+.
- Sets ignore duplicates and are unordered.
- Use set() to create an empty set; {} creates a dict.
- from module import * is discouraged due to namespace collisions.
"""


QUESTIONS = """
Questions:
1) What is the difference between bracket access and get()?
2) Why do list keys raise a TypeError?
3) When would you use items() instead of keys()?
4) What is the output of enumerate(products.items(), 1)?
5) Why does a shallow copy still share nested objects?
6) What is the difference between remove() and discard() on a set?
7) How would you check if two sets have no elements in common?
8) Why is if __name__ == "__main__" useful?
"""


def main():
    dict_syntax_and_constructor()
    dict_methods()
    dict_looping()
    nested_dict_and_comprehension()
    dict_copying()
    set_basics()
    set_operations()
    standard_library_imports()
    name_guard_example()

    print(NOTES.strip())
    print()
    print(QUESTIONS.strip())


if __name__ == "__main__":
    main()
