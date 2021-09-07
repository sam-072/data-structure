import queue 
import sys
class Graph:
    def __init__(self,nVertices):
        self.nVertices=nVertices
        self.adjList=[ [] for j in range(nVertices)]
        # the adjgency matrix will contains the vertices from 0 to nVertices - 1

    def addEdge(self,v1,v2):
        self.adjList[v1].append(v2)
        self.adjList[v2].append(v1)

    
    def removeEdge(self,v1,v2):
        if self.containEdge(v1,v2) is False:
            return
        self.adjList[v1][v2]=0
        self.adjList[v2][v1]=0
    
    def containEdge(self,v1,v2):
        return True if self.adjList[v1]==v2 else False
    
    def __str__(self):
        return str(self.adjList)

    def dfs(self):
        visited=[False for i in range(self.nVertices)]
        for i in range(self.nVertices):
            if visited[i] is False:
                self.__dfsHelper(i,visited)
    
    def __dfsHelper(self,sv,visited):
        print(sv)
        visited[sv]=True
        for i in self.adjList[sv]:
            if visited[i] is False:
                self.__dfsHelper(i, visited)

    def __bfsHelper(self,sv,visited):
        q=queue.Queue()
        q.put(sv)
        visited[sv]=True
        while q.empty() is False:
            u=q.get()
            print(u)
            for i in self.adjList[u]:
                if visited[i] is False:
                    q.put(i)
                    visited[i]=True
    
    def bfs(self):
        visited=[False for i in range(self.nVertices)]
        for i in range(self.nVertices):
            if visited[i] is False:
                self.__bfsHelper(i, visited)
    
    def hasPath(self,v1,v2):
        visited=[False for i in range(self.nVertices)]
        for i in range(self.nVertices):
            if visited[i] is False:
                path=(self.__hasPathHelper(v1,v2,visited))
                if path:
                    return True
        return False
    
    def __hasPathHelper(self,v1,v2,visited):
        visited[v1]=True
        if v1==v2:
            return True
       
        for i in self.adjList[v1]:
            if visited[i] is False:
                path=self.__hasPathHelper(i, v2, visited)
                if path:
                    return True

        return False

    def getPath(self,v1,v2):
        visited=[False for i in range(self.nVertices)]
        for i in range(self.nVertices):
            if visited[i] is False:
                path=self.__getPathHelper(v1,v2,visited)
                if path != None:
                    return path
        return None
    
    def __getPathHelper(self,v1,v2,visited):
        q=queue.Queue()
        q.put(v1)
        d=dict()
        z=0
        visited[v1]=True
        while q.empty() is False:
            front=q.get()
            for i in self.adjList[front]:
                if visited[i] is False:
                    d[i]=d.get(i,front)
                    q.put(i)
                    visited[i]=True
                    if i==v2:
                        z=-1
                        break
            if z==-1:
                break
        if z==-1:
            l=[v2]
            while d.get(l[-1],-1)!=-1:
                l.append(d[l[-1]])
            return l
        else:
            return None
    
    def isConnected(self):
        visited=[False for i in range(self.nVertices)]
        q=queue.Queue()
        q.put(0)
        visited[0]=True
        while q.empty() is False:
            u=q.get()
            for i in self.adjList[u]:
                if visited[i] is False:
                    q.put(i)
                    visited[i]=True
        
        if False in visited:
            return False
        return True
    
    def ConnectedComponents(self):
        visited=[False for i in range(self.nVertices)]
        ans=[]
        for i in range(self.nVertices):
            if visited[i] is False:
                path=self.__ConnectedComponentsHelper(i,visited,[])
                if len(path) !=0:
                    ans.append(path)
        return ans
    
    def __ConnectedComponentsHelper(self,sv,visited,l):
        q=queue.Queue()
        q.put(sv)
        visited[sv]=True
        while q.empty() is False:
            u=q.get()
            l.append(u)
            for i in self.adjList[u]:
                if visited[i] is False:
                    q.put(i)
                    visited[i]=True
        return l
    

if __name__=='__main__':
    g=Graph(7)
    g.addEdge(0,1)
    g.addEdge(0,3)
    g.addEdge(2,4)
    g.addEdge(2,5)
    g.addEdge(5,6)
    print(g)
    g.dfs()
    print()
    g.bfs()
    print(g.containEdge(3, 2))
    print(g.containEdge(0, 6))
    print(g.hasPath(3, 1))
    print(g.getPath(2, 6))
    print(g.isConnected())
    print(g.ConnectedComponents())
