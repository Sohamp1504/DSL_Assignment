# Binary Search Tree - Insertion, Deletion, Search and Display

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Insert a node
def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)

    return root


# Search for a node
def search(root, key):
    if root is None:
        return False

    if root.data == key:
        return True
    elif key < root.data:
        return search(root.left, key)
    else:
        return search(root.right, key)


# Find minimum value node
def find_min(root):
    current = root
    while current.left is not None:
        current = current.left
    return current


# Delete a node
def delete(root, key):
    if root is None:
        return root

    if key < root.data:
        root.left = delete(root.left, key)

    elif key > root.data:
        root.right = delete(root.right, key)

    else:
        # Case 1: No child
        if root.left is None and root.right is None:
            return None

        # Case 2: One child
        elif root.left is None:
            return root.right

        elif root.right is None:
            return root.left

        # Case 3: Two children
        else:
            temp = find_min(root.right)
            root.data = temp.data
            root.right = delete(root.right, temp.data)

    return root


# Display BST using inorder traversal
def display(root):
    if root is not None:
        display(root.left)
        print(root.data, end=" ")
        display(root.right)


# Main program
root = None

values = [50, 30, 70, 20, 40, 60, 80]

for value in values:
    root = insert(root, value)

print("BST (Inorder):")
display(root)

# Search
key = 40
if search(root, key):
    print(f"\n{key} is found in the BST.")
else:
    print(f"\n{key} is not found in the BST.")

# Delete
key = 30
root = delete(root, key)

print(f"\nBST after deleting {key}:")
display(root)