"""
lists.py - Guided examples for Python lists and tuples.

Learning goals:
- Membership tests, indexing, and slicing
- List mutation methods and slice assignment
- Sorting vs sorted, shallow copies, and aliasing
- List concatenation, nesting, and comprehensions
- Tuple creation, unpacking, and immutability
"""


def show_section(title):  # Define a helper to label output sections.
    print("\n" + title)  # Print a blank line and the section title.
    print("-" * len(title))  # Print a dashed underline under the title.


def membership_and_indexing():  # Define a demo for membership and indexing.
    show_section("Membership and indexing")  # Display the section header.
    users = ["dev", "ops", "admin"]  # Create a list of users.
    data = ["23", "45", "devops"]  # Create a list of data strings.

    print("users:", users)  # Print the users list.
    print("'dev' in users:", "dev" in users)  # Check membership.
    print("'dev' not in users:", "dev" not in users)  # Check non-membership.
    print("data:", data)  # Print the data list.
    print("'23' in data:", "23" in data)  # Check membership in data.
    print("'devops' not in data:", "devops" not in data)  # Check non-membership in data.

    print("last user:", users[-1])  # Access the last element.
    print("first data item:", data[0])  # Access the first element.
    print("users[1:3]:", users[1:3])  # Slice elements 1 to 2.
    print("data[:2]:", data[:2])  # Slice the first two elements.
    print("users[1:]:", users[1:])  # Slice from index 1 to end.
    print("data[-2:]:", data[-2:])  # Slice the last two elements.
    print("users[:-1]:", users[:-1])  # Slice all but the last element.


EXAMPLE_WALKTHROUGH_MEMBERSHIP = """  # Store a walkthrough for membership_and_indexing.
Example Walkthrough: membership_and_indexing
- show_section("Membership and indexing"):
  prints the "Membership and indexing" header and underline.
- users = ["dev", "ops", "admin"]:
  creates the users list.
- data = ["23", "45", "devops"]:
  creates the data list.
- print("users:", users):
  outputs: users: ['dev', 'ops', 'admin']
- print("'dev' in users:", "dev" in users):
  outputs: 'dev' in users: True
- print("'dev' not in users:", "dev" not in users):
  outputs: 'dev' not in users: False
- print("data:", data):
  outputs: data: ['23', '45', 'devops']
- print("'23' in data:", "23" in data):
  outputs: '23' in data: True
- print("'devops' not in data:", "devops" not in data):
  outputs: 'devops' not in data: False
- print("last user:", users[-1]):
  outputs: last user: admin
- print("first data item:", data[0]):
  outputs: first data item: 23
- print("users[1:3]:", users[1:3]):
  outputs: users[1:3]: ['ops', 'admin']
- print("data[:2]:", data[:2]):
  outputs: data[:2]: ['23', '45']
- print("users[1:]:", users[1:]):
  outputs: users[1:]: ['ops', 'admin']
- print("data[-2:]:", data[-2:]):
  outputs: data[-2:]: ['45', 'devops']
- print("users[:-1]:", users[:-1]):
  outputs: users[:-1]: ['dev', 'ops']
"""


def mutation_examples():  # Define a demo for list mutation.
    show_section("Mutation: append, insert, and slice assignment")  # Display header.
    users = ["dev", "ops", "admin"]  # Create a list to mutate.

    users.append("guest")  # Append a new element.
    print("after append:", users)  # Show the updated list.

    users.insert(1, "superuser")  # Insert at index 1.
    print("after insert:", users)  # Show the updated list.

    users[2:2] = ["tester", "developer"]  # Insert via slice assignment.
    print("after slice insert:", users)  # Show the updated list.

    users[1:3] = ["sysadmin"]  # Replace a slice with one element.
    print("after slice replace:", users)  # Show the updated list.


EXAMPLE_WALKTHROUGH_MUTATION = """  # Store a walkthrough for mutation_examples.
Example Walkthrough: mutation_examples
- show_section("Mutation: append, insert, and slice assignment"):
  prints the section header.
- users = ["dev", "ops", "admin"]:
  creates the starting list.
- users.append("guest"):
  adds "guest" to the end.
- print("after append:", users):
  outputs: after append: ['dev', 'ops', 'admin', 'guest']
- users.insert(1, "superuser"):
  inserts "superuser" at index 1.
- print("after insert:", users):
  outputs: after insert: ['dev', 'superuser', 'ops', 'admin', 'guest']
- users[2:2] = ["tester", "developer"]:
  inserts two items at index 2 without replacing.
- print("after slice insert:", users):
  outputs: after slice insert: ['dev', 'superuser', 'tester', 'developer', 'ops', 'admin', 'guest']
- users[1:3] = ["sysadmin"]:
  replaces elements at indices 1 and 2 with one item.
- print("after slice replace:", users):
  outputs: after slice replace: ['dev', 'sysadmin', 'developer', 'ops', 'admin', 'guest']
"""


def removal_examples():  # Define a demo for removing elements.
    show_section("Removal: remove, pop, del, clear")  # Display header.
    users = ["dev", "ops", "admin", "guest"]  # Create a list to modify.

    if "dev" in users:  # Check that the value exists before removing.
        users.remove("dev")  # Remove the first matching element.
    print("after remove:", users)  # Show the updated list.

    last = users.pop()  # Remove and capture the last element.
    print("popped:", last, "remaining:", users)  # Show removed and remaining.

    del users[0]  # Delete the element at index 0.
    print("after del index 0:", users)  # Show the updated list.

    users.clear()  # Remove all elements from the list.
    print("after clear:", users)  # Show the empty list.


EXAMPLE_WALKTHROUGH_REMOVAL = """  # Store a walkthrough for removal_examples.
Example Walkthrough: removal_examples
- show_section("Removal: remove, pop, del, clear"):
  prints the section header.
- users = ["dev", "ops", "admin", "guest"]:
  creates the starting list.
- if "dev" in users:
  condition is True, so remove runs.
- users.remove("dev"):
  removes the first "dev".
- print("after remove:", users):
  outputs: after remove: ['ops', 'admin', 'guest']
- last = users.pop():
  removes and returns the last element ("guest").
- print("popped:", last, "remaining:", users):
  outputs: popped: guest remaining: ['ops', 'admin']
- del users[0]:
  deletes the first element.
- print("after del index 0:", users):
  outputs: after del index 0: ['admin']
- users.clear():
  removes all elements.
- print("after clear:", users):
  outputs: after clear: []
"""


def extend_and_concat():  # Define a demo for extend and concatenation.
    show_section("Extend, concatenate, and nest lists")  # Display header.
    users = ["dev", "ops"]  # Create a list of users.
    users.extend(["admin", "manager"])  # Extend with multiple elements.
    print("after extend:", users)  # Show the updated list.

    list1 = [1, 2, 3]  # Define the first list.
    list2 = [4, 5, 6]  # Define the second list.
    combined = list1 + list2  # Concatenate lists into a new list.
    print("combined:", combined)  # Show the concatenated result.

    nested = [users, list2]  # Create a nested list.
    print("nested list:", nested)  # Show the nested structure.


EXAMPLE_WALKTHROUGH_EXTEND = """  # Store a walkthrough for extend_and_concat.
Example Walkthrough: extend_and_concat
- show_section("Extend, concatenate, and nest lists"):
  prints the section header.
- users = ["dev", "ops"]:
  creates the starting list.
- users.extend(["admin", "manager"]):
  appends both items to users.
- print("after extend:", users):
  outputs: after extend: ['dev', 'ops', 'admin', 'manager']
- list1 = [1, 2, 3]:
  creates list1.
- list2 = [4, 5, 6]:
  creates list2.
- combined = list1 + list2:
  creates a new list [1, 2, 3, 4, 5, 6].
- print("combined:", combined):
  outputs: combined: [1, 2, 3, 4, 5, 6]
- nested = [users, list2]:
  creates a list containing two lists.
- print("nested list:", nested):
  outputs: nested list: [['dev', 'ops', 'admin', 'manager'], [4, 5, 6]]
"""


def sort_and_reverse():  # Define a demo for sorting and reversing.
    show_section("Sorting and reversing")  # Display header.
    users = ["dev", "ops", "admin", "guest"]  # Create a list to sort.
    print("original:", users)  # Show the original list.
    print("sorted copy:", sorted(users))  # Show a sorted copy.

    users.sort()  # Sort the list in place.
    print("sorted in place:", users)  # Show the sorted list.

    users.sort(reverse=True)  # Sort in descending order.
    print("sorted reverse:", users)  # Show the descending order list.

    users.sort(key=len)  # Sort by string length.
    print("sorted by length:", users)  # Show the length-sorted list.

    users.reverse()  # Reverse the list in place.
    print("reversed in place:", users)  # Show the reversed list.
    print("reversed copy:", list(reversed(users)))  # Show a reversed copy.


EXAMPLE_WALKTHROUGH_SORT = """  # Store a walkthrough for sort_and_reverse.
Example Walkthrough: sort_and_reverse
- show_section("Sorting and reversing"):
  prints the section header.
- users = ["dev", "ops", "admin", "guest"]:
  creates the starting list.
- print("original:", users):
  outputs: original: ['dev', 'ops', 'admin', 'guest']
- print("sorted copy:", sorted(users)):
  outputs: sorted copy: ['admin', 'dev', 'guest', 'ops']
- users.sort():
  sorts the list in place.
- print("sorted in place:", users):
  outputs: sorted in place: ['admin', 'dev', 'guest', 'ops']
- users.sort(reverse=True):
  sorts in descending order.
- print("sorted reverse:", users):
  outputs: sorted reverse: ['ops', 'guest', 'dev', 'admin']
- users.sort(key=len):
  sorts by string length.
- print("sorted by length:", users):
  outputs: sorted by length: ['ops', 'dev', 'guest', 'admin']
- users.reverse():
  reverses the list in place.
- print("reversed in place:", users):
  outputs: reversed in place: ['admin', 'guest', 'dev', 'ops']
- print("reversed copy:", list(reversed(users))):
  outputs: reversed copy: ['ops', 'dev', 'guest', 'admin']
"""


def copy_and_alias():  # Define a demo for copying and aliasing.
    show_section("Copying vs aliasing (shallow copies)")  # Display header.
    users = ["dev", "ops", "admin"]  # Create a list to copy.
    alias = users  # Create a reference alias.
    copy1 = users.copy()  # Create a shallow copy via copy().
    copy2 = users[:]  # Create a shallow copy via slicing.
    copy3 = list(users)  # Create a shallow copy via list().

    users.append("guest")  # Mutate the original list.
    print("original:", users)  # Show the original list.
    print("alias:", alias)  # Show the alias reference.
    print("copy1:", copy1)  # Show the copy made with copy().
    print("copy2:", copy2)  # Show the copy made with slicing.
    print("copy3:", copy3)  # Show the copy made with list().


EXAMPLE_WALKTHROUGH_COPY = """  # Store a walkthrough for copy_and_alias.
Example Walkthrough: copy_and_alias
- show_section("Copying vs aliasing (shallow copies)"):
  prints the section header.
- users = ["dev", "ops", "admin"]:
  creates the original list.
- alias = users:
  alias points to the same list object.
- copy1 = users.copy():
  makes a shallow copy.
- copy2 = users[:]:
  makes a shallow copy using slicing.
- copy3 = list(users):
  makes a shallow copy using list().
- users.append("guest"):
  mutates the original list.
- print("original:", users):
  outputs: original: ['dev', 'ops', 'admin', 'guest']
- print("alias:", alias):
  outputs the same as original because alias is the same object.
- print("copy1:", copy1):
  outputs: copy1: ['dev', 'ops', 'admin']
- print("copy2:", copy2):
  outputs: copy2: ['dev', 'ops', 'admin']
- print("copy3:", copy3):
  outputs: copy3: ['dev', 'ops', 'admin']
"""


def plus_equals_demo():  # Define a demo for += with lists.
    show_section("+= with lists")  # Display header.
    users = ["dev", "ops"]  # Create a list of users.
    users += ["newuser"]  # Extend the list with another list.
    print("+= list:", users)  # Show the updated list.

    users = ["dev", "ops"]  # Reset the list.
    users += "newuser"  # Extend the list with each character.
    print("+= string (each char added):", users)  # Show the character expansion.


EXAMPLE_WALKTHROUGH_PLUS_EQUALS = """  # Store a walkthrough for plus_equals_demo.
Example Walkthrough: plus_equals_demo
- show_section("+= with lists"):
  prints the section header.
- users = ["dev", "ops"]:
  creates the starting list.
- users += ["newuser"]:
  extends the list with one new element.
- print("+= list:", users):
  outputs: += list: ['dev', 'ops', 'newuser']
- users = ["dev", "ops"]:
  resets the list.
- users += "newuser":
  extends the list with each character.
- print("+= string (each char added):", users):
  outputs: += string (each char added): ['dev', 'ops', 'n', 'e', 'w', 'u', 's', 'e', 'r']
"""


def comprehension_examples():  # Define a demo for list comprehensions.
    show_section("List comprehensions")  # Display header.
    squares = [n * n for n in range(1, 6)]  # Build squares with comprehension.
    print("squares:", squares)  # Show the squares list.

    even_squares = [n * n for n in range(1, 11) if n % 2 == 0]  # Filter evens.
    print("even squares:", even_squares)  # Show the filtered list.

    upper_users = [name.upper() for name in ["dev", "ops", "admin"]]  # Uppercase names.
    print("upper case:", upper_users)  # Show the uppercase list.


EXAMPLE_WALKTHROUGH_COMPREHENSION = """  # Store a walkthrough for comprehension_examples.
Example Walkthrough: comprehension_examples
- show_section("List comprehensions"):
  prints the section header.
- squares = [n * n for n in range(1, 6)]:
  creates [1, 4, 9, 16, 25].
- print("squares:", squares):
  outputs: squares: [1, 4, 9, 16, 25]
- even_squares = [n * n for n in range(1, 11) if n % 2 == 0]:
  creates [4, 16, 36, 64, 100].
- print("even squares:", even_squares):
  outputs: even squares: [4, 16, 36, 64, 100]
- upper_users = [name.upper() for name in ["dev", "ops", "admin"]]:
  creates ['DEV', 'OPS', 'ADMIN'].
- print("upper case:", upper_users):
  outputs: upper case: ['DEV', 'OPS', 'ADMIN']
"""


def tuple_examples():  # Define a demo for tuples.
    show_section("Tuples")  # Display header.
    mytuple = ("dev", "ops", "admin")  # Create a tuple of strings.
    another_tuple = (1, 2, 3, 4, 5, 6, 7, 7)  # Create a tuple of ints.

    print("mytuple:", mytuple)  # Print the first tuple.
    print("another_tuple:", another_tuple)  # Print the second tuple.
    print("count of 7:", another_tuple.count(7))  # Count occurrences of 7.
    print("index of 3:", another_tuple.index(3))  # Find the index of 3.

    one, two, *three = another_tuple  # Unpack into variables.
    print("unpacked:", one, two, three)  # Show unpacked values.

    newlist = list(mytuple)  # Convert tuple to list.
    newlist.append("guest")  # Append to the list.
    print("tuple -> list -> appended:", newlist)  # Show the list after append.


EXAMPLE_WALKTHROUGH_TUPLES = """  # Store a walkthrough for tuple_examples.
Example Walkthrough: tuple_examples
- show_section("Tuples"):
  prints the section header.
- mytuple = ("dev", "ops", "admin"):
  creates a tuple of three strings.
- another_tuple = (1, 2, 3, 4, 5, 6, 7, 7):
  creates a tuple of integers.
- print("mytuple:", mytuple):
  outputs: mytuple: ('dev', 'ops', 'admin')
- print("another_tuple:", another_tuple):
  outputs: another_tuple: (1, 2, 3, 4, 5, 6, 7, 7)
- print("count of 7:", another_tuple.count(7)):
  outputs: count of 7: 2
- print("index of 3:", another_tuple.index(3)):
  outputs: index of 3: 2
- one, two, *three = another_tuple:
  unpacks one=1, two=2, three=[3, 4, 5, 6, 7, 7].
- print("unpacked:", one, two, three):
  outputs: unpacked: 1 2 [3, 4, 5, 6, 7, 7]
- newlist = list(mytuple):
  converts tuple to list ['dev', 'ops', 'admin'].
- newlist.append("guest"):
  adds "guest" to the list.
- print("tuple -> list -> appended:", newlist):
  outputs: tuple -> list -> appended: ['dev', 'ops', 'admin', 'guest']
"""


NOTES = """  # Store study notes as a multiline string.
Notes:
- Lists are mutable dynamic arrays. Appending to the end is amortized O(1).
- Inserting or removing in the middle is O(n) because elements shift.
- Slicing creates a new list; slice assignment mutates the original list.
- list.sort() sorts in place and returns None; sorted() returns a new list.
- Copies are shallow; nested lists still share inner objects.
"""


QUESTIONS = """  # Store practice questions as a multiline string.
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


def main():  # Define the script entry point.
    membership_and_indexing()  # Run membership and indexing examples.
    mutation_examples()  # Run mutation examples.
    removal_examples()  # Run removal examples.
    extend_and_concat()  # Run extend and concatenation examples.
    sort_and_reverse()  # Run sorting and reversing examples.
    copy_and_alias()  # Run copy and alias examples.
    plus_equals_demo()  # Run += demo.
    comprehension_examples()  # Run comprehension examples.
    tuple_examples()  # Run tuple examples.

    print(NOTES.strip())  # Print notes without extra whitespace.
    print()  # Print a blank line between notes and questions.
    print(QUESTIONS.strip())  # Print questions for review.


EXAMPLE_WALKTHROUGH_MAIN = """  # Store a walkthrough for main.
Example Walkthrough: main
- membership_and_indexing():
  runs the membership and slicing demo.
- mutation_examples():
  runs the list mutation demo.
- removal_examples():
  runs the removal methods demo.
- extend_and_concat():
  runs the extend and concatenation demo.
- sort_and_reverse():
  runs the sorting and reversing demo.
- copy_and_alias():
  runs the copy vs alias demo.
- plus_equals_demo():
  runs the += demo.
- comprehension_examples():
  runs the comprehension demo.
- tuple_examples():
  runs the tuple demo.
- print(NOTES.strip()):
  prints the Notes block.
- print():
  prints a blank line.
- print(QUESTIONS.strip()):
  prints the Questions block.
"""


if __name__ == "__main__":  # Run main only when executed directly.
    main()  # Invoke the entry point.
