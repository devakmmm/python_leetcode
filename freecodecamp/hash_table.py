"""Simple hash table implementation using nested dictionaries."""


class HashTable:
    """Hash table that stores key-value pairs by hashed bucket."""

    def __init__(self):
        # Map hash -> {original_key: value}
        self.collection = {}

    def hash(self, key):
        """Compute hash as sum of Unicode code points for the string key."""
        return sum(ord(ch) for ch in key)

    def add(self, key, value):
        """Add or update a key-value pair in the hash table."""
        hashed_key = self.hash(key)
        # Create the bucket if it does not exist.
        if hashed_key not in self.collection:
            self.collection[hashed_key] = {}
        # Store or overwrite the value for the original key.
        self.collection[hashed_key][key] = value

    def remove(self, key):
        """Remove a key-value pair if it exists; otherwise do nothing."""
        hashed_key = self.hash(key)
        bucket = self.collection.get(hashed_key)
        if not bucket:
            return
        # Remove the key if present in the bucket.
        if key in bucket:
            del bucket[key]
            # Clean up empty buckets to keep the table tidy.
            if not bucket:
                del self.collection[hashed_key]

    def lookup(self, key):
        """Return the value for key, or None if not found."""
        hashed_key = self.hash(key)
        bucket = self.collection.get(hashed_key)
        if not bucket:
            return None
        return bucket.get(key)
