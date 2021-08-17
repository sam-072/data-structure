from collections import deque
class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    
class BinartTree:
    def __init__(self):
        self.root=None
        self.curr_size=0
    
    def buildTree(self,a):
        if len(a)==0 or a[0]==-1:
            self.root=None
        self.root=TreeNode(a[0])
        q=deque()
        q.append(self.root)
        size=1
        i=1
        while size>0 and i<len(a):
            curr_node=q.popleft()
            size-=1
            if a[i]!=-1:
                curr_node.left=TreeNode(a[i])
                self.curr_size+=1
                q.append(curr_node.left)
                size+=1
            i+=1
            if i>=len(a):
                break
            if a[i]!=-1:
                curr_node.right=TreeNode(a[i])
                self.curr_size+=1
                q.append(curr_node.right)
                size+=1
            i+=1
        # return self.root
    
    def PreOrderTraversal(self):
        l=self.prehelp(self.root)
        return l
    def prehelp(self,root):
        l=[]
        if root !=None:
            l.append(root.data)
            l.extend(self.prehelp(root.left))
            l.extend(self.prehelp(root.right))
        return l
    
    def inorderTraversal(self):
        return self.inordhelp(self.root)
    
    def inordhelp(self,root):
        l=[]
        if root != None:
            l.extend(self.inordhelp(root.left))
            l.append(root.data)
            l.extend(self.inordhelp(root.right))
        return l

    def PreOrderTraversal(self):
        return self.posthelp(self.root)
    def posthelp(self,root):
        l=[]
        if root != None:
            l.extend(self.posthelp(root.left))
            l.extend(self.posthelp(root.right))
            l.append(root.data)
        return l
    
    def LevelOrderTraversal(self):
        l=[]
        if self.root != None:
            q=deque()
            q.append(self.root)
            while len(q)>0:
                temp=q.popleft()
                l.append(temp.data)
                if temp.left != None:
                    q.append(temp.left)
                if temp.right != None:
                    q.append(temp.right)
        return l
    
    def search(self,value):
        if self.root is None:
            return -1
        q=deque()
        q.append(self.root)
        while len(q)>0:
            temp=q.popleft()
            if temp.data==value:
                return 1
            if temp.left != None:
                q.append(temp.left) 
            if temp.right != None:
                q.append(temp.right)
        return -1
    
    def size(self):
        return self.curr_size
    
    def height(self):
        return self.heighthelp(self.root)
    def heighthelp(self,root):
        if root is None:
            return 0
        return max(self.heighthelp(root.left),self.heighthelp(root.right))+1
    
    def heightestNode(self):
        return self.heighest(self.root)
    def heighest(self,root):
        if root is None:
            return -1  #this should be the minimun of the your binart tree
        return max(self.heighest(root.left),self.heighest(root.right),root.data)

    def lowestNode(self):
        return self.lowest(self.root)
    def lowest(self,root):
        if root is None:
            return 100000000  # this should be the maximum value of your binary tree
        return min(self.lowest(root.left),self.lowest(root.right),root.data)         

    def no_of_leafNode(self):
        return self.no_leaf(self.root)
    def no_leaf(self,root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        return self.no_leaf(root.left)+self.no_leaf(root.right)
    
    def sum_of_leafNode(self):
        return  self.sumleaf(self.root)
    def sumleaf(self,root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return root.data
        return self.sumleaf(root.left)+self.sumleaf(root.right)
    
    def isleaf(self,root):
        if root is None:
            return False
        if root.left is None and root.right is None:
            return True
        return False
    
    def sum_left_leafNode(self):
        return self.leftLeaf(self.root)
    def leftLeaf(self,root):
        res=0
        if root != None:
            if self.isleaf(root.left):
                res+=root.left.data
            else:
                res+=self.leftLeaf(root.left)
            res+=self.leftLeaf(root.right)
        return res
    
    def sum_right_leafNode(self):
        return self.rightLeaf(self.root)
    def rightLeaf(self,root):
        res=0
        if root != None:
            if self.isleaf(root.right):
                res+=root.right.data
            else:
                res+=self.rightLeaf(root.right)
            res+=self.rightLeaf(root.left)
        return res
    
    def remove_all_leafNode(self):
        self.root=self.removeleaf(self.root)
    def removeleaf(self,root):
        if root is None:
            return None
        if root.left is None and root.right is None:
            return None
        root.left=self.removeleaf(root.left)
        root.right=self.removeleaf(root.right)
        return root
    
    def isBalnced(self):
        h,b=self.isBalncedHelp(self.root)
        return b
    def isBalncedHelp(self,root):
        if root is None:
            return 0,True
        lh,lb=self.isBalncedHelp(root.left)
        rh,rb=self.isBalncedHelp(root.right)
        h=max(lh,rh)+1
        if abs(lh-rh)>1:
            return h,False
        if lb and rb:
            return h, True
        else:
            return h,False

    def diameter(self):
        no_of_edges,no_of_node= self.dia(self.root)
        # if diameter is according to no of edges
        return max(no_of_edges,no_of_node)-1
        # if dimeter is according to no of nodes
        return max(no_of_edges,no_of_node)
    def dia(self,root):
        if root is None:
            return 0,0   #no od edges , no of nodes
        le,ln=self.dia(root.left)
        re,rn=self.dia(root.right)

        return max(le,re)+1, max(rn,ln,le+re+1)

if __name__=='__main__':
    a=list(map(int,input().split()))
    bt=BinartTree()
    bt.buildTree(a)
    l=bt.PreOrderTraversal()
    print(bt.PreOrderTraversal())
    print(bt.inorderTraversal())
    print(bt.PreOrderTraversal())
    print(bt.LevelOrderTraversal())
    print(bt.search(4))
    print(bt.search(7))
    print(bt.search(17))
    print(bt.size())
    print(bt.height())
    print(bt.heightestNode())
    print("the minimum node in binary tree is :",bt.lowestNode())
    print("No of leaf nodes are : ",bt.no_of_leafNode())
    print("sum of all leaf nodes is :",bt.sum_of_leafNode())
    print("sum of all left leaf nodes :",bt.sum_left_leafNode())
    print("sum of all right leaf nodes :",bt.sum_right_leafNode())
    # bt.remove_all_leafNode()
    # print("after removing all leaf nodes :",bt.LevelOrderTraversal())
    print("tree is balned:",bt.isBalnced())
    print("diameter of binary tree:", bt.diameter())