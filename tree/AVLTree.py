class AvlNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.height=1

class AVLTree:
    def __init__(self):
        self.root=None
        self.curr_size=0

    def getHeight(self,root):
        if root is None:
            return 0
        return root.height
    
    def getBalanced(self,temp):
        if temp is None:
            return 0
        return self.getHeight(temp.left) - self.getHeight(temp.right)

    def rightRotation(self,disbalNode):
        newnode=disbalNode.left
        disbalNode.left=disbalNode.left.right
        newnode.right=disbalNode
        disbalNode.height=1+max(self.getHeight(disbalNode.left),self.getHeight(disbalNode.right))
        newnode.height=1+max(self.getHeight(newnode.left),self.getHeight(newnode.right))
        return newnode

    def leftRotation(self,disbalNode):
        newnode=disbalNode.right
        disbalNode.right=disbalNode.right.left
        newnode.left=disbalNode
        disbalNode.height=1+max(self.getHeight(disbalNode.left),self.getHeight(disbalNode.right))
        newnode.height=1+max(self.getHeight(newnode.left),self.getHeight(newnode.right))
        return newnode


    def insert(self,data):
        self.root=self.insertH(self.root,data)
    def insertH(self,root,data):
        if not root:
            return AvlNode(data)
        elif data < root.data:
            root.left=self.insertH(root.left, data)
        else:
            root.right=self.insertH(root.right, data)

        root.height=1+max(self.getHeight(root.left),self.getHeight(root.right))
        bal=self.getBalanced(root)

        # left left condition or right rotation
        if bal > 1 and data <root.left.data:
            return  self.rightRotation(root)

        # left right condition or first left rotation then right rotation
        if bal>1 and data >=root.left.data:
            root.left=self.leftRotation(root.left)
            return self.rightRotation(root) 

        # right right condition or right rotation
        if bal <-1 and data >= root.right.data:
            return self.leftRotation(root)
        
        # right left condition or first right rotation then left rotation
        if bal <-1 and data <root.right.data:
            root.right=self.rightRotation(root.right)
            return self.leftRotation(root)
        
        return root

    def inorderTraversal(self):
        return self.inordhelp(self.root)
    
    def inordhelp(self,root):
        l=[]
        if root != None:
            l.extend(self.inordhelp(root.left))
            l.append(root.data)
            l.extend(self.inordhelp(root.right))
        return l
    
    def getMin(self,root):
        if root is None or root.left is None:
            return root
        return self.getMin(root.left)

    def deleteNode(self,data):
        deleted,root=self.deleteH(self.root,data)
        if root!=None:
            self.curr_size-=1
        return deleted
    def deleteH(self,root,data):
        if root is None:
            return False,root
        if data<root.data:
            deleted,root.left=self.deleteH(root.left, data)
        elif data>root.data:
            deleted,root.right=self.deleteH(root.right, data)
        else:
            if root.left is None:
                temp=root.right
                root=None
                return True,temp
            elif root.right is None:
                temp=root.left
                root=None
                return True,temp
            
            temp=self.getMin(root.right)
            root.data=temp.data
            root.right=self.deleteH(root.right, temp.data)
        
        if root is None:
            return root
        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))

        bal=self.getBalanced(root)
        if bal>1 and self.getBalanced(root.left)>=0:
            return self.rightRotation(root)
        
        if bal<-1 and self.getBalanced(root.right)<=0:
            return self.leftRotation(root)
        
        if bal>1 and self.getBalanced(root.left)<0:
            root.left=self.leftRotation(root.left)
            return self.rightRotation(root)
        
        if bal<-1 and self.getBalanced(root.right)>0:
            root.right=self.rightRotation(root.right)
            return self.leftRotation(root)
            
        return deleted,root

    def preOrderTraversal(self):
        self.level(self.root)
    def level(self,root):
        if root !=None:
            print("data",root.data,"height:",root.height)
            self.level(root.left)
            self.level(root.right)



if __name__=='__main__':
    avl=AVLTree()
    avl.insert(14)
    avl.insert(17)
    avl.insert(11)
    avl.insert(7)
    avl.insert(53)
    avl.insert(4)
    avl.insert(13)
    avl.insert(12)
    avl.insert(8)
    avl.insert(60)
    avl.insert(19)
    avl.insert(16)
    avl.insert(20)

    print(avl.inorderTraversal())
    avl.preOrderTraversal()
    print(avl.deleteNode(8))
    print(avl.deleteNode(7))
    print(avl.deleteNode(11))

    print(avl.inorderTraversal())




