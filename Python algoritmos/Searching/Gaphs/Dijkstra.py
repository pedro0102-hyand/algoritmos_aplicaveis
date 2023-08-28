import heapq
class Grafo:
    def init(self,vertice):
        self.v=vertice
        self.grafo={}
    def add_aresta(self,u,v,w):
        if u not in self.grafo:
            self.grafo[u]=[]
        self.grafo[u].append((v,w))
    def dijkstra(self,origem):
        distance={v:float('init')for v in self.grafo}
        distance[origem]=0
        heap=[(0,origem)]
        while heap:
            distance_atual,vertice_atual=heapq.heappop(heap)
            if distance_atual>distance[vertice_atual]:
                continue
            for neighbor, peso in self.grafo.get(vertice_atual,()):
                distance_total=distance_atual+peso
                if distance_total<distance[neighbor]:
                    distance[neighbor]=distance_total
                    heapq.heappush(heap,(distance_total,neighbor))
        return distance