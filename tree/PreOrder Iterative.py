class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def preOrder(root):
    if root is None:
        return 
    ans=[]
    st=[root]
    while len(st)>0:
        curr = st.pop()
        ans.append(curr.data)
        if curr.right != None:
            st.append(curr.right)
        if curr.left != None:
            st.append(curr.left)
    return ans

if __name__=='__main__':
    root=Node(1)
    root1=Node(2)
    root2=Node(3)
    root3=Node(4)
    root4=Node(5)
    root5=Node(6)
    root.left=root1
    root.right=root2
    root1.left=root3
    root1.right=root4
    root2.left=root5
    print(preOrder(root))



    