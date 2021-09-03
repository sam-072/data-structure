# Given an undirected graph G(V,E), check if the graph G is connected graph or not.
# Note:
# 1. V is the number of vertices present in graph G and vertices are numbered from 0 to V-1. 
# 2. E is the number of edges present in graph G.
# Input Format :
# The first line of input contains two integers, that denote the value of V and E.
# Each of the following E lines contains two integers, that denote that there exists an edge between vertex a and b.
# Output Format :
# The first and only line of output contains "true" if the given graph is connected or "false", otherwise.
# Constraints :
# 0 <= V <= 1000
# 0 <= E <= (V * (V - 1)) / 2
# 0 <= a <= V - 1
# 0 <= b <= V - 1
# Time Limit: 1 second
# Sample Input 1:
# 4 4
# 0 1
# 0 3
# 1 2
# 2 3
# Sample Output 1:
# true
# Sample Input 2:
# 4 3
# 0 1
# 1 3 
# 0 3
# Sample Output 2:
# false 

import queue
class Graph:
    def __init__(self,nVertices):
        self.nVertices=nVertices
        self.adjMatrix=[[0 for i in range(self.nVertices)] for j in range(self.nVertices)]

    def addEdge(self,v1,v2):
        self.adjMatrix[v1][v2]=1
        self.adjMatrix[v2][v1]=1
    
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


if __name__=='__main__':
    v,e=map(int,input().split())
    g=Graph(v)
    for i in range(e):
        v1,v2=map(int, input().split())
        g.addEdge(v1, v2)
    print(g.isConnected())
