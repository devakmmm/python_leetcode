# Quick Sort (Fixed Version)

This version actually partitions the list around a pivot, recurses on both sides, and combines the results. It avoids undefined variables and makes progress toward termination.

```python
def quick_sort(int_list):
    if len(int_list) <= 1:
        return int_list

    pivot = int_list[0]
    left = [x for x in int_list[1:] if x < pivot]
    right = [x for x in int_list[1:] if x >= pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)
```
