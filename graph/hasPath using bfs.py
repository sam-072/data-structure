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
                path=self.__hasPathHelper(v1,v2,visited)
                if path:
                    return True
        return False

    def __hasPathHelper(self,v1,v2,visited):
        q=queue.Queue()
        q.put(v1)
        visited[v1]=True
        while q.empty() is False:
            front=q.get()
            for i in range(self.nVertices):
                if self.adjMatrix[front][i]>0 and visited[i] is False:
                    q.put(i)
                    visited[i]=True
                    if i==v2:
                        return True
        return False

if __name__=='__main__':
    v,e=map(int,input().split())
    g=Graph(v)
    for i in range(e):
        v1,v2=map(int, input().split())
        g.addEdge(v1, v2)
    v1,v2=map(int, input().split())
    print(g.hasPath(v1, v2))
                
