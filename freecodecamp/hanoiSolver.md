# Tower of Hanoi Solver

The Tower of Hanoi puzzle starts with all disks on the first rod, smallest on top. The goal is to move them to the last rod, following the rules: move only the top disk, move one disk at a time, and never place a larger disk on a smaller one.

The recursive solution always uses **2^n - 1** moves for `n` disks:
- Move `n-1` disks to the auxiliary rod.
- Move the largest disk to the target rod.
- Move `n-1` disks from auxiliary to target.

## Code

```python
def hanoi_solver(total_disks):
    rods = [list(range(total_disks, 0, -1)), [], []]
    moves = []

    def snapshot():
        return " ".join(str(rod) for rod in rods)

    def move(n, src, dst, aux):
        if n == 0:
            return
        move(n - 1, src, aux, dst)
        rods[dst].append(rods[src].pop())
        moves.append(snapshot())
        move(n - 1, aux, dst, src)

    moves.append(snapshot())
    move(total_disks, 0, 2, 1)
    return "\n".join(moves)
```

## Line-by-line Explanation

- `def hanoi_solver(total_disks):` Defines a function that will compute all moves for a Tower of Hanoi puzzle with `total_disks` disks.
- `rods = [list(range(total_disks, 0, -1)), [], []]` Creates the three rods as lists; the first rod starts with disks in descending order (largest to smallest) so the smallest disk is on top.
- `moves = []` Initializes a list to store each snapshot of the rods after a move.
- `def snapshot():` Starts a helper function that will capture the current state of all rods as a single string.
- `return " ".join(str(rod) for rod in rods)` Converts each rod list to a string and joins them with spaces so each line matches the required output format.
- `def move(n, src, dst, aux):` Starts the recursive helper that moves `n` disks from rod `src` to rod `dst` using `aux` as the temporary rod.
- `if n == 0:` Defines the base case: if there are no disks to move, stop recursion.
- `return` Exits the function in the base case, performing no action.
- `move(n - 1, src, aux, dst)` Recursively moves the top `n-1` disks from `src` to `aux` so the largest disk is free.
- `rods[dst].append(rods[src].pop())` Moves the top disk from the source rod to the destination rod by popping from `src` and appending to `dst`.
- `moves.append(snapshot())` Records the new state immediately after a disk move.
- `move(n - 1, aux, dst, src)` Recursively moves the `n-1` disks from `aux` onto `dst` to stack them on the largest disk.
- `moves.append(snapshot())` Captures the starting configuration before any moves are made.
- `move(total_disks, 0, 2, 1)` Kicks off the full solution: move all disks from rod 0 to rod 2 using rod 1 as auxiliary.
- `return "\n".join(moves)` Joins all recorded snapshots with newlines to produce the final multi-line output string.

## Example

```python
print(hanoi_solver(3))
```

Output:

```
[3, 2, 1] [] []
[3, 2] [] [1]
[3] [2] [1]
[3] [2, 1] []
[] [2, 1] [3]
[1] [2] [3]
[1] [] [3, 2]
[] [] [3, 2, 1]
```

## Why This Works

- **Correctness:** The recursive pattern always respects the rules, because it only moves the smallest available disk at each step.
- **Moves count:** For `n` disks, the recurrence is `T(n) = 2*T(n-1) + 1`, which solves to `2^n - 1`.
- **Output format:** Each line shows the three rods as lists, matching the required example.
