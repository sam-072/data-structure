class Graph:
    def __init__(self,v):
        self.nVertices=v
        self.adjList=[[] for i in range(v)]
    
    def addEdge(self,v1,v2):
        self.adjList[v1].append(v2)
        self.adjList[v2].append(v1)
    
    def dfs(self):
        visited=self.nVertices*[False]
        c=0
        for i in self.adjList[1]:
            # print(i,len(self.adjList[i]))
            if len(self.adjList[i])%2==0:
                c+=1
        return c
            
    
    def __str__(self):
        return str(self.adjList)

if __name__=='__main__':
    v,e=map(int, input().split())
    g=Graph(v+1)
    for i in range(e):
        v1,v2=map(int, input().split())
        g.addEdge(v1, v2)
    # print(g)
    print(g.dfs())
