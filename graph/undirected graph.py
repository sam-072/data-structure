import queue
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

    def dfs(self):
        visited=[False for i in range(self.nVertices)]
        self.__dfsHelper(0,visited)
    
    def __dfsHelper(self,sv,visited):
        print(sv)
        visited[sv]=True
        for i in range(self.nVertices):
            if self.adjMatrix[sv][i]>0 and visited[i] is False:
                self.__dfsHelper(i, visited)

    def bfs(self):
        q=queue.Queue()
        q.put(0)
        visited=[False for i in range(self.nVertices)]
        visited[0]=True
        while q.empty() is False:
            u=q.get()
            print(u)
            for i in range(self.nVertices):
                if self.adjMatrix[u][i]>0 and visited[i] is False:
                    q.put(i)
                    visited[i]=True



if __name__=='__main__':
    g=Graph(5)
    g.addEdge(0,1)
    g.addEdge(1,3)
    g.addEdge(0,2)
    g.addEdge(2,3)
    g.addEdge(2,4)
    print(g)
    g.dfs()
    print()
    g.bfs()
    print(g.containEdge(3, 2))
    print(g.containEdge(3, 3))
