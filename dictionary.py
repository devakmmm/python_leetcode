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

import math  # Import the math module for standard library examples.


def show_section(title):  # Define a helper to label output sections.
    print("\n" + title)  # Print a blank line and the section title.
    print("-" * len(title))  # Print a dashed underline under the title.


def dict_syntax_and_constructor():  # Define a demo for dict creation styles.
    show_section("Dictionaries: literals and dict()")  # Display the section header.
    dictionary = {"key1": "value1", "key2": "value2"}  # Create a dict literal.
    print("literal:", dictionary)  # Print the literal dict.

    pizza = dict(  # Create a dict using the dict constructor.
        [  # Start a list of key-value tuples.
            ("name", "Margherita Pizza"),  # Add a name entry.
            ("price", 8.9),  # Add a price entry.
            ("calories_per_slice", 250),  # Add a calories entry.
            ("toppings", ["mozzarella", "basil"]),  # Add a list of toppings.
        ]  # End the list of tuples.
    )  # Finish constructing the dict.
    print("dict constructor:", pizza)  # Print the constructed dict.
    print("bracket access:", pizza["name"])  # Access a value with brackets.
    print("get with default:", pizza.get("total_time", 0))  # Access with a default.

    try:  # Start a block to show a TypeError example.
        bad_key = [1, 2]  # Create a mutable list key.
        bad_dict = {bad_key: "nope"}  # Attempt to use a list as a key.
        print(bad_dict)  # Print the dict if it worked (it will not).
    except TypeError as exc:  # Catch the unhashable key error.
        print("list key error:", exc)  # Print the error message.

    ok_key = (1, 2)  # Create an immutable tuple key.
    ok_dict = {ok_key: "tuple key ok"}  # Use the tuple as a dict key.
    print("tuple key:", ok_dict)  # Print the dict with a tuple key.


def dict_methods():  # Define a demo for common dictionary methods.
    show_section("Common dictionary methods")  # Display the section header.
    pizza = {  # Define a sample dictionary.
        "name": "Margherita Pizza",  # Store the name value.
        "price": 8.9,  # Store the price value.
        "calories_per_slice": 250,  # Store the calories value.
    }  # End the sample dictionary.

    keys_view = pizza.keys()  # Get a dynamic view of keys.
    values_view = pizza.values()  # Get a dynamic view of values.
    items_view = pizza.items()  # Get a dynamic view of items.
    print("keys view:", keys_view)  # Print the keys view.
    print("values view:", values_view)  # Print the values view.
    print("items view:", items_view)  # Print the items view.

    pizza.update({"price": 15, "total_time": 25})  # Update existing and add new keys.
    print("after update:", pizza)  # Print the updated dictionary.
    print("keys after update:", list(keys_view))  # Show updated keys from the view.

    removed_price = pizza.pop("price", 10)  # Remove price with a default fallback.
    print("pop price:", removed_price)  # Print the removed price value.

    try:  # Start a block for missing key removal.
        pizza.pop("total_price")  # Attempt to pop a missing key.
    except KeyError as exc:  # Catch the KeyError.
        print("pop missing key:", exc)  # Print the error message.

    last_key, last_value = pizza.popitem()  # Remove the last inserted item.
    print("popitem:", last_key, last_value)  # Print the removed key-value pair.

    temp = {"a": 1, "b": 2}  # Create a temporary dictionary.
    temp.clear()  # Remove all items from the temp dict.
    print("clear:", temp)  # Print the now-empty dict.


def dict_looping():  # Define a demo for iterating over dictionaries.
    show_section("Looping over dictionaries")  # Display the section header.
    products = {  # Define a sample products dictionary.
        "Laptop": 990,  # Add a product and price.
        "Smartphone": 600,  # Add a product and price.
        "Tablet": 250,  # Add a product and price.
        "Headphones": 70,  # Add a product and price.
    }  # End the products dictionary.

    for price in products.values():  # Iterate over values only.
        print("value:", price)  # Print each price value.

    for product in products.keys():  # Iterate over keys explicitly.
        print("key:", product)  # Print each product name.

    for product in products:  # Iterate over keys implicitly.
        print("key (implicit):", product)  # Print each product name.

    for product in products.items():  # Iterate over key-value tuples.
        print("item tuple:", product)  # Print each tuple.

    for product, price in products.items():  # Unpack key-value tuples.
        print("item unpacked:", product, price)  # Print the unpacked pair.

    for index, item in enumerate(products.items()):  # Enumerate items with index.
        print("enumerate:", index, item)  # Print index and item tuple.

    for index, item in enumerate(products.items(), 1):  # Enumerate starting at 1.
        print("enumerate start=1:", index, item)  # Print index and item tuple.


def nested_dict_and_comprehension():  # Define a demo for nested dicts.
    show_section("Nested dictionaries and comprehensions")  # Display header.
    bands = {  # Define a nested dictionary of bands.
        "The Beatles": {  # Add the Beatles entry.
            "members": ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Starr"],  # Members list.
            "genre": "Rock",  # Genre label.
        },  # End Beatles entry.
        "Queen": {  # Add the Queen entry.
            "members": ["Freddie Mercury", "Brian May", "Roger Taylor", "John Deacon"],  # Members list.
            "genre": "Rock",  # Genre label.
        },  # End Queen entry.
        "Nirvana": {  # Add the Nirvana entry.
            "members": ["Kurt Cobain", "Krist Novoselic", "Dave Grohl"],  # Members list.
            "genre": "Grunge",  # Genre label.
        },  # End Nirvana entry.
    }  # End the bands dictionary.

    print("Queen members:", bands["Queen"]["members"])  # Access nested members.
    member_counts = {name: len(data["members"]) for name, data in bands.items()}  # Count members.
    print("member counts:", member_counts)  # Print the counts.


def dict_copying():  # Define a demo for copying and aliasing.
    show_section("Copying vs aliasing (shallow copy)")  # Display header.
    original = {"a": 1, "b": {"nested": 2}}  # Define a nested dict.
    alias = original  # Create a direct alias reference.
    shallow = original.copy()  # Create a shallow copy.

    original["a"] = 10  # Mutate a top-level value.
    original["b"]["nested"] = 99  # Mutate a nested value.

    print("original:", original)  # Print the original dict.
    print("alias:", alias)  # Print the alias dict.
    print("shallow:", shallow)  # Print the shallow copy.


def set_basics():  # Define a demo for set creation and methods.
    show_section("Sets: creation and methods")  # Display header.
    my_set = {1, 2, 3, 4, 5}  # Create a set literal.
    empty_set = set()  # Create an empty set.
    print("set literal:", my_set)  # Print the set literal.
    print("empty set:", empty_set, type(empty_set))  # Show empty set type.

    my_set.add(6)  # Add a new element to the set.
    print("after add:", my_set)  # Print the updated set.

    my_set.remove(4)  # Remove an existing element.
    print("after remove:", my_set)  # Print the updated set.

    try:  # Start a block to show remove failure.
        my_set.remove(42)  # Attempt to remove a missing element.
    except KeyError as exc:  # Catch the KeyError.
        print("remove missing:", exc)  # Print the error message.

    my_set.discard(42)  # Discard a missing element without error.
    print("after discard missing:", my_set)  # Show the set remains unchanged.

    temp = my_set.copy()  # Copy the set.
    temp.clear()  # Remove all elements from the copy.
    print("clear:", temp)  # Print the cleared set.


def set_operations():  # Define a demo for set operations.
    show_section("Set operations")  # Display header.
    my_set = {1, 2, 3, 4, 5}  # Define the first set.
    your_set = {2, 3, 4, 6}  # Define the second set.

    print("issubset:", {2, 3}.issubset(my_set))  # Check subset relationship.
    print("issuperset:", my_set.issuperset({2, 3}))  # Check superset relationship.
    print("isdisjoint:", {7, 8}.isdisjoint(my_set))  # Check disjoint relationship.

    print("union |:", my_set | your_set)  # Compute union.
    print("intersection &:", my_set & your_set)  # Compute intersection.
    print("difference -:", my_set - your_set)  # Compute difference.
    print("symmetric difference ^:", my_set ^ your_set)  # Compute symmetric difference.

    print("5 in my_set:", 5 in my_set)  # Check membership with in.


def standard_library_imports():  # Define a demo for import statements.
    show_section("Python standard library imports")  # Display header.
    import math as m  # Import math with an alias.
    from math import radians, sin, cos  # Import specific math functions.

    print("math.sqrt(36):", math.sqrt(36))  # Call sqrt via the module.
    print("m.sqrt(36):", m.sqrt(36))  # Call sqrt via the alias.

    angle_degrees = 40  # Define an angle in degrees.
    angle_radians = radians(angle_degrees)  # Convert degrees to radians.
    print("sin:", sin(angle_radians))  # Compute sine.
    print("cos:", cos(angle_radians))  # Compute cosine.


def name_guard_example():  # Define a demo for the __name__ guard.
    show_section("__name__ and main guard")  # Display header.
    print("__name__ in this module:", __name__)  # Show this module's name.
    if __name__ == "__main__":  # Check if running as a script.
        print("Running as a script")  # Print the script message.
    else:  # Otherwise, assume it was imported.
        print("Imported as a module")  # Print the import message.


NOTES = """  # Store study notes as a multiline string.
Notes:
- Dictionary keys must be hashable (immutable types like str, int, tuple).
- dict.get(key, default) avoids KeyError and provides a fallback.
- keys(), values(), items() return live views that update when the dict changes.
- popitem() removes the last inserted item in Python 3.7+.
- Sets ignore duplicates and are unordered.
- Use set() to create an empty set; {} creates a dict.
- from module import * is discouraged due to namespace collisions.
"""


QUESTIONS = """  # Store practice questions as a multiline string.
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


def main():  # Define the script entry point.
    dict_syntax_and_constructor()  # Run dict creation examples.
    dict_methods()  # Run dict methods examples.
    dict_looping()  # Run dict looping examples.
    nested_dict_and_comprehension()  # Run nested dict examples.
    dict_copying()  # Run dict copying examples.
    set_basics()  # Run set creation and method examples.
    set_operations()  # Run set operation examples.
    standard_library_imports()  # Run import examples.
    name_guard_example()  # Run __name__ guard example.

    print(NOTES.strip())  # Print notes without extra whitespace.
    print()  # Print a blank line between notes and questions.
    print(QUESTIONS.strip())  # Print questions for review.


if __name__ == "__main__":  # Run main only when executed directly.
    main()  # Invoke the entry point.
