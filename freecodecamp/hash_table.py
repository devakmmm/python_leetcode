"""Simple hash table implementation using nested dictionaries."""  # Module description.


class HashTable:  # Defines a class for a basic hash table.
    """Hash table that stores key-value pairs by hashed bucket."""  # Class description.

    def __init__(self):  # Constructor runs when a new instance is created.
        # Map hash -> {original_key: value}
        self.collection = {}  # Initialize the storage as an empty dict.

    def hash(self, key):  # Compute a hash for a string key.
        """Compute hash as sum of Unicode code points for the string key."""
        return sum(ord(ch) for ch in key)  # Add ord() values of each character.

    def add(self, key, value):  # Insert or update a key-value pair.
        """Add or update a key-value pair in the hash table."""
        hashed_key = self.hash(key)  # Convert the key to its hash bucket.
        # Create the bucket if it does not exist.
        if hashed_key not in self.collection:  # Check if bucket is missing.
            self.collection[hashed_key] = {}  # Create a new bucket dict.
        # Store or overwrite the value for the original key.
        self.collection[hashed_key][key] = value  # Save the value in the bucket.

    def remove(self, key):  # Delete a key-value pair.
        """Remove a key-value pair if it exists; otherwise do nothing."""
        hashed_key = self.hash(key)  # Compute the bucket hash.
        bucket = self.collection.get(hashed_key)  # Get the bucket or None.
        if not bucket:  # If the bucket doesn't exist, nothing to remove.
            return  # Exit without error.
        # Remove the key if present in the bucket.
        if key in bucket:  # Check for the exact key in the bucket.
            del bucket[key]  # Delete the key-value pair.
            # Clean up empty buckets to keep the table tidy.
            if not bucket:  # If the bucket is now empty...
                del self.collection[hashed_key]  # Remove the bucket itself.

    def lookup(self, key):  # Retrieve a value by key.
        """Return the value for key, or None if not found."""
        hashed_key = self.hash(key)  # Compute the bucket hash.
        bucket = self.collection.get(hashed_key)  # Get the bucket or None.
        if not bucket:  # If no bucket, the key is not present.
            return None  # Return None when missing.
        return bucket.get(key)  # Return the value, or None if key not in bucket.


# Example usage:
# table = HashTable()
# table.add("ab", 1)   # hash 195
# table.add("ba", 2)   # hash 195 (collision, same bucket)
# print(table.lookup("ab"))  # 1
# table.remove("ab")
# print(table.lookup("ab"))  # None
