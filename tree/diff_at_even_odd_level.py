class treeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
os,es=0,0
def diif_level(root,es,os,k=0):
    if root is None:
        return 0
    if k%2==0:
        es+=root.data
    else:
        os+=root.data
    diif_level(root.left,es,os,k+1)
    diif_level(root.right,es,os,k+1)
    

if __name__ == '__main__':
    root=treeNode(1)
    t2=treeNode(2)
    t9=treeNode(9)
    t3=treeNode(3)
    t5=treeNode(5)
    t7=treeNode(7)
    root.left=t2
    root.right=t9
    t2.left=t3
    t2.right=t5
    t9.right=t7
    print(diif_level(root,es,os))
    print(os,es)