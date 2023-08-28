
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
def dfs(grafo, node, visited):
    if node not in visited:
        visited.append(node)
        for neighbor in grafo[node]:
            dfs(grafo, neighbor, visited)
start_node = 'A'
visited_nodes = []
dfs(grafo, start_node, visited_nodes)
print(visited_nodes)
