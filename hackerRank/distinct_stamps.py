# We import sys so we can access standard input in a fast, reliable way.
# This matches HackerRank's execution model where input is piped into the program.
# Keeping input handling explicit also makes the code easier to test locally.
import sys

# We read the first line, which should contain the number of stamps.
# Using readline keeps the memory footprint small since only one line is read at a time.
# This line will be converted to an integer on the next step.
n_line = sys.stdin.readline()

# We convert the line to an integer to get the count of stamp entries.
# If the line is empty, we fall back to zero to avoid a ValueError.
# This protects the program in case the input is missing or truncated.
n = int(n_line) if n_line else 0

# We create an empty set to store unique country names.
# A set automatically ignores duplicates, which is exactly what this problem needs.
# The add method will be used to insert each country as we read it.
countries = set()

# We loop exactly n times to read each stamp's country name.
# The underscore is used because the loop counter itself is not needed.
# Each iteration corresponds to one country line in the input.
for _ in range(n):
    # We read one country name and remove only the trailing newline character.
    # This keeps the country name clean while preserving internal spaces.
    # Using rstrip('\n') ensures consistent matching inside the set.
    country = sys.stdin.readline().rstrip("\n")

    # We add the country name to the set of unique countries.
    # If the country is already present, the set stays the same.
    # This is the core use of the .add() operation requested in the prompt.
    countries.add(country)

# We print the number of unique countries collected in the set.
# The length of the set is the count of distinct country names.
# This is the single value required by the output format.
print(len(countries))

# Sample Input:
# 7
# UK
# China
# USA
# France
# New Zealand
# UK
# France
# Sample Output:
# 5
