# Merge Sort Step: Left Half

To split the array, take everything from the start up to (but not including) the midpoint. This creates the left half that merge sort will recursively sort.

```python
array = [8, 4, 2, 9, 5, 1]
mid_point = len(array) // 2
left_part = array[:mid_point]

```
