class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None
        self.curr_size=0

    def insertH(self,root,data):
        if root is None:
            newnode=TreeNode(data)
            return newnode
        if data<root.data:
            root.left=self.insertH(root.left,data)
            return root
        else:
            root.right=self.insertH(root.right,data)
            return root

    def insert(self,data):
        self.curr_size+=1
        self.root=self.insertH(self.root,data)

    def size(self):
        return self.curr_size
    
    def isPresent(self,data):
        return self.present(self.root,data)
    
    def present(self,root,data):
        if root is None:
            return False
        if root.data==data:
            return True
        elif data <root.data:
            return self.present(root.left,data)
        else:
            return self.present(root.right,data)
    
    def printH(self,root):
        if root is None:
            return
        print(root.data,end=":")
        if root.left != None:
            print("L",root.left.data,end=" , ")
        if root.right != None:
            print("R",root.right.data,end="")
        print()
        self.printH(root.left) 
        self.printH(root.right) 
        
    def printTree(self):
        self.printH(self.root)
    
    
    

b=BST()
b.insert(10)
b.insert(1)
b.insert(5)
b.insert(11)
b.insert(15)
print(b.size())
print(b.isPresent(10))    
print(b.isPresent(1))    
print(b.isPresent(11))    
print(b.isPresent(15))    
print(b.isPresent(100))    
b.printTree()    


