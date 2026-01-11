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
