# Given an undirected graph G(V, E) and two vertices v1 and v2(as integers), find and print the path from v1 to v2 (if exists). Print nothing if there is no path between v1 and v2.
# Find the path using DFS and print the first path that you encountered.
# Note:
# 1. V is the number of vertices present in graph G and vertices are numbered from 0 to V-1. 
# 2. E is the number of edges present in graph G.
# 3. Print the path in reverse order. That is, print v2 first, then intermediate vertices and v1 at last.
# 4. Save the input graph in Adjacency Matrix.
# Input Format :
# The first line of input contains two integers, that denote the value of V and E.
# Each of the following E lines contains two integers, that denote that there exists an edge between vertex 'a' and 'b'.
# The following line contain two integers, that denote the value of v1 and v2.
# Output Format :
# Print the path from v1 to v2 in reverse order.
# Constraints :
# 2 <= V <= 1000
# 1 <= E <= (V * (V - 1)) / 2
# 0 <= a <= V - 1
# 0 <= b <= V - 1
# 0 <= v1 <= 2^31 - 1
# 0 <= v2 <= 2^31 - 1
# Time Limit: 1 second
# Sample Input 1 :
# 4 4
# 0 1
# 0 3
# 1 2
# 2 3
# 1 3
# Sample Output 1 :
# 3 0 1
# Sample Input 2 :
# 6 3
# 5 3
# 0 1
# 3 4
# 0 3

class Graph:
    def __init__(self,nVertices):
        self.nVertices=nVertices
        self.adjMatrix=[[0 for i in range(self.nVertices)] for j in range(self.nVertices)]

    def addEdge(self,v1,v2):
        self.adjMatrix[v1][v2]=1
        self.adjMatrix[v2][v1]=1
    
    def getPath(self,v1,v2):
        visited=[False for i in range(self.nVertices)]
        for i in range(self.nVertices):
            if visited[i] is False:
                path=self.__getPathHelper(v1,v2,visited)
                if path != None:
                    return path
        return None
    
    def __getPathHelper(self,v1,v2,visited):
        visited[v1]=True
        if self.adjMatrix[v1][v2]==1:
            return [v2,v1]
        for i in range(self.nVertices):
            if visited[i] is False and self.adjMatrix[v1][i]>0:
                path=self.__getPathHelper(i, v2, visited)
                if path != None:
                    path.append(v1)
                    return path
        return None


if __name__=='__main__':
    v,e=map(int, input().split())
    g=Graph(v)
    for i in range(e):
        a,b=map(int, input().split())
        g.addEdge(a, b)
    v1,v2=map(int, input().split())
    print(g.getPath(v1, v2))






















