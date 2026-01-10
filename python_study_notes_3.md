# Python Study Notes (Part 3)

These sections cover essential topics beyond the current code files.
Each section uses the pattern: explanation → code → explanation.

## Core Language Patterns — Unpacking, swapping, slicing

Python has concise, readable patterns for common tasks.

```python
# Unpacking
first, *middle, last = [1, 2, 3, 4, 5]

# Swapping
a, b = 10, 20
a, b = b, a

# Slicing
nums = [0, 1, 2, 3, 4, 5]
print(nums[::2])   # every 2nd element
print(nums[::-1])  # reversed copy
```

Unpacking collects the “rest” into a list. Tuple‑style swapping avoids a temp
variable. Slicing supports step sizes and reverse copies.

## Data Model — Identity vs equality, mutability, hashability

Understanding Python’s data model prevents subtle bugs.

```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == c)  # True (same values)
print(a is c)  # False (different objects)
print(a is b)  # True (same object)

my_set = {1, 2, 3}
# my_set.add([4, 5])  # TypeError: unhashable list
my_set.add((4, 5))    # OK: tuple is hashable
```

`==` compares values; `is` compares identity. Mutable types (list, dict, set)
are unhashable by default; immutable types (str, int, tuple) are hashable.

## Iterators and Generators — Lazy iteration

Iterators let you process items without storing everything in memory.

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for value in countdown(3):
    print(value)
```

`yield` produces values one at a time. This is memory‑efficient and ideal for
large or infinite sequences.

## Comprehensions — List, dict, set, generator

Comprehensions are compact ways to build collections.

```python
squares = [n * n for n in range(6)]
lookup = {n: n * n for n in range(6)}
evens = {n for n in range(10) if n % 2 == 0}
gen = (n * n for n in range(6))
```

Use list/dict/set comprehensions when you want a concrete collection. Use a
generator expression when you want lazy evaluation.

## Functions Advanced — Default args, keyword‑only, decorators

Default args are evaluated once; keyword‑only args improve clarity.

```python
def greet(name, *, punctuation="!"):
    return f"Hello, {name}{punctuation}"

def logger(fn):
    def wrapper(*args, **kwargs):
        print("calling:", fn.__name__)
        return fn(*args, **kwargs)
    return wrapper

@logger
def add(a, b):
    return a + b
```

The `*` makes `punctuation` keyword‑only. Decorators wrap functions for logging,
timing, caching, and access control.

## Context Managers — with, __enter__, __exit__

Context managers ensure cleanup even on errors.

```python
class ManagedFile:
    def __init__(self, path):
        self.path = path
        self.file = None
    def __enter__(self):
        self.file = open(self.path, "w", encoding="utf-8")
        return self.file
    def __exit__(self, exc_type, exc, tb):
        if self.file:
            self.file.close()

with ManagedFile("notes.txt") as f:
    f.write("safe write")
```

`with` calls `__enter__` at the start and `__exit__` at the end, even if an
exception occurs.

## Exceptions — Custom types and best practice

Raise specific exceptions and keep error handling tight.

```python
class ParseError(Exception):
    pass

def parse_int(text):
    try:
        return int(text)
    except ValueError as exc:
        raise ParseError("not an int") from exc
```

Use custom exceptions to signal specific failures. `raise ... from ...`
preserves the original traceback for debugging.

## Dataclasses — Cleaner data containers

Dataclasses reduce boilerplate for simple data objects.

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

p = Point(2, 3)
print(p)
```

Dataclasses auto‑generate `__init__`, `__repr__`, and comparisons unless you
override them.

## Typing — Hints for clarity and tooling

Type hints improve readability and enable static analysis.

```python
from typing import Iterable

def total(values: Iterable[int]) -> int:
    return sum(values)
```

Hints are not enforced at runtime, but tools like `mypy` can check them.
