import sys
class Graph:
    def __init__(self,nVertices):
        self.nVertices=nVertices
        self.adjMatrix=[[0 for i in range(nVertices)] for j in range(nVertices)]
        # the adjgency matrix will contains the vertices from 0 to nVertices - 1

    def addEdge(self,v1,v2,wt=1):
        self.adjMatrix[v1][v2]=wt
    
    def __getMinVertex(self,visited,weight):
        min_v=-1
        for i in range(self.nVertices):
            if visited[i] is False and (min_v==-1 or weight[min_v]> weight[i]):
                min_v=i
        return min_v
    
    def prims(self):
        visited=self.nVertices*[False]
        parent=self.nVertices*[-1]
        weight=self.nVertices*[sys.maxsize]
        weight[0]=0

        for i in range(self.nVertices-1):
            min_v=self.__getMinVertex(visited, weight)
            visited[min_v]=True
            for j in range(self.nVertices):
                if self.adjMatrix[min_v][j]>0 and visited[j] is False:
                    if weight[j] > self.adjMatrix[min_v][j]:
                        weight[j]=self.adjMatrix[min_v][j]
                        parent[j]=min_v
        
        for i in range(1,self.nVertices):
            if i<parent[i]:
                print(i,parent[i],weight[i])
            else:
                print(parent[i],i,weight[i])

if __name__=='__main__':
    v,e=map(int, input().split())
    g=Graph(v)
    for i in range(e):
        v1,v2,wt=map(int, input().split())
        g.addEdge(v1, v2,wt)        
        
    g.prims()