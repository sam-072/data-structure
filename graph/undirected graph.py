class Graph:
    def __init__(self,nVertices):
        self.nVertices=nVertices
        self.adjMatrix=[[0 for i in range(nVertices)] for j in range(nVertices)]
        # the adjgency matrix will contains the vertices from 0 to nVertices - 1

    def addEdge(self,v1,v2):
        self.adjMatrix[v1][v2]=1
        self.adjMatrix[v2][v1]=1
    
    def removeEdge(self,v1,v2):
        if self.containEdge(v1,v2) is False:
            return
        self.adjMatrix[v1][v2]=0
        self.adjMatrix[v2][v1]=0
    
    def containEdge(self,v1,v2):
        return True if self.adjMatrix[v1][v2]>0 else False
    
    def __str__(self):
        return str(self.adjMatrix)

if __name__=='__main__':
    g=Graph(5)
    g.addEdge(1, 3)
    g.addEdge(2, 3)
    g.addEdge(1, 2)
    g.removeEdge(1, 2)
    print(g)
    print(g.containEdge(3, 2))
    print(g.containEdge(3, 3))
