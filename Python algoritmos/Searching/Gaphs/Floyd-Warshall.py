class Grafo:
    def init(self, vertices):
        self.V = vertices
        self.distancia = [[float('inf')] * self.V for _ in range(self.V)]
    def adiciona_aresta(self, u, v, w):
        self.distancia[u][v] = w
    def floyd_warshall(self):
        for i in range(self.V):
            self.distancia[i][i] = 0
        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    self.distancia[i][j] = min(self.distancia[i][j], self.distancia[i][k] + self.distancia[k][j])
        return self.distancia

