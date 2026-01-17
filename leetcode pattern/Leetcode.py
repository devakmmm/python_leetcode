"""
LeetCode pattern recognition notes (based on the Bitflip pattern guide).

How pattern recognition works
1) Check constraints (time/space feasibility)
   - Small n (<= 20): brute force, backtracking, recursion, 2^n / n! ok.
   - Medium n (10^3 to 10^6): O(n) or O(n log n), DP, greedy, two pointers, heaps.
   - Large n (>= 10^7): O(log n) or O(1), binary search or math formulas.

2) Analyze input format (data structure hints)
   - Tree/Binary Tree/BST: DFS for paths/recursion; BFS for level order or shortest path.
   - Graph: BFS for shortest path; DFS for connected components; Union Find for groups.
   - 2D grid: DFS/BFS for islands; Union Find for regions; DP for path counting.
   - Sorted array: two pointers, binary search, greedy.
   - String: two pointers (palindrome), sliding window (substring), trie (prefix), stack.
   - Linked list: fast/slow pointers, dummy nodes, cycle detection.

3) Analyze output format (what must be produced)
   - List of lists (subsets, combinations, paths): backtracking with recursion.
   - Single number (max/min profit, cost, ways, jumps): DP or greedy.
   - In-place modification: two pointers.
   - Ordered list (sorted or dependency order): sorting, heap, or topological sort.

4) Keyword pattern recognition (question phrasing hints)
   - DP: "number of ways", "maximum/minimum", "can you reach", "longest/shortest".
   - Two pointers: "palindrome", "sorted array", "target sum", "remove duplicates".
   - Sliding window: "substring/subarray with condition", "max/min window", "contains all".
   - Heap: "k largest/smallest", "top k", "median", "priority".
   - Stack: "parentheses", "valid expression", "nested structure", "undo".
   - Monotonic stack: "next greater/smaller".
   - Hash map: "count frequency", "find duplicates", "anagram".
   - Trie: "word search", "prefix".
   - Greedy: "minimum operations", "local optimal choice", "interval scheduling".
   - Union Find: "connected components", "number of groups".
   - Binary search: "kth element", "search in sorted", "minimize maximum",
     "first/last occurrence".
   - Bit manipulation: "xor", "single number", "power of 2".
   - Math/geometry: "gcd/lcm", "prime", "angle", "coordinate".
   - Game theory: "optimal strategy", "win/lose", "minimax".

When to use certain patterns (quick mapping)
- Backtracking: generate all combinations/permutations/paths.
- Two pointers: sorted arrays, in-place array edits, palindromes, pair sums.
- Sliding window: contiguous substring/subarray with constraints.
- BFS/DFS: traversal, shortest path in unweighted graphs, islands/regions.
- DP: optimize min/max or count ways with overlapping subproblems.
- Greedy: locally optimal choices lead to global optimal result.
- Heap: maintain top-k or dynamic median.
- Stack/Monotonic stack: next greater/smaller, parsing, matching brackets.
- Union Find: dynamic connectivity, number of components.
- Binary search: monotonic property or answer-space search.

Hints to look for in questions
- Constraints that rule out brute force.
- Keywords above (especially "max/min", "ways", "kth", "next greater").
- Input/Output structure that implies recursion or traversal.
- Any statement like "in-place", "sorted", "shortest path", or "all subsets".
"""
