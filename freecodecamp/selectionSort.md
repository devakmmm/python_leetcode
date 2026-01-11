# Selection Sort

Selection sort is best for very small lists or when swaps are expensive and you want to minimize them. It is easy to implement and understand, but it is slow for large inputs.

Selection sort finds the smallest item in the unsorted part of the list and swaps it into the next position. It repeats this until the list is fully sorted.

## Implementation

```python
def selection_sort(items):
    for i in range(len(items)):
        min_index = i
        for j in range(i + 1, len(items)):
            if items[j] < items[min_index]:
                min_index = j
        if min_index != i:
            items[i], items[min_index] = items[min_index], items[i]
    return items
```

## Loop Walkthrough (Detailed)

Example input:
- `items = [4, 10, 6, 14, 2, 1, 8, 5]`

Outer loop `i = 0` (find smallest in indices 0..end):
- Start `min_index = 0` (value `4`)
- Compare `10` to `4` → no change
- Compare `6` to `4` → no change
- Compare `14` to `4` → no change
- Compare `2` to `4` → update `min_index = 4`
- Compare `1` to `2` → update `min_index = 5`
- Compare `8` to `1` → no change
- Compare `5` to `1` → no change
- Swap index `0` and `5`: list becomes `[1, 10, 6, 14, 2, 4, 8, 5]`

Outer loop `i = 1` (find smallest in indices 1..end):
- Start `min_index = 1` (value `10`)
- Compare `6` to `10` → update `min_index = 2`
- Compare `14` to `6` → no change
- Compare `2` to `6` → update `min_index = 4`
- Compare `4` to `2` → no change
- Compare `8` to `2` → no change
- Compare `5` to `2` → no change
- Swap index `1` and `4`: list becomes `[1, 2, 6, 14, 10, 4, 8, 5]`

The algorithm keeps moving `i` forward, each time placing the smallest remaining element into its correct position.

## Example Run

```python
numbers = [4, 10, 6, 14, 2, 1, 8, 5]
selection_sort(numbers)
print(numbers)  # [1, 2, 4, 5, 6, 8, 10, 14]
```
