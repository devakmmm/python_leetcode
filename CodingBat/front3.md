# front3 - Study Notes

## Problem
Given a string, return a new string which is 3 copies of the "front" of the string.
The "front" is the first 3 chars, or whatever is there if the string is shorter than 3.

## Primary Python Solution
```python
def front3(s):
    front_end = 3
    if len(s) < front_end:
        front_end = len(s)
    front = s[:front_end]
    return front + front + front
```

## Why This Works
- The "front" is defined as up to 3 characters, so `front_end` starts at 3.
- If the string is shorter than 3, we clamp `front_end` to the string length.
- `s[:front_end]` safely returns the first 0..3 characters without errors.
- Concatenating `front` three times builds the required output.

## Alternative Answers (Same Behavior)
### Alternative 1: Use `min` to clamp the length
```python
def front3(s):
    front = s[:min(3, len(s))]
    return front * 3
```

### Alternative 2: Early return for short strings
```python
def front3(s):
    if len(s) < 3:
        return s * 3
    return s[:3] * 3
```

### Alternative 3: Defensive style with explicit empty string handling
```python
def front3(s):
    if not s:
        return ""
    front = s[:3]
    return front * 3
```

## Examples and Walkthroughs
```text
Input: "Java"
front = "Jav"
Output: "JavJavJav"

Input: "Chocolate"
front = "Cho"
Output: "ChoChoCho"

Input: "ab"
front = "ab"
Output: "ababab"

Input: ""
front = ""
Output: ""
```
Key idea: slicing never throws an index error, so `s[:3]` is always safe, even for short strings.

## Slicing Deep Dive (Mini-Guide With Examples)
Slicing syntax is `s[start:stop:step]` where `start` is inclusive, `stop` is exclusive, and `step` controls stride. All parts are optional. For `s = "python"`, `s[:3]` is `"pyt"`, `s[3:]` is `"hon"`, `s[1:5]` is `"ytho"`, `s[:-1]` is `"pytho"`, and `s[::-1]` is `"nohtyp"`. Negative indexes count from the end, so `s[-2:]` is `"on"`. A common interview pitfall is confusing inclusive/exclusive bounds: `s[:3]` gives 3 characters (indexes 0,1,2), while `s[:len(s)]` gives the whole string; `s[:len(s)-1]` drops the last character. Slicing returns a new string, so it costs O(k) time and space for a slice of length k.

## Interview Notes (FAANG/LeetCode Mindset)
- **Edge cases:** empty string, length 1, length 2.
- **Complexity:** O(n) time to build the result (n is the output length), O(n) space for the new string.
- **Clarity:** `s[:3] * 3` is compact and idiomatic, but ensure you handle short strings.
- **Readability:** using `min(3, len(s))` makes the intent explicit.
- **Immutability:** strings are immutable; all transformations create new strings.

## Common Mistakes
- Using `s[0:3]` is fine, but `s[0:2]` would be wrong (off-by-one).
- Writing `s[3]` for short strings raises `IndexError`.
- Forgetting to handle `""` or length < 3.
- Returning `front * 3` without defining `front` correctly.

## Quick Self-Check Tests
```python
assert front3("Java") == "JavJavJav"
assert front3("Chocolate") == "ChoChoCho"
assert front3("abc") == "abcabcabc"
assert front3("ab") == "ababab"
assert front3("a") == "aaa"
assert front3("") == ""
```

## Related Practice Topics
- String repetition and pattern building
- Substring extraction and bounds checking
- Two-pointer and sliding-window patterns
- Palindrome construction and checks
- String compression and run-length encoding
