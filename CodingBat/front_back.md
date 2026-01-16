# front_back - Study Notes

## Problem
Given a string, return a new string where the first and last chars have been exchanged.
If the string length is 0 or 1, return the string unchanged.

## Primary Python Solution
```python
def front_back(s):
    if len(s) <= 1:
        return s
    mid = s[1:len(s) - 1]
    return s[len(s) - 1] + mid + s[0]
```

## Why This Works
- The edge case is length 0 or 1; swapping does nothing, so return as-is.
- `mid` keeps all characters except the first and last.
- The new string is last + mid + first.
- Strings are immutable in Python, so we build a new string instead of swapping in-place.

## Alternative Answers (Same Behavior)
### Alternative 1: Use negative indexing and slicing
```python
def front_back(s):
    if len(s) <= 1:
        return s
    return s[-1] + s[1:-1] + s[0]
```

### Alternative 2: Convert to list and swap
```python
def front_back(s):
    if len(s) <= 1:
        return s
    chars = list(s)
    chars[0], chars[-1] = chars[-1], chars[0]
    return "".join(chars)
```

## Slicing: One-Paragraph Guide With Examples
Slicing uses the form `s[start:stop:step]`, where `start` is inclusive, `stop` is exclusive, and `step` controls the stride; all parts are optional and may be negative for counting from the end. For `s = "hello"`, `s[1:4]` is `"ell"`, `s[:2]` is `"he"`, `s[2:]` is `"llo"`, `s[-1]` is `"o"`, `s[1:-1]` is `"ell"`, and `s[::-1]` is `"olleh"`. The exclusive `stop` is a frequent interview bug: `s[1:len(s)-1]` is the same as `s[1:-1]`, but `s[1:len(s)]` includes the last char while `s[1:-0]` is empty because `-0` is `0`. Slicing always returns a new string, so it is O(k) for a slice of length k.

## Interview Notes (FAANG/LeetCode Mindset)
- Edge cases: empty string, length 1, length 2.
- Complexity: O(n) time to build a new string, O(n) space for the result.
- Immutability: strings cannot be modified in place in Python; list conversion is a common workaround.
- Off-by-one safety: be precise about inclusive/exclusive bounds.
- Prefer clarity over cleverness unless asked to optimize.

## Quick Self-Check Tests
```python
assert front_back("code") == "eodc"
assert front_back("a") == "a"
assert front_back("ab") == "ba"
assert front_back("") == ""
```

## Related Practice Topics
- String reversal with slicing and two pointers
- Palindrome checks and transformations
- Substring extraction and window problems
- Two-sum style thinking for indexes and bounds
- Character frequency counting (hash maps)
