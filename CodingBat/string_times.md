# string_times - What Went Wrong

## The Problem
Given a string and a non-negative integer `n`, return a larger string that is `n` copies of the original string.

## Why This Version Is Wrong
```python
def string_times(s, n):
    result = list(s)
    for i in range(n):
        result = result.append(s)
    return result
```
- `list.append()` returns `None`, so `result = result.append(s)` overwrites `result` with `None` after the first loop.
- Starting with `list(s)` changes the type: you end up with a list of characters, not a string.
- Even if `append` were used correctly, appending `s` to a list would create a list of strings, not a combined string.

## Correct Python Solution (Simple and Idiomatic)
```python
def string_times(s, n):
    return s * n
```

## Correct Solution (Loop Version)
```python
def string_times(s, n):
    result = ""
    for _ in range(n):
        result += s
    return result
```

## Quick Examples
```text
string_times("Hi", 2) -> "HiHi"
string_times("Hi", 3) -> "HiHiHi"
string_times("abc", 0) -> ""
```

## Key Takeaways
- `append` mutates a list and returns `None`.
- If you want repetition, use `s * n` or build a string with `+=`.
- Always check the type of your accumulator (`""` for strings, `[]` for lists).

s = "code"
lst = list(s)

print(lst)          # ['c', 'o', 'd', 'e']
print(type(lst))    # <class 'list'>

lst[0] = 'C'
print(lst)          # ['C', 'o', 'd', 'e']
print(s)            # "code" (original string unchanged)

lst.append("X")
print(lst)          # ['C', 'o', 'd', 'e', 'X']
