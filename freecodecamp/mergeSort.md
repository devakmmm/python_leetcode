# Merge Sort Step: Left Half

To split the array, take everything from the start up to (but not including) the midpoint. This creates the left half that merge sort will recursively sort.

```python
array = [8, 4, 2, 9, 5, 1]
mid_point = len(array) // 2
left_part = array[:mid_point]
```

```

# Merge Sort Full Example

This shows a complete merge sort implementation and a small runnable example that prints the array before and after sorting.

```python
def merge_sort(array):
    if len(array) <= 1:
        return

    middle_point = len(array) // 2
    left_part = array[:middle_point]
    right_part = array[middle_point:]

    merge_sort(left_part)
    merge_sort(right_part)

    left_array_index = 0
    right_array_index = 0
    sorted_index = 0

    while left_array_index < len(left_part) and right_array_index < len(right_part):
        if left_part[left_array_index] < right_part[right_array_index]:
            array[sorted_index] = left_part[left_array_index]
            left_array_index += 1
        else:
            array[sorted_index] = right_part[right_array_index]
            right_array_index += 1
        sorted_index += 1

    while left_array_index < len(left_part):
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_index += 1

    while right_array_index < len(right_part):
        array[sorted_index] = right_part[right_array_index]
        right_array_index += 1
        sorted_index += 1


if __name__ == '__main__':
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]
    print('Unsorted array: ')
    print(numbers)
    merge_sort(numbers)
    print('Sorted array: ')
    print(numbers)
```
