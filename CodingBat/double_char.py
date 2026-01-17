def double_char(s: str) -> str:
    """Return a new string where every character from s appears twice.

    Example walkthrough for s="Hi-There":
    - Start with an empty list of pieces: []
    - Read 'H' -> append 'H', 'H' => ["H", "H"]
    - Read 'i' -> append 'i', 'i' => ["H", "H", "i", "i"]
    - Read '-' -> append '-', '-' => ["H", "H", "i", "i", "-", "-"]
    - ...continue for the rest...
    - Join all pieces => "HHii--TThheerree"
    """
    doubled = []  # List to collect characters; list append is fast.
    for ch in s:  # Iterate over each character in the input string, left to right.
        doubled.append(ch)  # Add the current character once.
        doubled.append(ch)  # Add it a second time to "double" it.
    return "".join(doubled)  # Combine all pieces into the final string efficiently.
