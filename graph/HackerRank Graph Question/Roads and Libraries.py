import queue
class Graph:
    def __init__(self,nVertices):
        self.nVertices=nVertices
        self.adjList=[[] for i in range(nVertices)]

    def addEdge(self,v1,v2):
        self.adjList[v2].append(v1)
        self.adjList[v1].append(v2)
    
    def ConnectedComponents(self):
        visited=[False for i in range(self.nVertices)]
        c_lib=c_road=0
        for i in range(self.nVertices):
            if visited[i] is False:
                path=self.__ConnectedComponentsHelper(i,visited,[])
                if path != None:
                    c_lib+=1
                    c_road+=len(path)-1
        return c_road,c_lib-1
    
    def __ConnectedComponentsHelper(self,sv,visited,l):
        q=queue.Queue()
        visited[sv]=True
        q.put(sv)
        while q.empty() is False:
            u=q.get()
            l.append(u)
            for i in self.adjList[u]:
                if visited[i] is False:
                    q.put(i)
                    visited[i]=True
        return l

if __name__=='__main__':
    for _ in range(int(input())):
        n,m,c_lib,c_road=map(int, input().split())
        g=Graph(n+1)
        for i in range(m):
            v1,v2=map(int, input().split())
            g.addEdge(v1, v2)
        c1,c2=g.ConnectedComponents()
        print(min(n*c_lib,c1*c_road+c2*c_lib))

