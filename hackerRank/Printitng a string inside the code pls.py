# We import the sys module to access standard input directly.
# This is useful in HackerRank because input is provided through STDIN rather than prompts.
# Using sys keeps the solution fast and avoids extra overhead.
import sys

# We read all input at once as a single string from STDIN.
# This avoids calling string methods like strip or split while still capturing the number.
# The int conversion below can handle surrounding whitespace on its own.
data = sys.stdin.read()

# We check whether any input was provided before converting it.
# This prevents a ValueError if the input is empty or missing in a test run.
# If data is empty, the program simply finishes without printing anything.
if data:
    # We convert the input text to an integer n.
    # The int constructor ignores leading and trailing whitespace, so no string method is required.
    # This value n is the upper bound of the sequence to print.
    n = int(data)

    # We loop from 1 to n inclusive using range.
    # Each iteration represents the next number that must appear in the output in order.
    # For example, if n is 3, the loop visits 1, 2, and 3.
    for i in range(1, n + 1):
        # We print the current number without a newline by setting end to an empty string.
        # This concatenates the digits directly so there are no spaces between them.
        # The final output for n equal to 3 will be 123 on a single line.
        print(i, end="")
