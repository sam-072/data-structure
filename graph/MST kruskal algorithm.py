# Kruskal's Algorithm  or minimum spanning tree  or union find algorithm

# Given an undirected, connected and weighted graph G(V, E) with V number of vertices (which are numbered from 0 to V-1) and E number of edges.
# Find and print the Minimum Spanning Tree (MST) using Kruskal's algorithm.
# For printing MST follow the steps -
# 1. In one line, print an edge which is part of MST in the format - 
# v1 v2 w
# where, v1 and v2 are the vertices of the edge which is included in MST and whose weight is w. And v1  <= v2 i.e. print the smaller vertex first while printing an edge.
# 2. Print V-1 edges in above format in different lines.
# Note : Order of different edges doesn't matter.
# Input Format :
# Line 1: Two Integers V and E (separated by space)
# Next E lines : Three integers ei, ej and wi, denoting that there exists an edge between vertex ei and vertex ej with weight wi (separated by space)
# Output Format :
# Print the MST, as described in the task.
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
# 1 2 1
# 0 1 3
# 0 3 5

# T.C = O(E log E ) + O(E*V)


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
        edgeArray.append(Edge(v1,v2,wt))
    output=kruskal(edgeArray,v)
    for edge in output:
        if edge.v1 <edge.v2:
            print(edge.v1,edge.v2,edge.wt)
        else:
            print(edge.v2,edge.v1,edge.wt)
