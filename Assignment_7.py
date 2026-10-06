# Assignment 7

from collections import deque


# Graph representation
locations = ['A', 'B', 'C', 'D']

location_index = {
    name: idx for idx, name in enumerate(locations)
}


# Adjacency Matrix
adj_matrix = [
    [0, 1, 1, 0],
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [0, 1, 1, 0]
]


# Adjacency List
adj_list = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}


# -------- DFS using Adjacency Matrix --------
def dfs_matrix(start):
    visited = [False] * len(locations)
    result = []

    def dfs(node):
        visited[node] = True
        result.append(locations[node])

        for neighbor in range(len(adj_matrix)):
            if adj_matrix[node][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor)

    dfs(location_index[start])

    return result


# -------- BFS using Adjacency List --------
def bfs_list(start):
    visited = set()
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.add(node)
            result.append(node)

            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return result


# -------- Menu --------
def menu():
    print("\n==== MENU ====")
    print("1. DFS")
    print("2. BFS")
    print("3. Exit")


# -------- Main Program --------
while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        start_location = 'A'
        dfs_result = dfs_matrix(start_location)

        print(
            "DFS traversal (using adjacency matrix):",
            dfs_result
        )

    elif choice == '2':
        start_location = 'A'
        bfs_result = bfs_list(start_location)

        print(
            "BFS traversal (using adjacency list):",
            bfs_result
        )

    elif choice == '3':
        print("Exiting...")
        break

    else:
        print("Invalid choice! Please select 1, 2, or 3.")