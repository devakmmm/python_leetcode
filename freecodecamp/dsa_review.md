# Data Structures Review

Short explanations and tiny Python snippets to make the concepts stick.

## 1) Big O notation
**Answer:** How the time or space grows relative to input size (an upper bound).

**Explanation:** Big O focuses on growth as input gets large, not exact seconds on one machine.

```python
# O(n): one pass through the list
def contains(nums, target):
    for n in nums:
        if n == target:
            return True
    return False
```

## 2) Best first step in a challenge
**Answer:** Clarify the problem and constraints with examples and edge cases.

**Explanation:** Clear requirements prevent wrong assumptions and shape the right solution.

```python
# Example: clarify inputs/outputs before coding
# Input: list of ints, may be empty
# Output: max value or None if empty
```

## 3) Dynamic vs static arrays
**Answer:** Dynamic arrays can grow or shrink by resizing; static arrays have a fixed size.

**Explanation:** Dynamic arrays allocate new storage and copy items when capacity is exceeded.

```python
# Python list behaves like a dynamic array
arr = [1, 2, 3]
arr.append(4)  # may trigger a resize internally
```

## 4) Append to dynamic array (amortized)
**Answer:** O(1) amortized.

**Explanation:** Most appends are constant time; occasional resizes cost more but are rare.

```python
# Amortized O(1): repeated appends
arr = []
for i in range(1000):
    arr.append(i)
```

## 5) Index access in singly linked list
**Answer:** You must traverse from the head node to the k-th node one by one.

**Explanation:** No random access; only a next pointer exists.

```python
class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt

# Access index k by walking nodes
```

## 6) Doubly linked list feature
**Answer:** Pointers to both next and previous nodes enabling backward traversal.

**Explanation:** Each node has `next` and `prev` references.

```python
class DNode:
    def __init__(self, val, prev=None, nxt=None):
        self.val = val
        self.prev = prev
        self.next = nxt
```

## 7) Stack definition
**Answer:** Last In, First Out (LIFO) with push and pop at the top.

**Explanation:** The most recently added item is removed first.

```python
stack = []
stack.append(10)  # push
stack.append(20)
stack.pop()       # returns 20
```

## 8) Queue front removal
**Answer:** dequeue.

**Explanation:** Dequeue removes the oldest item at the front.

```python
from collections import deque
q = deque([1, 2, 3])
q.popleft()  # dequeue -> 1
```

## 9) Hash map average lookup
**Answer:** O(1) on average with a good hash function and low load factor.

**Explanation:** Keys distribute across buckets to keep lookups fast.

```python
phone = {"ana": "555-0101", "bob": "555-0102"}
phone["ana"]  # average O(1)
```

## 10) Set guarantee
**Answer:** It stores only unique elements (no duplicates).

**Explanation:** Adding an existing element does not create a duplicate.

```python
s = {1, 2, 2, 3}
# s is {1, 2, 3}
```

## 11) Insert into dynamic array at index i
**Answer:** O(n)

**Explanation:** Elements to the right must be shifted.

```python
arr = [1, 2, 3, 4]
arr.insert(1, 99)  # shifts items to the right
```

## 12) Insert at head of singly linked list
**Answer:** O(1)

**Explanation:** Update head pointer; no traversal needed.

```python
head = Node(2)
head = Node(1, head)  # new head in O(1)
```

## 13) Read top of stack without removal
**Answer:** peek.

**Explanation:** Peek returns the top element without popping it.

```python
stack = [5, 7, 9]
stack[-1]  # peek -> 9
```

## 14) Queue definition
**Answer:** First In, First Out (FIFO) with enqueue at the back and dequeue at the front.

**Explanation:** Items are processed in arrival order.

```python
from collections import deque
q = deque()
q.append(1)   # enqueue
q.append(2)
q.popleft()  # dequeue -> 1
```

## 15) Hash collision
**Answer:** When two different keys produce the same hash index.

**Explanation:** Collisions are handled with chaining or open addressing.

```python
# Pseudocode idea of collision handling with buckets
buckets = [[] for _ in range(8)]
key = "abc"
index = hash(key) % len(buckets)
```

## 16) Why hash maps resize
**Answer:** To keep the load factor low so that average operations remain O(1).

**Explanation:** More buckets reduce collisions.

```python
# When size/capacity crosses a threshold, rehash into a larger table
```

## 17) Set membership complexity
**Answer:** Membership tests are typically O(1) on average.

**Explanation:** Hashing makes membership checks fast.

```python
s = {"x", "y", "z"}
"y" in s  # average O(1)
```

## 18) Complexity that grows faster than O(n log n)
**Answer:** O(n^2)

**Explanation:** Quadratic growth eventually dominates n log n.

```python
# O(n^2): nested loops
for i in range(n):
    for j in range(n):
        pass
```

## 19) Next step after brute force
**Answer:** Analyze its time/space complexity and optimize identified bottlenecks.

**Explanation:** Measure or reason about where the time goes before improving.

```python
# Compare approaches by complexity before optimizing
# O(n^2) -> O(n log n) or O(n) if possible
```

## 20) Space complexity
**Answer:** How memory usage grows relative to input size.

**Explanation:** It tracks extra memory as input increases.

```python
# O(n) space: store a copy of input
def copy_list(nums):
    return [n for n in nums]
```
