# Python Review Notes

This document is a structured review of core Python topics with explanations and runnable examples. All code samples target Python 3.x.

## What is Python?
Python is a general-purpose programming language known for readability and a large standard library. It is dynamically typed, so variables can point to values of any type without explicit declarations.

Common use cases:
- Data science and machine learning
- Web development and APIs
- Scripting and automation
- Embedded systems and IoT (for example, MicroPython)

## Python in Your Local Environment
The recommended way to install Python is to download the official installer from https://www.python.org/.

Check your installed version:
```bash
python3 --version
```

Run a Python script:
```bash
python3 my_script.py
```

Open the interactive REPL:
```bash
python3
```

## Variables and Naming
Variables are names bound to objects. Assignment does not copy a value; it binds a name to a value.

```python
name = 'John Doe'
age = 25
```

Naming rules and conventions:
- Names start with a letter or underscore, not a number.
- Names can contain letters, numbers, and underscores.
- Names are case-sensitive: `age`, `Age`, and `AGE` are different.
- Avoid Python keywords like `if`, `class`, and `def`.
- Use `snake_case` for multi-word names.

## Comments and Output
Single-line comments start with `#`.

```python
# This is a single-line comment
```

Triple-quoted strings are often used as docstrings, but can also be used to hold multi-line notes.

```python
"""
Multi-line note or docstring.
"""
```

`print()` displays output to the console:
```python
print('Hello world!')
```

## Core Data Types
Python is dynamically typed, so the type is determined by the value assigned.

### Numbers (int, float)
```python
my_integer = 10
my_float = 4.5
```

### String (str)
```python
my_string = 'hello'
```

### Boolean (bool)
```python
is_active = True
```

### List
Ordered, mutable collection.
```python
my_list = [22, 'Hello world', 3.14, True]
```

### Tuple
Ordered, immutable collection.
```python
my_tuple = (7, 5, 8)
```

### Dictionary
Key-value mapping.
```python
my_dict = {'name': 'Alice', 'age': 25}
```

### Set
Unordered collection of unique elements.
```python
my_set = {7, 5, 8}
```

### Range
Lazy sequence of numbers, often used in loops.
```python
my_range = range(5)
```

### None
Represents the absence of a value.
```python
my_none = None
```

## Mutable vs Immutable
- Immutable types cannot be changed in place: `int`, `float`, `bool`, `str`, `tuple`, `range`, `None`.
- Mutable types can be modified: `list`, `dict`, `set`.

Reassignment points the variable name to a new object:
```python
x = 'hello'
x = 'world'  # x now points to a new string object
```

## Type Inspection
Use `type()` to see the type and `isinstance()` to check a type safely.

```python
greeting = 'Hello there!'
age = 21

print(type(greeting))  # <class 'str'>
print(type(age))       # <class 'int'>

print(isinstance('Hello', str))  # True
print(isinstance(42, str))       # False
```

## Working with Strings
Strings are immutable sequences of characters.

### Indexing and Slicing
```python
text = 'Hello world'

print(text[0])   # H
print(text[6])   # w
print(text[-1])  # d

print(text[0:5])  # Hello
print(text[6:])   # world
print(text[::2])  # Hlowrd
```

### Escaping Quotes
```python
msg = 'It\'s a sunny day'
quote = "She said, \"Hello!\""
```

### Concatenation and f-strings
```python
name = 'Jessica'
print('My name is ' + name + '.')

message = f'My name is {name}.'
print(message)
```

### Length and Membership
```python
print(len('Python'))        # 6
print('Py' in 'Python')     # True
print('java' in 'Python')   # False
```

### Common String Methods
```python
text = '  hello World  '

print(text.upper())        # '  HELLO WORLD  '
print(text.lower())        # '  hello world  '
print(text.strip())        # 'hello World'
print(text.replace('World', 'Python'))  # '  hello Python  '

parts = 'one-two-three'.split('-')
print(parts)  # ['one', 'two', 'three']

print(' '.join(parts))     # 'one two three'

print(text.startswith('  he'))  # True
print(text.endswith('  '))      # True

print('banana'.find('na'))   # 2
print('banana'.count('a'))   # 3

print('hello'.capitalize())  # 'Hello'
print('hello'.islower())     # True
print('HELLO'.isupper())     # True
print('los angeles'.title()) # 'Los Angeles'
```

### str.maketrans() and translate()
```python
trans_table = str.maketrans('abc', '123')
result = 'abcabc'.translate(trans_table)
print(result)  # '123123'
```

## Numbers and Math
Python supports integer and floating-point arithmetic. Mixing `int` and `float` produces a `float`.

```python
int_1 = 56
int_2 = 12
float_1 = 5.4
float_2 = 12.0

print(int_1 + int_2)     # 68
print(float_1 + float_2) # 17.4
print(int_1 / int_2)     # 4.666...
```

Common numeric operations:
```python
print(56 % 12)   # 8  (modulus)
print(56 // 12)  # 4  (floor division)
print(4 ** 2)    # 16 (exponentiation)
```

Common numeric helpers:
```python
print(float(4))     # 4.0
print(int(4.9))     # 4
print(round(3.4))   # 3
print(abs(-13))     # 13
print(bin(56))      # '0b111000'
print(oct(56))      # '0o70'
print(hex(56))      # '0x38'
print(pow(2, 3))    # 8
```

## Augmented Assignment
Augmented assignment combines an operation and assignment in one step.

```python
count = 10
count += 5  # 15

count -= 3  # 12
count *= 2  # 24
count /= 4  # 6.0
count //= 2 # 3.0
count **= 2 # 9.0
```

## Functions
Functions are reusable blocks of code that take inputs and return outputs.

```python
def get_sum(num_1, num_2):
    return num_1 + num_2

print(get_sum(3, 4))  # 7
```

If a function has no `return`, it returns `None`:
```python
def greet():
    print('hello')

result = greet()
print(result)  # None
```

Default parameters let you omit optional values:
```python
def get_sum(num_1, num_2=2):
    return num_1 + num_2

print(get_sum(3))  # 5
```

Calling a function with the wrong number of arguments raises a `TypeError`.

## Input and Common Built-ins
`input()` always returns a string. Convert it when you need numbers.

```python
name = input('What is your name? ')
print('Hello', name)

age = int(input('How old are you? '))
print(age + 1)
```

## Scope
- Local: defined inside a function.
- Enclosing: in an outer function when functions are nested.
- Global: defined at the top level.
- Built-in: names provided by Python itself.

```python
# Global scope
rate = 0.7

def outer():
    msg = 'Hello'
    def inner():
        print(msg)  # enclosing scope
    inner()

outer()
```

## Comparison Operators
```python
print(3 == 4)  # False
print(3 != 4)  # True
print(3 > 4)   # False
print(3 < 4)   # True
print(3 >= 4)  # False
print(3 <= 4)  # True
```

## Conditionals
```python
age = 16

if age >= 18:
    print('Adult')
elif age >= 13:
    print('Teen')
else:
    print('Child')
```

Nested conditionals are useful when a second condition depends on the first:
```python
is_citizen = True
age = 25

if is_citizen:
    if age >= 18:
        print('Eligible to vote')
```

## Truthy and Falsy Values
Falsy values include `None`, `False`, `0`, `0.0`, `''`, `[]`, `{}`, and `set()`.
All other values are truthy.

```python
print(bool(0))        # False
print(bool(''))       # False
print(bool('hello'))  # True
```

### Boolean Operators and Short-circuiting
- `and` returns the first falsy value or the last value.
- `or` returns the first truthy value or the last value.
- `not` flips truthiness.

```python
print(0 and 5)      # 0
print(0 or 5)       # 5
print(not '')       # True
```

## Lists
Lists are ordered and mutable.

```python
cities = ['Los Angeles', 'London', 'Tokyo']
print(cities[0])   # Los Angeles
print(cities[-1])  # Tokyo
```

Lists can be created with `list()`:
```python
print(list('Jessica'))  # ['J', 'e', 's', 's', 'i', 'c', 'a']
```

Lists are mutable:
```python
languages = ['Python', 'Java', 'C++']
languages[0] = 'JavaScript'
print(languages)
```

Accessing an invalid index raises `IndexError`.

### List Operations
```python
nums = [1, 2, 3]

nums.append(4)        # add one item
nums.extend([5, 6])   # add many items
nums.insert(1, 1.5)   # insert at index

nums.remove(2)        # removes first 2
last = nums.pop()     # removes and returns last item
nums.clear()          # remove all items
```

### Sorting
```python
nums = [19, 2, 35, 1]
nums.sort()           # in place
print(nums)           # [1, 2, 19, 35]

nums = [19, 2, 35, 1]
print(sorted(nums))   # new list
```

### Slicing and Unpacking
```python
desserts = ['cake', 'cookies', 'ice cream', 'pie']
print(desserts[1:3])  # ['cookies', 'ice cream']

name, *rest = ['Alice', 34, 'Rust Developer']
print(name)  # Alice
print(rest)  # [34, 'Rust Developer']
```

## Tuples
Tuples are ordered and immutable.

```python
developer = ('Alice', 34, 'Rust Developer')
print(developer[1])  # 34
```

Because tuples are immutable, item assignment raises `TypeError`.

Common tuple operations:
```python
numbers = (1, 2, 3, 4, 5)
print(numbers.count(2))  # 1
print(numbers.index(4))  # 3
print(sorted(numbers))   # [1, 2, 3, 4, 5]
```

## Loops
### for Loop
```python
languages = ['Rust', 'Java', 'Python']
for lang in languages:
    print(lang)
```

### while Loop
```python
secret = 3
guess = 0

while guess != secret:
    guess = int(input('Guess the number (1-5): '))
    if guess != secret:
        print('Wrong! Try again.')
```

### break and continue
```python
names = ['Jess', 'Naomi', 'Tom']

for name in names:
    if name == 'Naomi':
        break
    print(name)
```

Loop `else` runs only if the loop was not broken:
```python
words = ['sky', 'apple', 'rhythm']

for word in words:
    for letter in word:
        if letter.lower() in 'aeiou':
            print(f"{word} has vowel {letter}")
            break
    else:
        print(f"{word} has no vowels")
```

## range(), enumerate(), and zip()
`range()` generates a sequence of integers.

```python
for num in range(3):
    print(num)
```

`enumerate()` adds an index to items:
```python
languages = ['Spanish', 'English', 'Russian']
for index, language in enumerate(languages, start=1):
    print(index, language)
```

`zip()` iterates in parallel:
```python
developers = ['Naomi', 'Dario']
ids = [1, 2]

for name, dev_id in zip(developers, ids):
    print(name, dev_id)
```

## Comprehensions and Iterable Helpers
List comprehensions combine looping and filtering into one line.

```python
even_numbers = [num for num in range(21) if num % 2 == 0]
print(even_numbers)
```

`filter()` and `map()` return iterators, so wrap them in `list()` if needed.

```python
words = ['tree', 'sky', 'mountain']
long_words = list(filter(lambda w: len(w) > 4, words))
print(long_words)

celsius = [0, 10, 20]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print(fahrenheit)
```

`sum()` adds values in an iterable:
```python
print(sum([5, 10, 15]))        # 30
print(sum([5, 10, 15], 10))    # 40
```

## Lambda Functions
Lambdas are small anonymous functions, often used with `map()` or `filter()`.

```python
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4]
```

## Dictionaries
Dictionaries map keys to values. Keys must be immutable types.

```python
pizza = {
    'name': 'Margherita',
    'price': 8.9,
    'calories_per_slice': 250
}

print(pizza['name'])
pizza['price'] = 10.5
```

### dict() Constructor
```python
pizza = dict(name='Margherita', price=8.9)
```

### Common Dictionary Methods
```python
print(pizza.get('price', 0))
print(pizza.keys())
print(pizza.values())
print(pizza.items())

pizza.pop('price', None)

pizza.update({'price': 15, 'total_time': 25})
```

### Looping Over a Dictionary
```python
products = {'Laptop': 990, 'Tablet': 250}

for key in products:
    print(key)

for value in products.values():
    print(value)

for key, value in products.items():
    print(key, value)
```

## Sets
Sets store unique, unordered values. They cannot contain mutable items like lists.

```python
numbers = {1, 2, 3, 4}
empty_set = set()  # do not use {}
```

### Common Set Methods
```python
numbers.add(5)
numbers.remove(4)    # raises KeyError if not present
numbers.discard(99)  # safe removal
numbers.clear()
```

### Set Operations
```python
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print(set_a | set_b)  # union
print(set_a & set_b)  # intersection
print(set_a - set_b)  # difference
print(set_a ^ set_b)  # symmetric difference

print(set_a.issubset(set_b))
print(set_a.issuperset(set_b))
print(set_a.isdisjoint(set_b))
```

## Standard Library and Imports
Python ships with many built-in modules such as `math`, `random`, `re`, and `datetime`.

```python
import math
print(math.sqrt(36))
```

Aliases reduce typing or avoid name conflicts:
```python
import math as m
print(m.sqrt(36))
```

Import specific names when you only need a few items:
```python
from math import sin, cos, radians
angle = radians(40)
print(sin(angle))
print(cos(angle))
```

Avoid `from module import *` unless you control the module and know it will not pollute your namespace.

## __name__ and Script Entry Points
`__name__` is `'__main__'` when a file is run directly, and the module name when imported.

```python
if __name__ == '__main__':
    print('Run as a script')
```

## Common Errors and Debugging
Common errors:
- `SyntaxError`: invalid Python syntax.
- `NameError`: using a name that is not defined.
- `TypeError`: invalid operation for a type.
- `IndexError`: out-of-range index.
- `AttributeError`: missing attribute or method.

Debugging tips:
- Use `print()` to inspect values as code runs.
- Use `pdb` for step-by-step debugging.
- Use IDE debuggers with breakpoints and variable inspection.

## Exception Handling
Use `try` / `except` to handle errors gracefully.

```python
try:
    print(22 / 0)
except ZeroDivisionError:
    print('You cannot divide by zero')
```

Multiple exception blocks let you handle specific cases:
```python
try:
    number = int(input('Enter a number: '))
    print(22 / number)
except ZeroDivisionError:
    print('Zero is not allowed')
except ValueError:
    print('Please enter a valid number')
else:
    print('No errors occurred')
finally:
    print('Cleanup runs here')
```

Capture the exception object for details:
```python
try:
    value = int('not a number')
except ValueError as e:
    print(f'Caught error: {e}')
```

Raise custom errors when a condition should stop execution:
```python
class InvalidCredentialsError(Exception):
    pass

def login(username, password):
    if username != 'admin' or password != 'password123':
        raise InvalidCredentialsError('Invalid username or password')
    return f'Welcome, {username}!'
```

## Classes and Objects
A class is a blueprint for creating objects. Objects are instances of classes.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f'{self.name.upper()} says woof!')

dog = Dog('Jack', 3)
dog.bark()
```

### Instance vs Class Attributes
```python
class Dog:
    species = 'French Bulldog'  # class attribute

    def __init__(self, name):
        self.name = name         # instance attribute

print(Dog.species)
print(Dog('Jack').species)
```

### Dunder (Magic) Methods
Dunder methods enable built-in behavior like `len()` and `str()`.

```python
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __len__(self):
        return self.pages

    def __str__(self):
        return f"'{self.title}' has {self.pages} pages"

book = Book('Built Wealth Like a Boss', 420)
print(len(book))
print(str(book))
```

## OOP Principles
### Encapsulation
Encapsulation bundles data and behavior, and hides internal details.

```python
class Wallet:
    def __init__(self, balance):
        self.__balance = balance  # name-mangled

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
```

### Getters and Setters with @property
Properties allow controlled access to attributes while using dot notation.

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError('Radius must be positive')
        self._radius = value
```

### Inheritance
Inheritance allows a child class to reuse and extend a parent class.

```python
class Parent:
    def greet(self):
        return 'Hello from Parent'

class Child(Parent):
    def greet(self):
        return 'Hello from Child'
```

### Polymorphism
Different classes can implement the same method name with different behavior.

```python
class A:
    def action(self):
        return 'A'

class B:
    def action(self):
        return 'B'
```

### Abstraction
Abstraction hides details and exposes only necessary behavior.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
```

### Name Mangling
Double underscore prefixes are name-mangled to avoid accidental overrides.

```python
class Parent:
    def __init__(self):
        self.__data = 'Parent data'

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__data = 'Child data'

c = Child()
print(c.__dict__)  # {'_Parent__data': 'Parent data', '_Child__data': 'Child data'}
```

## Algorithms and Big O
Algorithms are step-by-step procedures to solve problems. Big O notation describes how time or space grows as input size increases.

Common time complexities:
- O(1): constant time
- O(log n): logarithmic time
- O(n): linear time
- O(n log n): log-linear time
- O(n^2): quadratic time

## Data Structures
### Arrays and Lists
Python lists are dynamic arrays that grow as needed.

Time complexity (average):
- Access: O(1)
- Append: O(1)
- Insert in middle: O(n)
- Delete in middle: O(n)

### Stacks
Last-in, first-out (LIFO). Use a list as a stack.

```python
stack = []
stack.append(1)
stack.append(2)
print(stack.pop())  # 2
```

### Queues
First-in, first-out (FIFO). Use `collections.deque` for efficiency.

```python
from collections import deque
queue = deque()
queue.append(1)
queue.append(2)
print(queue.popleft())  # 1
```

### Linked Lists
Nodes hold data and references to the next (and possibly previous) nodes. Good for frequent insertions, but no O(1) random access.

### Hash Maps and Sets
Dictionaries and sets use hashing for average O(1) insert, lookup, and delete.

Hash collisions happen when different keys map to the same index. Common strategies:
- Chaining: store collisions in a list at each bucket.
- Open addressing: probe for another open slot.

## Searching Algorithms
### Linear Search
Check each item until you find the target. Time complexity O(n).

### Binary Search
Repeatedly split the sorted list in half. Time complexity O(log n). The list must be sorted.

## Sorting Algorithms
### Merge Sort
Divide-and-conquer sorting algorithm with O(n log n) time and O(n) space.

## Graphs
Graphs are nodes (vertices) connected by edges.

Types:
- Directed or undirected
- Weighted or unweighted
- Cyclic or acyclic

Traversals:
- BFS (queue, level-order)
- DFS (stack/recursion, depth-first)

Representations:
- Adjacency list
- Adjacency matrix

## Trees and Tries
A tree is a connected, acyclic graph.

Common trees:
- Binary Tree
- Binary Search Tree (BST)

Tries (prefix trees) store strings by character and are efficient for autocomplete.

## Priority Queues and Heaps
A priority queue removes items based on priority. Heaps are common implementations.

```python
import heapq

heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)

print(heapq.heappop(heap))  # 1
```

## Dynamic Programming
Dynamic programming solves problems by storing solutions to overlapping subproblems.

### Memoization (Top-Down)
```python
def climb_stairs_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 2:
        return n
    memo[n] = climb_stairs_memo(n-1, memo) + climb_stairs_memo(n-2, memo)
    return memo[n]
```

### Tabulation (Bottom-Up)
```python
def climb_stairs_tabulation(n):
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
```

## Assignment
- Review each section.
- Run or rewrite at least one example from every major topic.
- Write a short summary in your own words for the topics you find hardest.
