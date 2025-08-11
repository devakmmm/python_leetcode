#f_strings

person="Dave"
coins=3

print(f"{person} has {coins} coins left.") # This code demonstrates the use of f-strings in Python to format strings with variables.
# The output will show the person's name and the number of coins they have left.
# F-strings provide a concise way to embed expressions inside string literals, using curly braces `{}`.
# This feature was introduced in Python 3.6 and is a preferred way to format strings due to its readability and efficiency.

message= "\n%s has %s coins left." % (person, coins)  # This code demonstrates the use of the old-style string formatting in Python.
print(message)  # The output will show the person's name and the number of coins they have left.
# This method uses the `%` operator to format strings, where `%s` is a placeholder for string values.
# While this method is still valid, f-strings are generally preferred in modern Python code for their clarity and ease of use.

player = {
    "person": "Alice",
    "coins": 5
}
print(f"{player['person']} has {coins} coins left.") # This code demonstrates the use of f-strings in Python to format strings with variables, including accessing values from a dictionary.
# The output will show the person's name from the dictionary and the number of coins they have left.
# F-strings provide a concise way to embed expressions inside string literals, using curly braces `{}`.
# This feature was introduced in Python 3.6 and is a preferred way to format strings due to its readability and efficiency.


#formatting with f-strings

num=10
print(f"2.25 times {num} is {2.25 * num:.2f} ")  # This code demonstrates the use of f-strings in Python to format strings with variables and expressions.
# The output will show the result of multiplying 2.25 by the variable `num`, formatted to two decimal places.
# The expression `{2.25 * num:.2f}` inside the f-string calculates the product and formats it as a floating-point number with two decimal places.
# F-strings provide a concise way to embed expressions inside string literals, using curly braces `{}`.
# This feature was introduced in Python 3.6 and is a preferred way to format strings due to its readability and efficiency.

print(f"2.25 times {num} is {2.25 / num:.2%} ")  # This code demonstrates the use of f-strings in Python to format strings with variables and expressions.