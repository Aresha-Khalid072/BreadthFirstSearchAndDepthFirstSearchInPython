from collections import deque

def bfs(graph, start, goal):
    parent = {start: None}
    q = deque([start])
    while q:
        node = q.popleft()
        if node == goal:
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            return path[::-1]
        for child in graph.get(node, []):
            if child not in parent:
                parent[child] = node
                q.append(child)
    return None

def dfs(graph, start, goal):
    parent = {start: None}
    stack = [start]
    while stack:
        node = stack.pop()
        if node == goal:
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            return path[::-1]
        for child in reversed(graph.get(node, [])):
            if child not in parent:
                parent[child] = node
                stack.append(child)
    return None


graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}


# BFS
print("BFS:", bfs(graph, 'A', 'E'))

# DFS
print("DFS:", dfs(graph, 'A', 'E'))