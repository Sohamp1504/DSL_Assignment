# Assignment 6

class HashTable:

    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self._hash_function(key)

        # Update value if key already exists
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                print(f"Updated key {key} with value '{value}'")
                return

        # Insert new key-value pair
        self.table[index].append([key, value])
        print(f"Inserted key {key} with value '{value}'")

    def search(self, key):
        index = self._hash_function(key)

        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]

        return None

    def delete(self, key):
        index = self._hash_function(key)

        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                print(f"Deleted key {key}")
                return

        print(f"Key {key} not found for deletion.")

    def display(self):
        print("\n--- Hash Table ---")

        for i, bucket in enumerate(self.table):
            print(f"Index {i}: {bucket}")

        print("------------------\n")


# --- Demonstration ---
if __name__ == "__main__":

    ht = HashTable()

    # Inserting elements
    ht.insert(15, "apple")
    ht.insert(15, "orange")
    ht.insert(50, "pineapple")
    ht.insert(25, "banana")
    ht.insert(35, "cherry")

    # Display initial state
    ht.display()

    # Searching elements
    print("Search 35:", ht.search(35))
    print("Search 25:", ht.search(25))

    # Deleting an element
    ht.delete(25)

    # Search after deletion
    print("Search 25 after deletion:", ht.search(25))

    # Final table state
    ht.display()