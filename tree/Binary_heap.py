class BHeap:
    def __init__(self,maxsize=10):
        self.a=(maxsize+1)*[None]
        self.curr_size=0
        self.maxSize=maxsize
    
def peek(root):
    if not root:
        return 
    return root.a[1]
    
def size(root):
    if not root:
        return
    return root.curr_size
    
def levelOrderTraversal(root):
    if not root:
        return
    l=[]
    for i in range(1,root.curr_size+1):
        l.append(root.a[i])
    return l
    
def heapifyI(root,index,HeapType):
    parentIndex=int(index/2)
    if parentIndex<1:
        return
    if HeapType=="Min":
        if root.a[parentIndex]>root.a[index]:
            root.a[parentIndex],root.a[index]=root.a[index],root.a[parentIndex]
        heapifyI(root, parentIndex, HeapType)
    
    elif HeapType=="Max":
        if root.a[parentIndex]<root.a[index]:
            root.a[parentIndex],root.a[index]=root.a[index],root.a[parentIndex]
        heapifyI(root, parentIndex, HeapType)
    
def inserNode(root,data,Heaptype):
    if root.curr_size==root.maxSize:
        return -1
    root.curr_size+=1
    root.a[root.curr_size]=data
    heapifyI(root, root.curr_size, Heaptype)
    return 1

def heapifyE(root,index,heapType):
    leftIndex=2*index
    rightIndex=2*index + 1
    swapIndex=0
    if root.curr_size<leftIndex:
        return
    elif root.curr_size==leftIndex:
        if heapType=="Min":
            if root.a[parentIndex]>root.a[index]:
                root.a[parentIndex],root.a[index]=root.a[index],root.a[parentIndex]
            return
        else:
            if root.a[parentIndex]<root.a[index]:
                root.a[parentIndex],root.a[index]=root.a[index],root.a[parentIndex]
            return
    else:
        if heapType=='Min':
            
            if root.a[leftIndex]<root.a[rightIndex]:
                swapIndex=leftIndex
            else:
                swapIndex=rightIndex
            if root.a[index] > root.a[swapIndex]:
                root.a[index],root.a[swapIndex]=root.a[swapIndex],root.a[index]
        
        else:

            if root.a[leftIndex] > root.a[rightIndex]:
                swapIndex=leftIndex
            else:
                swapIndex=rightIndex
            if root.a[index] < root.a[swapIndex]:
                root.a[index],root.a[swapIndex]=root.a[swapIndex],root.a[index]
        
    heapifyE(root, swapIndex, heapType)


def extractNode(root,HeapType):
    if root.curr_size==0:
        return
    extractedNode=root.a[1]
    root.a[1]=root.a[root.curr_size]
    root.a[root.curr_size]=None
    root.curr_size-=1
    heapifyE(root, 1, heapType)
    return extractedNode





if __name__=='__main__':
    root=BHeap(5)
    
    print(inserNode(root, 6, "Min"))
    print(inserNode(root, 16, "Min"))
    print(inserNode(root, 62, "Min"))
    print(inserNode(root, 36, "Min"))
    print(inserNode(root, 66, "Min"))
    print(inserNode(root, 69, "Min"))
    print(peek(root))
    print(size(root))
    print(levelOrderTraversal(root))