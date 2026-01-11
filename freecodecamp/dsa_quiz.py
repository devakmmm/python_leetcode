"""
Data Structures Quiz Answers with Explanations.
"""

ANSWERS = [
    {
        "question": 1,
        "answer": "How the time or space grows relative to input size (an upper bound).",
        "explanation": "Big O describes the growth rate of time/space as input size increases, typically as an upper bound."
    },
    {
        "question": 2,
        "answer": "Clarify the problem and constraints with examples and edge cases.",
        "explanation": "Understanding requirements and edge cases prevents incorrect assumptions and guides a correct solution."
    },
    {
        "question": 3,
        "answer": "Dynamic arrays can grow or shrink by resizing; static arrays have a fixed size.",
        "explanation": "Static arrays allocate a fixed block, while dynamic arrays resize (often by copying) when capacity is exceeded."
    },
    {
        "question": 4,
        "answer": "O(1) amortized.",
        "explanation": "Most appends are constant time; occasional resizes cost O(n) but are spread across many appends."
    },
    {
        "question": 5,
        "answer": "You must traverse from the head node to the k-th node one by one.",
        "explanation": "Singly linked lists only store a next pointer, so you must walk nodes sequentially to reach index k."
    },
    {
        "question": 6,
        "answer": "Pointers to both next and previous nodes enabling backward traversal.",
        "explanation": "Doubly linked lists store both next and previous references, allowing reverse traversal."
    },
    {
        "question": 7,
        "answer": "Last In, First Out (LIFO) with push and pop at the top.",
        "explanation": "Stacks add and remove from one end, so the most recent item is removed first."
    },
    {
        "question": 8,
        "answer": "dequeue",
        "explanation": "Dequeue removes the front element in a queue."
    },
    {
        "question": 9,
        "answer": "O(1) on average with a good hash function and low load factor.",
        "explanation": "Hash maps distribute keys across buckets so average lookup is constant time."
    },
    {
        "question": 10,
        "answer": "It stores only unique elements (no duplicates).",
        "explanation": "A set enforces uniqueness; duplicates are ignored or overwrite existing entries depending on implementation."
    },
    {
        "question": 11,
        "answer": "O(n)",
        "explanation": "Inserting at index i shifts later elements, which can move up to n items."
    },
    {
        "question": 12,
        "answer": "O(1)",
        "explanation": "Inserting at the head just updates a couple of pointers."
    },
    {
        "question": 13,
        "answer": "peek",
        "explanation": "Peek returns the top element without removing it."
    },
    {
        "question": 14,
        "answer": "First In, First Out (FIFO) with enqueue at the back and dequeue at the front.",
        "explanation": "Queues process items in arrival order: add at back, remove from front."
    },
    {
        "question": 15,
        "answer": "When two different keys produce the same hash index.",
        "explanation": "A collision occurs when distinct keys map to the same bucket index."
    },
    {
        "question": 16,
        "answer": "To keep the load factor low so that average operations remain O(1).",
        "explanation": "Resizing spreads keys across more buckets, reducing collisions and keeping operations fast."
    },
    {
        "question": 17,
        "answer": "Membership tests are typically O(1) on average.",
        "explanation": "Sets are usually hash-based, so membership checks are constant time on average."
    },
    {
        "question": 18,
        "answer": "O(n^2)",
        "explanation": "Quadratic growth eventually dominates n log n as n becomes large."
    },
    {
        "question": 19,
        "answer": "Analyze its time/space complexity and optimize identified bottlenecks.",
        "explanation": "Profiling and complexity analysis show where optimization will actually help."
    },
    {
        "question": 20,
        "answer": "How memory usage grows relative to input size.",
        "explanation": "Space complexity measures how memory requirements scale with input size."
    },
]


def get_answers():
    """Return the quiz answers with explanations."""
    return ANSWERS
