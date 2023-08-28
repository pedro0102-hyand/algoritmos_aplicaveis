from collections import deque
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
def bfs(grafo, start_node):
    visited = []
    queue = deque([start_node])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(grafo[node])
    return visited
start_node = 'A'
visited_nodes = bfs(grafo, start_node)
print( visited_nodes)
