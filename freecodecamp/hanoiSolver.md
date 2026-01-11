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
