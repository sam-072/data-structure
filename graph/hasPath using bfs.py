import queue
class Graph:
    def __init__(self,nVertices):
        self.nVertices=nVertices
        self.adjMatrix=[[0 for i in range(self.nVertices)] for j in range(self.nVertices)]

    def addEdge(self,v1,v2):
        self.adjMatrix[v1][v2]=1
        self.adjMatrix[v2][v1]=1

    def hasPath(self,v1,v2):
        visited=[False for i in range(self.nVertices)]
        for i in range(self.nVertices):
            if visited[i] is False:
                path=self__hasPathHelper(v1,v2,visited)
                if path:
                    return True
        return False

    def __hasPathHelper(self,v1,v2,visited):
        q=queue.Queue()
        q.put(v1)
        visited[v1]=True
        if v1==v2:
            return True
                
