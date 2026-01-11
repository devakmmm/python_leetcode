# Merge Sort Step: Left Half

To split the array, take everything from the start up to (but not including) the midpoint. This creates the left half that merge sort will recursively sort.

```python
array = [8, 4, 2, 9, 5, 1]
mid_point = len(array) // 2
left_part = array[:mid_point]
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

# Loop Walkthrough (Detailed)

These loops are where the actual merge happens. The idea is to compare the current smallest values from the left and right halves and write the smaller one into the main array.

Example halves:
- `left_part = [2, 6, 9]`
- `right_part = [1, 5, 8]`
- `array = [?, ?, ?, ?, ?, ?]`

Main merge loop:
- Start: `left_array_index = 0`, `right_array_index = 0`, `sorted_index = 0`
- Compare `2` (left) vs `1` (right) → write `1` to `array[0]`, move `right_array_index` to `1`
- Compare `2` vs `5` → write `2` to `array[1]`, move `left_array_index` to `1`
- Compare `6` vs `5` → write `5` to `array[2]`, move `right_array_index` to `2`
- Compare `6` vs `8` → write `6` to `array[3]`, move `left_array_index` to `2`
- Compare `9` vs `8` → write `8` to `array[4]`, move `right_array_index` to `3`
- Now `right_part` is exhausted (index 3 == len 3). Exit loop.

Leftover loops:
- Leftover left items loop copies remaining `9` into `array[5]`.
- Rightover right items loop does nothing in this case because `right_part` is already exhausted.

Result:
- `array = [1, 2, 5, 6, 8, 9]`

# Shorter Merge Sort (Returns a New List)

This version is shorter and more like the quick sort style. It returns a new sorted list instead of sorting in place.

```python
def merge_sort_short(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = merge_sort_short(array[:mid])
    right = merge_sort_short(array[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result
```
