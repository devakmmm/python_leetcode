# Python Study Notes (Part 1)

These notes summarize the topics covered in the workspace. Each section follows a
Jupyter-style flow: explanation → code → explanation. Use the full `.py` files
for runnable versions and deeper walkthroughs.

## hello.py — A minimal program

Start with simple variables, functions, and output.

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("world"))
```

Output:
```
Hello, world!
```

This defines a function that returns a string and prints it. Output:
`Hello, world!`.

## data_types.py — Strings, numbers, booleans, None

Strings are immutable; numbers support arithmetic; booleans reflect truthiness.

```python
first = "dev"
last = "ops"
full = first + " " + last

print(full.upper())
print(full[0], full[-1], full[1:3])

a, b = 10, 3
print(a // b, a % b, a ** b)

value = None
print(value is None)
```

Output:
```
DEV OPS
d s ev
3 1 1000
True
```

`full.upper()` returns a new string (strings are immutable). `//` is integer
division, `%` is remainder, and `**` is exponentiation. `None` is a singleton,
so use `is None` to check for it.

## fstring.py — f-strings and formatting

F-strings embed expressions directly inside strings.

```python
person = "Dave"
coins = 3
print(f"{person} has {coins} coins left.")
print(f"{2.25 * 10:.2f}")
print(f"{2.25 / 10:.2%}")
```

Output:
```
Dave has 3 coins left.
22.50
22.50%
```

`:.2f` formats floats to two decimals; `:.2%` converts to a percentage string.

## lists.py — Lists and tuples

Lists are mutable and support slicing; tuples are immutable.

```python
users = ["dev", "ops", "admin"]
users.append("guest")
print(users[1:3])

users[1:3] = ["sysadmin"]
print(users)

mytuple = ("dev", "ops", "admin")
one, two, *rest = (1, 2, 3, 4)
```

Output:
```
['ops', 'admin']
['dev', 'sysadmin', 'guest']
```

Slice assignment can change list length. Tuple unpacking collects extra values
into a list with `*rest`.

## dictionary.py — Dictionaries and sets

Dictionaries map keys to values; sets store unique items.

```python
pizza = dict([("name", "Margherita"), ("price", 8.9)])
print(pizza["name"], pizza.get("total_time", 0))

pizza.update({"price": 10})
print(list(pizza.keys()), list(pizza.values()))

my_set = {1, 2, 3}
my_set.add(4)
print(my_set | {3, 4, 5})
```

Output:
```
Margherita 0
['name', 'price'] ['Margherita', 10]
{1, 2, 3, 4, 5}
```

`get` avoids `KeyError` by returning a default. Set union (`|`) combines unique
items; duplicates collapse automatically.

## loops.py — for/while, break/continue, enumerate, zip

Loops iterate over iterables and ranges; `enumerate` adds an index.

```python
names = ["Alice", "Bob", "Charlie"]
for i, name in enumerate(names, start=1):
    print(i, name)

count = 3
while count > 0:
    count -= 1
```

Output:
```
1 Alice
2 Bob
3 Charlie
```

`enumerate` yields `(index, item)` pairs. `while` loops continue until the
condition is False.

## ternaryoperator.py — Conditional expressions

Use a ternary expression for short, readable branches.

```python
score = 87
grade = "pass" if score >= 60 else "fail"
print(grade)
```

Output:
```
pass
```

This selects `"pass"` because the condition is True.

## regex_quantifiers.py — `\d` vs `\d+`

`\d` matches a single digit; `\d+` matches one or more digits in a row.

```python
import re

book = "Fahrenheit 451"
print(re.search(r"\d", book).group())
print(re.search(r"\d+", book).group())
print(re.findall(r"\d+", "Room 451, Floor 7"))
```

Output:
```
4
451
['451', '7']
```

`\d` finds the first digit (`4`), while `\d+` finds the full number (`451`).
`findall` returns all matches as a list, so you get `['451', '7']`.
