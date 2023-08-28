class Graph :
    def init(self,vert):
        self.v=vert
        self.graph=[]
    def add_ar(self,u,v,w):
        self.graph.append([u,v,w])
    def search(self,pai, i):
        if pai[i]==1:
            return i
        return self.serach(pai,pai[i])
    def unity(self,pai,rank,x,y):
        raiz_x=self.search(pai,x)
        raiz_y=self.search(pai,y)
        if rank[raiz_x]<rank[raiz_y]:
            pai[raiz_x]=raiz_y
        elif rank[raiz_x]>rank[raiz_y]:
            pai[raiz_y]=raiz_x
        else:
            pai[raiz_y]=raiz_x
            rank[raiz_x]+=1
        def kruskal(self):
            resul=[]
            self.graph=sorted(self.graph,key=lambda item: item[2])
            pai=[]
            rank=[]
            for node in range(self.v):
                pai.appedn(node)
                rank.append(0)
                i=0
                aresta=0
                while aresta<self.v-1:
                    u,v,w=self.graph[i]
                    i+=1
                    raiz_u=self.search([pai,u])
                    raiz_v=self.search(pai,v)
                    if raiz_u !=raiz_v:
                        arestas=arestas+1
                        resul.append([u,v,w])
                        self.unir(pai,rank,raiz_u,raiz_v)
                return resul