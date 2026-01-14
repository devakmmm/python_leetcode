# Python Study Notes (Part 4)

These sections cover advanced practice topics and the standard library.
Each section uses the pattern: explanation → code → explanation.

## File I/O — Text, JSON, CSV

Use `with` and explicit encoding for safe file handling.

```python
from pathlib import Path
import json

path = Path("data.json")
data = {"name": "Ada", "age": 36}
path.write_text(json.dumps(data), encoding="utf-8")

loaded = json.loads(path.read_text(encoding="utf-8"))
print(loaded["name"])
```

Output:
```
Ada
```

`Path.write_text` and `read_text` make simple file I/O concise. Use `json` for
structured data exchange.

## Packages and Imports — Layout and __init__

Packages are folders with an `__init__.py` file.

```python
# project/
#   mypkg/
#     __init__.py
#     utils.py
#
# utils.py
def add(a, b):
    return a + b

# __init__.py
from .utils import add
```

Output:
```
(no output; package layout and imports are defined)
```

Import from the package with `from mypkg import add`. Relative imports use a dot
prefix.

## Testing — pytest basics

Tests make your code reliable and refactor‑safe.

```python
# test_math.py
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
```

Output:
```
(no output; pytest reports passing tests)
```

Run with `pytest`. A failing assertion tells you exactly where behavior differs
from expectation.

## Logging — Structured visibility

Logging is better than print for real apps.

```python
import logging

logging.basicConfig(level=logging.INFO)
logging.info("App started")
```

Output:
```
INFO:root:App started
```

You can route logs to files and include timestamps, levels, and modules.

## Debugging — pdb

Use the debugger to inspect state step‑by‑step.

```python
def buggy():
    x = 10
    y = 0
    import pdb; pdb.set_trace()
    return x / y
```

Output:
```
(enters pdb; if continued, ZeroDivisionError)
```

`pdb` lets you step, inspect variables, and evaluate expressions before a crash.

## Performance — Big‑O and data structure choice

Pick the right structure for the job.

```python
nums = list(range(100000))
nums_set = set(nums)

print(99999 in nums)     # O(n)
print(99999 in nums_set) # O(1) average
```

Output:
```
True
True
```

List membership is linear; set membership is constant time on average.

## Standard Library — collections, itertools, functools, datetime

Python’s batteries‑included tools save time and code.

```python
from collections import Counter, deque
from itertools import islice
from functools import lru_cache
from datetime import datetime

counts = Counter("mississippi")
q = deque([1, 2, 3])
q.appendleft(0)

first_three = list(islice(range(10), 3))

@lru_cache(maxsize=None)
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)

print(datetime.now().isoformat())
```

Output (example):
```
2024-01-01T12:34:56.789012
```

`Counter` counts items, `deque` is a fast queue, `islice` slices iterators,
`lru_cache` memoizes functions, and `datetime` handles time.

## Concurrency — threads, processes, async

Choose the right model for the workload.

```python
import threading

def worker():
    print("work")

t = threading.Thread(target=worker)
t.start()
t.join()
```

Output:
```
work
```

Threads help with I/O‑bound tasks, processes help with CPU‑bound tasks, and
`asyncio` is great for high‑concurrency I/O.

## Project Hygiene — venv, requirements, style

Keep projects reproducible and readable.

```python
# Create and activate a venv
# python3 -m venv .venv
# source .venv/bin/activate

# Save dependencies
# pip freeze > requirements.txt
```

Output:
```
(no output; shell commands run in a terminal)
```

Use PEP 8 style, meaningful names, and small functions. Consistent formatting
makes collaboration easier.
