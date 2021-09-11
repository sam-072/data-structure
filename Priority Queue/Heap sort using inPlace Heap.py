def HeapifyDown(arr,i,n):
    P_index=i
    left_index=2*P_index+1
    right_index=2*P_index+2
    while left_index < n:
        min_index=P_index
        if arr[min_index] > arr[left_index]:
            min_index=left_index
        if right_index < n and arr[min_index] > arr[right_index]:
            min_index=right_index
        if min_index==P_index:
            break
        arr[min_index],arr[P_index] = arr[P_index], arr[min_index]
        P_index=min_index
        left_index=2*P_index+1
        right_index=2*P_index+2
    return

def HeapSort(arr):
    n=len(arr)

    # Build heap using Inplace heap
    for i in range(n//2,-1,-1):
        HeapifyDown(arr,i,n)

    # Remove the first element and add it to the last of array and call heapifyDown
    # on the array from index 0 to length -1

    for i in range(n-1,0,-1):
        arr[0],arr[i] = arr[i],arr[0]
        HeapifyDown(arr, 0, i)
    
    return


if __name__=='__main__':
    arr=[int(ele) for ele in input().split()]
    HeapSort(arr)
    for i in arr:
        print(i,end=" ")