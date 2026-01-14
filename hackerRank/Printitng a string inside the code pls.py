import sys

# Read the integer n from standard input.
n_line = sys.stdin.readline().strip()
if n_line:
    n = int(n_line)

    # Print numbers from 1 to n without spaces or string methods like join.
    for i in range(1, n + 1):
        print(i, end="")
