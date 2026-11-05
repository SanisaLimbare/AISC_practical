

from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

# Breadth First Search
def BFS(start, goal):
    visited = set()
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)

            for neighbour in graph[node]:
                new_path = path + [neighbour]
                queue.append(new_path)

    return None


# Depth First Search
def DFS(start, goal):
    visited = set()
    stack = [[start]]

    while stack:
        path = stack.pop()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)

            for neighbour in reversed(graph[node]):
                new_path = path + [neighbour]
                stack.append(new_path)

    return None


# Main program
start = 'A'
goal = 'G'

print("BFS Path:", BFS(start, goal))
print("DFS Path:", DFS(start, goal))

