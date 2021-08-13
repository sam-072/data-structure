import operator
class treeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
ops = { '+' : operator.add,'-' : operator.sub,'*' : operator.mul,'/' : operator.truediv,  '%' : operator.mod,'^' : operator.xor}

def mirror(root):
    if root is None:
        return 
    l=mirror(root.left)
    r=mirror(root.right)
    root.left=r
    root.right=l
    return root

def expression(root):
    if root is None:
        return
    l=expression(root.left)
    r=expression(root.right)
    return ops[root.data](l.data,r.data)

def pre(root):
    if root is None:
        return
    print(root.data)
    pre(root.left) 
    pre(root.right)

if __name__ == '__main__':
    root=treeNode('+') 
    t1=treeNode("*") 
    t2=treeNode("-") 
    t3=treeNode(5) 
    t4=treeNode(4) 
    t5=treeNode(100) 
    t6=treeNode(20) 

    root.left=t1
    root.right=t2
    t1.left=t3 
    t1.right=t4
    t2.left=t5
    t2.right=t6
    pre(root)
    # mirror(root)
    print(">>>>>>>>>>>>>>>>>>")
    # pre(root) 
    print(expression(root))