class Edge:
    def __init__(self,v1,v2,wt):
        self.v1=v1
        self.v2=v2
        self.wt=wt

def getParent(v,parent):
    if parent[v]==v:
        return v
    return getParent(parent[v], parent)

def kruskal(edgeArray,v):
    edgeArray=sorted(edgeArray,key=lambda edge:edge.wt)
    parent=[i for i in range(v)]
    count=0
    i=0
    output=[]

    while count<v-1:
        curredge=edgeArray[i]
        p1=getParent(curredge.v1, parent)
        p2=getParent(curredge.v2, parent)
        if p1 != p2:
            output.append(curredge)
            count+=1
            parent[p1]=p2
        i+=1
    return output

if __name__=='__main__':
    v,e=map(int, input().split())
    edgeArray=[]
    for i in range(e):
        v1,v2,wt=map(int, input().split())
        edgeArray.append(Edge(v1-1,v2-1,wt))
    output=kruskal(edgeArray,v)
    c=0
    for edge in output:
        c+=edge.wt
    print(c)
