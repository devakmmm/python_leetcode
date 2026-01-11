# Quick Sort (Fixed Version)

Quick sort is a good default when you want fast average performance and can accept that the worst case is slower. It is often used for in-memory sorting because it is typically fast in practice and has low extra memory usage compared to merge sort.

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

# Loop Walkthrough (Detailed)

Even though the code uses list comprehensions, each one is still a loop that scans the list once.

Example input:
- `int_list = [4, 10, 6, 14, 2, 1, 8, 5]`
- `pivot = 4`
- We loop over the rest: `[10, 6, 14, 2, 1, 8, 5]`

Left list comprehension (loop):
- Check `10 < 4` → no
- Check `6 < 4` → no
- Check `14 < 4` → no
- Check `2 < 4` → yes, add `2`
- Check `1 < 4` → yes, add `1`
- Check `8 < 4` → no
- Check `5 < 4` → no
- Result: `left = [2, 1]`

Right list comprehension (loop):
- Check `10 >= 4` → yes, add `10`
- Check `6 >= 4` → yes, add `6`
- Check `14 >= 4` → yes, add `14`
- Check `2 >= 4` → no
- Check `1 >= 4` → no
- Check `8 >= 4` → yes, add `8`
- Check `5 >= 4` → yes, add `5`
- Result: `right = [10, 6, 14, 8, 5]`

Then quick sort runs again on `left` and `right`, and finally combines:
- `sorted = quick_sort(left) + [pivot] + quick_sort(right)`
