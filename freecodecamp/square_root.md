# Bisection Method Square Root

This function finds the square root of a number by repeatedly halving an interval
until the interval is small enough to meet a tolerance.

## Key ideas
- If the input is negative, there is no real square root.
- If the input is 0 or 1, the square root is the number itself.
- For any other positive number, keep halving the interval until it is small.
- If the method does not converge fast enough, return `None`.

## Implementation

```python
"""Square root using the bisection method."""


def square_root_bisection(square_target, tolerance=0.01, max_iterations=100):
    """Return the square root using bisection, or None if it fails to converge."""
    if square_target < 0:
        raise ValueError(
            "Square root of negative number is not defined in real numbers"
        )

    if square_target in (0, 1):
        print(f"The square root of {square_target} is {square_target}")
        return square_target

    low = 0.0
    high = square_target if square_target >= 1 else 1.0
    root = None

    for _ in range(max_iterations):
        mid = (low + high) / 2
        guess = mid * mid

        if guess == square_target:
            root = mid
            print(f"The square root of {square_target} is approximately {root}")
            return root

        if guess > square_target:
            high = mid
        else:
            low = mid

        if (high - low) <= tolerance:
            root = (low + high) / 2
            print(f"The square root of {square_target} is approximately {root}")
            return root

    print(f"Failed to converge within {max_iterations} iterations")
    return None
```

## Example

```python
square_root_bisection(9)
# The square root of 9 is approximately 3.0

square_root_bisection(2, tolerance=0.001)
# The square root of 2 is approximately 1.414...

square_root_bisection(-4)
# ValueError: Square root of negative number is not defined in real numbers
```
