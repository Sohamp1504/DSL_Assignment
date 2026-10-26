class LinearProbingHashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size
        self.DELETED = "<DELETED>"

    def _hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self._hash_function(key)
        original_index = index
        while self.table[index] not in (None, self.DELETED):
            if self.table[index] == key:
                print(f"Key {key} already exists at index {index}.")
                return
            index = (index + 1) % self.size
            if index == original_index:
                print("Hash table is full. Cannot insert.")
                return
        self.table[index] = key
        print(f"Inserted key {key} at index {index}.")

    def search(self, key):
        index = self._hash_function(key)
        original_index = index
        while self.table[index] is not None:
            if self.table[index] == key:
                print(f"Key {key} found at index {index}.")
                return index
            index = (index + 1) % self.size
            if index == original_index:
                break
        print(f"Key {key} not found.")
        return None

    def delete(self, key):
        index = self.search(key)
        if index is not None:
            self.table[index] = self.DELETED
            print(f"Key {key} deleted from index {index}.")

    def display(self):
        print("Hash Table:")
        for i, key in enumerate(self.table):
            print(f"Index {i}: {key}")

def menu():
    ht = LinearProbingHashTable()
    while True:
        print("____MENU____")
        print("1.Insert key")
        print("2.Search key")
        print("3.Delete key")
        print("4.Display Table")
        print("5.Exit")

        choice=input("enter choice :")
        if choice == '1':
            key=int(input("Enter key :"))
            ht.insert(key)
        elif choice == '2':
            key=int(input("Enter key :"))
            ht.search(key)
        elif choice == '3':
            key=int(input("Enter key :"))
            ht.delete(key)
        elif choice == '4':
            ht.display()
        
        elif choice == '5':
            print("👋 Exiting hash code")
            break
        else:
            print("❌ Invalid choice. Try again.")
menu()
