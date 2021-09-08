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
        l=[]
        for i in range(self.nVertices):
            if visited[i] is False:
                path=self.__ConnectedComponentsHelper(i,visited,[])
                if path != None:
                    l.append(len(path))
        return l
    
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
    n,p=map(int,input().split())
    g=Graph(n)
    for i in range(p):
        v1,v2=map(int, input().split())
        g.addEdge(v1,v2)
    l=g.ConnectedComponents()
    n1=len(l)
    l1=n1*[0]
    p=l[-1]
    for i in range(n1-1,0,-1):
        l1[i]=p
        p+=l[i-1]
    c=0
    for i in range(n1-1):
        c+=l[i]*l1[i+1]
    print(c)
    