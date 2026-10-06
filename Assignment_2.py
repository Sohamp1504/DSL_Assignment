# Assignment_2
# Employee Salary Sorting and Top 5 Salaries Display

# Sample list of employee salaries
salaries = [45000.75, 52000.0, 39000.3, 61000.8, 47000.25,
            88000.0, 73000.45, 59000.1]


# ---------------- Selection Sort ----------------
def selection_sort(arr):
    n = len(arr)
    sorted_arr = arr.copy()  # Avoid modifying original list

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if sorted_arr[j] < sorted_arr[min_index]:
                min_index = j

        # Swap
        sorted_arr[i], sorted_arr[min_index] = (
            sorted_arr[min_index],
            sorted_arr[i]
        )

    return sorted_arr


# ---------------- Bubble Sort ----------------
def bubble_sort(arr):
    n = len(arr)
    sorted_arr = arr.copy()

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if sorted_arr[j] > sorted_arr[j + 1]:

                # Swap
                sorted_arr[j], sorted_arr[j + 1] = (
                    sorted_arr[j + 1],
                    sorted_arr[j]
                )

    return sorted_arr


# ---------------- Display Top 5 Salaries ----------------
def display_top_5(salary_list):
    # Sort in descending order
    top_5 = salary_list[-5:][::-1]

    print("\nTop 5 Highest Salaries:")

    for i, salary in enumerate(top_5, 1):
        print(f"{i}. ₹{salary:.2f}")


# ---------------- Main Program ----------------

print("Original Salaries:")
for salary in salaries:
    print(f"₹{salary:.2f}")

# Selection Sort
selection_sorted = selection_sort(salaries)

print("\nSalaries using Selection Sort:")
for salary in selection_sorted:
    print(f"₹{salary:.2f}")

# Bubble Sort
bubble_sorted = bubble_sort(salaries)

print("\nSalaries using Bubble Sort:")
for salary in bubble_sorted:
    print(f"₹{salary:.2f}")

# Display Top 5
display_top_5(selection_sorted)