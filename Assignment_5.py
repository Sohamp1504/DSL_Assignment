# Assignment 5

class HashTable:

    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        # Check if the table is already full
        if None not in self.table:
            print("Hash table is full! Cannot insert:", key)
            return

        index = self.hash_function(key)

        # Linear probing to find the next empty slot
        while self.table[index] is not None:
            index = (index + 1) % self.size

        self.table[index] = key
        print(f"Inserted {key} at index {index}")

    def search(self, key):
        index = self.hash_function(key)

        for i in range(self.size):
            pos = (index + i) % self.size

            if self.table[pos] == key:
                print(f"Key {key} found at index: {pos}")
                return pos

            # If an empty slot is encountered
            if self.table[pos] is None:
                break

        print(f"Key {key} not found")
        return None

    def delete(self, key):
        index = self.hash_function(key)

        for i in range(self.size):
            pos = (index + i) % self.size

            if self.table[pos] == key:
                self.table[pos] = None
                print(f"Key {key} deleted from index {pos}")
                return True

            if self.table[pos] is None:
                break

        print(f"Key {key} not found to delete")
        return False

    def display(self):
        print("\n--- Hash Table ---")

        for i in range(self.size):
            print(f"{i} : {self.table[i]}")

        print("------------------\n")


# --- Demonstration ---
if __name__ == "__main__":

    ht = HashTable(5)

    # Insert elements
    ht.insert(10)
    ht.insert(15)
    ht.insert(20)
    ht.insert(25)

    ht.display()

    # Search for keys
    ht.search(15)
    ht.search(99)

    # Delete an element
    ht.delete(15)

    ht.display()