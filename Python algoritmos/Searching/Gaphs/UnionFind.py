class unionFind:
    def init (self,n):
        self.parent=list(range(n))
        self.rank=[0]*n
        def find(self, n1):
            if self.parent[n1]!=n1:
                self.parent[n1]=self.find(self.parent[n1])
            return self.parent[n1]
        def union(self,n1,n2):
            root_n1=self.find(n1)
            root_n2=self.find(n2)
            if root_n1==root_n2:
                return
            if self.rank[root_n1]<self.ranl[root_n2]:
                self.parent[root_n1]=root_n2
            elif self.rank[root_n1]>self.rank[root_n2]:
                self.parent[root_n2]=root_n1
            else:
                self.parent[root_n2]=root_n1
                self.rank[root_n1]+=1