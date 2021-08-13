class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Node:
    def __init__(self,value):
        self.value = value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

class Queue:
    def __init__(self):
        self.obj=LinkedList()
    
    def isEmpty(self):
        if self.obj.head==None:
            return True
        return False
    
    def enqueue(self,value):
        newnode=Node(value)
        if self.obj.head==None:
            self.obj.head=newnode
            self.obj.tail=newnode
        else:
            self.obj.tail.next=newnode
            self.obj.tail=newnode
    
    def dequeue(self):
        if self.isEmpty():
            return -1
        tempnode=self.obj.head.value
        if self.obj.head==self.obj.tail:
            self.obj.head=None
            self.obj.tail=None
        else:
            self.obj.head=self.obj.head.next
        return tempnode



def PreOrderTraversal(root):
    if root is None:
        return
    print(root.data)
    PreOrderTraversal(root.left)
    PreOrderTraversal(root.right)

def InOrderTraversal(root):
    if root is None:
        return
    InOrderTraversal(root.left)
    print(root.data)
    InOrderTraversal(root.right)

def PostOrderTraversal(root):
    if root is None:
        return
    PostOrderTraversal(root.left)
    PostOrderTraversal(root.right)
    print(root.data)

def LevelOrderTraversal(root):
    if root is None:
        return 
    obj=Queue()
    obj.enqueue(root)
    while obj.isEmpty() is False:
        temp=obj.dequeue()
        print(temp.data)
        if temp.left is not None:
            obj.enqueue(temp.left)
        if temp.right is not None:
            obj.enqueue(temp.right)    

def searchBT(root,value):
    if root is None:
        return -1
    obj1=Queue()
    obj1.enqueue(root)
    while obj1.isEmpty() is False:
        temp=obj1.dequeue()
        if temp.data == value:
            return 1
        if temp.left is not None:
            obj1.enqueue(temp.left)
        if temp.right is not None:
            obj1.enqueue(temp.right)
    return -1

# this function insert nodes at level order
def insertBT():
    a=input()
    if a[0]!=-1:
        root=TreeNode(a[0])
        obj=Queue()
        obj.enqueue(root)
        print(root)
    else:
        return None
    for i in range(1,len(a),2):
        temp=obj.dequeue()
        if a[i]!=-1:
            newnode=TreeNode(a[i])
            temp.left=newnode
            obj.enqueue(newnode)
        if a[i+1]!=-1:
            newnode=TreeNode(a[i])
            temp.right=newnode
            obj.enqueue(newnode)
    return root

def sizeBT(root):
    if root is None:
        return 0
    else:
        return 1 +sizeBT(root.left)+sizeBT(root.right)

def deepestNode(root):
    if root is None:
        return
    obj=Queue()
    obj.enqueue(root)
    while not(obj.isEmpty()):
        temp=obj.dequeue()
        if temp.left is not None:
            obj.enqueue(temp.left)
        if temp.right is not None:
            obj.enqueue(temp.right)
    return temp

def delDeepestNode(root,dp):
    if root is None:
        return
    obj=Queue()
    obj.enqueue(root)
    while not(obj.isEmpty()):
        temp=obj.dequeue()
        if temp is dp:
            dp=None
            return
        if temp.right:
            if temp.right is dp:
                temp.right = None
                return
            else:
                obj.enqueue(temp.right)
        if temp.left:
            if temp.left is dp:
                temp.left =None
                return
            else:
                obj.enqueue(temp.left)
        
        

def deleteNodeBT(root,node):
    if root is None:
        return -1
    obj=Queue()
    obj.enqueue(root)
    while not(obj.isEmpty()):
        temp=obj.dequeue()
        if temp.data==node:
            dp=deepestNode(root)
            print("deepest node : ",dp.data)
            temp.data=dp.data
            delDeepestNode(root,dp)
        if temp.left is not None:
            obj.enqueue(temp.left)
        if temp.right is not None:
            obj.enqueue(temp.right)
    return -1

def deleteBT(root):
    root.data=None
    root.left=None
    root.right=None

def largestData(root):
    if root is None:
        return -1 #that is the minum number from the given tree , ideally it should be minus infinity
    return max(largestData(root.left),largestData(root.right),root.data) 

def minValue(root):
    if root is None:
        return 100000   # height value in tree
    return min(minValue(root.left),minValue(root.right),root.data)

def heightBT(root):
    if root is None:
        return 0
    return max(heightBT(root.left),heightBT(root.right))+1

def isleaf(root):
    if root is None:
        return False
    if root.left is None and root.right is None:
        return True
    return False

def noLeafNode(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return noLeafNode(root.left)+noLeafNode(root.right)

def sumleafs(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return root.data
    return sumleafs(root.left)+sumleafs(root.right)

def sumleftleafs(root):
    res=0
    if root is not None:
        if isleaf(root.left):
            res+=root.left.data
        else:
            res+=sumleftleafs(root.left)
        res+=sumleftleafs(root.right)
    return res

def sumrightleafs(root):
    res=0
    if root is not None:
        if isleaf(root.right):
            res+=root.right.data
        else:
            res+=sumrightleafs(root.right)
        res+=sumrightleafs(root.left)
    return res

def printDepthK(root,k):
    if root is None:
        return
    if k==0:
        print(root.data)
        return
    printDepthK(root.left,k-1)
    printDepthK(root.right,k-1)

def printAtDepthV2(root,k,d=0):
    if root is None:
        return
    if d==k:
        print(root.data)
        return
    printAtDepthV2(root.left,k,d+1)
    printAtDepthV2(root.right,k,d+1)

# this function removes all the leaf nodes from the tree
def removeLeafs(root):
    if root is None:
        return None
    if root.left is None and root.right is None:
        return None
    root.left=removeLeafs(root.left)
    root.right=removeLeafs(root.right)
    return root

# this function will check is binary tree is balnced or not . In wrost case it will
#  take O(n^2) just like in bubble sort where as in best case it will take O(n log n) just like merge sort
def isBlanced(root):
    if root is None:
        return True
    lh=heightBT(root.left)
    rh=heightBT(root.right)
    if abs(lh-rh)>1:
        return False
    if isBlanced(root.right) and isBlanced(root.left):
        return True
    else:
        return False

# this is a better version of isBalnced function and this function takes O(n)
def isBlancedV2(root):
    if root is None:
        return 0,True
    lh,lb=isBlancedV2(root.left)
    rh,rb=isBlancedV2(root.right)
    h=max(lh,rh)+1
    if abs(lh-rh)>1:
        return h,False
    if lb and rb:
        return h,True
    else:
        return h,False

def isBlanced2(root):
    h,t=isBlancedV2(root)
    return t

# this function return the diameter of the tree but it takes O(n^2) in wrost case
# and O(n log n) in best case
def diameterBT(root):
    if root is None:
        return 0
    h=heightBT(root.left)+heightBT(root.right)
    dl=diameterBT(root.left)
    dr=diameterBT(root.right)
    return max(h,dl,dr)

# this is a better version of diameter of tree because it takes O(n) times
# this is optimised class for height and diameter
def diameterBT2(root):
    if root is None:
        return 0,0
    l1,r1=diameterBT2(root.left)
    l2,r2=diameterBT2(root.right)
    return max(l1,l2)+1 , max(r1,r2,l1+l2+1)

def diameter(root):
    l,r=diameterBT2(root)
    return max(l,r)-1
    
# this function will build tree using inorder and preOrder
def buildTreePI(pre,inorder):
    if len(pre)==0:
        return None
    
    rootData=pre[0]
    root=TreeNode(rootData)

    rootI=-1
    for i in range(len(inorder)):
        if inorder[i]==rootData:
            rootI=i
            break
    if rootI==-1:
        return None
    linorder=inorder[:rootI]
    rinorder=inorder[rootI+1:]

    l=len(linorder)  # this will find the length of left inorder or left subtree
    lpre=pre[1:l+1]
    rpre=pre[l+1:]

    leftchild=buildTreePI(lpre,linorder)
    rightchild=buildTreePI(rpre,rinorder)

    root.left=leftchild
    root.right=rightchild

    return root

def buildTree(In, post):
    if len(post)==0 or len(In)==0 or len(In)!=len(post):
        return None
    rootdata=post[-1]
    root=Node(rootdata)
    rootI=-1
    for i in range(len(In)):
        if In[i]==rootdata:
            rootI=i
            break
    if rootI==-1:
        return None
    lIn=In[:rootI]
    rIn=In[rootI+1:]
    # print("inorder",lIn,rIn)
    l=len(lIn)
    lpost=post[:l]
    rpost=post[l:-1]
    # print("postorder",lpost,rpost)
    
    leftchild=buildTree(lIn,lpost)
    rightchild=buildTree(rIn,rpost)
    
    root.left=leftchild
    root.right=rightchild
    
    return root
    

# pre=[1,2,4,8,9,10,11,5,3,6,7]
# io=[8,4,10,9,11,2,5,1,6,3,7]
# root=buildTreePI(pre,io)
# LevelOrderTraversal(root)
# print(">>>>>>>>>>>>>>>>>>>>>>")
post=[9,1,2,12,7,5,3,11,4,8]
In=[9,5,1,7,2,12,8,4,3,11]
root1=buildTree(In,post)
print(root1)
InOrderTraversal(root1)
LevelOrderTraversal(root1)


# class BSTree:
# root=TreeNode("Drink")
# cold=TreeNode("cold")
# hot=TreeNode("hot")
# tea=TreeNode("tea")
# coffee=TreeNode("coffee")
# cola=TreeNode("cola")
# sprit=TreeNode("sprit")
# root.leftChild=hot
# root.rightChild=cold
# hot.leftChild=tea
# hot.rightChild=coffee
# cold.leftChild=sprit
# cold.rightChild=cola
# # root=removeLeafs(root)
# LevelOrderTraversal(root)
# print(isBlancedV2(root))
# print(diameterBT(root))
# LevelOrderTraversal(root)
# insertBT(root,"sam")

if __name__ == '__main__':
    root=TreeNode(10)
    root1=TreeNode(100)
    root2=TreeNode(1)
    root3=TreeNode(12)
    root4=TreeNode(124)
    root.left=root1
    root.right=root2
    root1.left=root3
    root1.right=root4
    # PreOrderTraversal(root)
    # print(">>>>>>>>>>>>>>")
    # InOrderTraversal(root)
    # print(">>>>>>>>>>>>>>")
    # PostOrderTraversal(root)
    # print(">>>>>>>>>>>>>>")
    # LevelOrderTraversal(root)
    # print(">>>>>>>>>>>>>>")
    # print(searchBT(root,12))
    # print(searchBT(root,124))
    # print(searchBT(root,1))
    # print(searchBT(root,11223))
    # print(">>>>>>>>>>>>>>")
    # print(deepestNode(root).data)
    # # deleteNodeBT(root,1)
    # LevelOrderTraversal(root)
    # print(heightBT(root))
    # print(noLeafNode(root))
    # print(largestData(root))
    # print(minValue(root))
    # print(sizeBT(root))
    # print(sumleafs(root))
    # printDepthK(root,2)
    # printAtDepthV2(root, 0, 2)
    # print(isleaf(root4))
    # print(isleaf(root))
    # print(sumleftleafs(root))
    # print(sumrightleafs(root))
    print(isBlanced2(root))
    print(diameter(root))