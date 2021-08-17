class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def PostOrderTraversal(root):
    l=[]
    if root != None:
        l.extend(PostOrderTraversal(root.left))
        l.extend(PostOrderTraversal(root.right))
        l.append(root.data)
    return l

def buildTreePI(inorder,pre):
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

    leftchild=buildTreePI(linorder,lpre)
    rightchild=buildTreePI(rinorder,rpre)

    root.left=leftchild
    root.right=rightchild

    return root
def solution(inor,pre,n):
    root=buildTreePI(inor, pre)
    l=PostOrderTraversal(root)
    return l
if __name__=='__main__':
    solution([2,3,5,1,6], [1,3,2,5,6],5)
    # PostOrderTraversal(root)
    