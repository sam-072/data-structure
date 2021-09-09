# problem name : Breadth First Search: Shortest Reach
# problem link : https://www.hackerrank.com/challenges/bfsshortreach/problem
# level : Medium

import sys
class Graph:
    def __init__(self,nVertices):
        self.nVertices=nVertices
        self.adjMatrix=[[0 for i in range(nVertices)] for j in range(nVertices)]
        # the adjgency matrix will contains the vertices from 0 to nVertices - 1

    def addEdge(self,v1,v2):
        self.adjMatrix[v1][v2]=6
        self.adjMatrix[v2][v1]=6
    
    def __minDist(self,distance,visited):
        mindis=sys.maxsize
        minindex=-1
        for i in range(self.nVertices):
            if visited[i] is False and (minindex==-1 or distance[minindex]> distance[i]):
                minindex=i
        return minindex
    
    def sortestPath(self,v):
        visited=self.nVertices*[False]
        distance=self.nVertices*[sys.maxsize]
        distance[v]=0
        for i in range(self.nVertices-1):
            u=self.__minDist(distance,visited)
            visited[u]=True
            for j in range(self.nVertices):
                if self.adjMatrix[u][j]>0 and visited[j] is False:
                    currD=distance[u]+ self.adjMatrix[u][j]
                    if distance[j]> currD:
                        distance[j]=currD
    
        for i in range(1,self.nVertices):
            if distance[i]!=0:
                if distance[i]==sys.maxsize:
                    print(-1,end=" ")
                else:
                    print(distance[i],end=" ")
        print()


if __name__=='__main__':
    for _ in range(int(input())):
        v,e=map(int, input().split())
        g=Graph(v+1)
        for i in range(e):
            v1,v2=map(int, input().split())
            g.addEdge(v1, v2)        
        v1=int(input())
        g.sortestPath(v1)