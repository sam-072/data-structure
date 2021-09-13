import heapq
n,k=map(int, input().split())
a=list(map(int, input().split()))
heap=a[:k]
heapq.heapify(heap)
for i in range(k,n):
    if a[i]> heap[0]:
        heapq.heapreplace(heap, a[i])
    
print(*heap)

