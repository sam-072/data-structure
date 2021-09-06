# Dijkstra's Algorithm

# Given an undirected, connected and weighted graph G(V, E) with V number of vertices (which are numbered from 0 to V-1) and E number of edges.
# Find and print the shortest distance from the source vertex (i.e. Vertex 0) to all other vertices (including source vertex also) using Dijkstra's Algorithm.
# Input Format :
# Line 1: Two Integers V and E (separated by space)
# Next E lines : Three integers ei, ej and wi, denoting that there exists an edge between vertex ei and vertex ej with weight wi (separated by space)
# Output Format :
# For each vertex, print its vertex number and its distance from source, in a separate line. The vertex number and its distance needs to be separated by a single space.
# Note : Order of vertices in output doesn't matter.
# Constraints :
# 2 <= V, E <= 10^5
# Time Limit: 1 sec
# Sample Input 1 :
# 4 4
# 0 1 3
# 0 3 5
# 1 2 1
# 2 3 8
# Sample Output 1 :
# 0 0
# 1 3
# 2 4
# 3 5


import sys
class Graph:
    def __init__(self,nVertices):
        self.nVertices=nVertices
        self.adjMatrix=[[0 for i in range(nVertices)] for j in range(nVertices)]
        # the adjgency matrix will contains the vertices from 0 to nVertices - 1

    def addEdge(self,v1,v2,wt=1):
        self.adjMatrix[v1][v2]=wt
        self.adjMatrix[v2][v1]=wt
    
    def __minDist(self,distance,visited):
        mindis=sys.maxsize
        minindex=-1
        for i in range(self.nVertices):
            if visited[i] is False and (minindex==-1 or distance[minindex]> distance[i]):
                minindex=i
        return minindex
    
    def sortestPath(self):
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



if __name__=='__main__':
    v,e=map(int, input().split())
    g=Graph(v)
    for i in range(e):
        v1,v2,wt=map(int, input().split())
        g.addEdge(v1, v2,wt)        
        
    g.sortestPath()