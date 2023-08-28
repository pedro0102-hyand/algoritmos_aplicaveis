class Grafo:
    def __init__(self, vertices):
        self.V = vertices
        self.arestas = []
    def adiciona_aresta(self, u, v, w):
        self.arestas.append((u, v, w))
    def bellman_ford(self, origem):
        distancia = {v: float('inf') for v in range(self.V)}
        distancia[origem] = 0
        for _ in range(self.V - 1):
            for u, v, w in self.arestas:
                if distancia[u] != float('inf') and distancia[u] + w < distancia[v]:
                    distancia[v] = distancia[u] + w
        for u, v, w in self.arestas:
            if distancia[u] != float('inf') and distancia[u] + w < distancia[v]:
                raise ValueError("O grafo contém um ciclo negativo alcançável a partir da origem.")
        return distancia
