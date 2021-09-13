import heapq
def kSmallest(a,k,n):
    heap=a[:k]
    heapq._heapify_max(heap)
    for i in range(k,n):
        if a[i] < heap[0]:
            heapq._heapreplace_max(heap, a[i])
    return heap

n,k=map(int, input().split())
a=list(map(int, input().split()))
print(*kSmallest(a, k, n))

