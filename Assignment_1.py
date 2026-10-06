# Assignment_1
# E-commerce Customer Account ID Search Program

# Sample list of customer account IDs
customer_ids = [1034, 2051, 1022, 1505, 3002, 2501, 1890, 1200]


# -------- Linear Search --------
def linear_search(ids, target):
    for i in range(len(ids)):
        if ids[i] == target:
            return i
    return -1


# -------- Binary Search --------
def binary_search(ids, target):
    left = 0
    right = len(ids) - 1

    while left <= right:
        mid = (left + right) // 2

        if ids[mid] == target:
            return mid
        elif ids[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# -------- Main Program --------
print("Customer Account ID Search System")
print("List of Customer IDs:", customer_ids)

# Get ID to search from user
try:
    search_id = int(input("Enter Customer ID to search: "))
except ValueError:
    print("Invalid input! Please enter a numeric ID.")
    exit()


# -------- Linear Search --------
index_linear = linear_search(customer_ids, search_id)

if index_linear != -1:
    print(
        f"Linear Search: Customer ID {search_id} "
        f"found at index {index_linear}."
    )
else:
    print(f"Linear Search: Customer ID {search_id} not found.")


# -------- Binary Search --------
# Binary Search requires a sorted list
sorted_ids = sorted(customer_ids)

print("Sorted Customer IDs for Binary Search:", sorted_ids)

index_binary = binary_search(sorted_ids, search_id)

if index_binary != -1:
    print(
        f"Binary Search: Customer ID {search_id} "
        f"found at index {index_binary} in sorted list."
    )
else:
    print(f"Binary Search: Customer ID {search_id} not found.")