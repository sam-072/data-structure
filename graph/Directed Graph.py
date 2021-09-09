import queue 
import sys
class Graph:
    def __init__(self,nVertices):
        self.nVertices=nVertices
        self.adjMatrix=[[0 for i in range(nVertices)] for j in range(nVertices)]
        # the adjgency matrix will contains the vertices from 0 to nVertices - 1

    def addEdge(self,v1,v2,wt):
        self.adjMatrix[v1][v2]=wt
    
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
        for i in range(self.nVertices):
            if visited[i] is False:
                self.__dfsHelper(i,visited)
    
    def __dfsHelper(self,sv,visited):
        print(sv)
        visited[sv]=True
        for i in range(self.nVertices):
            if self.adjMatrix[sv][i]>0 and visited[i] is False:
                self.__dfsHelper(i, visited)

    def __bfsHelper(self,sv,visited):
        q=queue.Queue()
        q.put(sv)
        visited[sv]=True
        while q.empty() is False:
            u=q.get()
            print(u)
            for i in range(self.nVertices):
                if self.adjMatrix[u][i]>0 and visited[i] is False:
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
       
        for i in range(self.nVertices):
            if visited[i] is False and self.adjMatrix[v1][i]>0:
                path=self.__hasPathHelper(i, v2, visited)
                if path:
                    return True

        return False

    def __minDist(self,distance,visited):
        mindis=sys.maxsize
        minindex=-1
        for i in range(self.nVertices):
            if visited[i] is False and (minindex==-1 or distance[minindex]> distance[i]):
                minindex=i
        return minindex
    
    def getPath(self):
        visited=self.nVertices*[False]
        distance=self.nVertices*[sys.maxsize]
        distance[0]=0
        for i in range(self.nVertices-1):
            u=self.__minDist(distance,visited)
            visited[u]=True
            for j in range(self.nVertices):
                if self.adjMatrix[u][j]>0 and visited[j] is False:
                    currD=distance[u]+ self.adjMatrix[u][j]
                    if distance[j]> currD:
                        distance[j]=currD

        for i in range(self.nVertices):
            print(i,distance[i])
    
    def isConnected(self):
        visited=[False for i in range(self.nVertices)]
        q=queue.Queue()
        q.put(0)
        visited[0]=True
        while q.empty() is False:
            u=q.get()
            for i in range(self.nVertices):
                if self.adjMatrix[u][i]>0 and visited[i] is False:
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
            for i in range(self.nVertices):
                if self.adjMatrix[u][i]>0 and visited[i] is False:
                    q.put(i)
                    visited[i]=True
        return l
    

if __name__=='__main__':
    v,e=map(int, input().split())
    g=Graph(v)
    for i in range(e):
        v1,v2,wt=map(int, input().split())
        g.addEdge(v1, v2, wt)
    g.getPath()
    