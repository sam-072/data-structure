from collections import deque
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Tree:
    def __init__(self):
        self.root = None
        self.curr_size = 0
    
    def buildTree(self,a):
        if len(a)==0 or a[0]==-1:
            self.root=None
        self.root = Node(a[0])
        q=deque()
        q.append(self.root)
        k=1
        i=1
        n=len(a)
        while k>0 and i<n:
            curr_node = q.popleft()
            k-=1
            if a[i] != -1:
                curr_node.left = Node(a[i])
                q.append(curr_node.left)
                self.curr_size+=1
                k+=1
            
            i+=1
            
            if i>=n:
                break

            if a[i] != -1:
                curr_node.right=Node(a[i])
                q.append(curr_node.right)
                k+=1
                self.curr_size+=1
            
            i+=1
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
    
    
if __name__=='__main__':
    a=list(map(int, input().split()))
    t=Tree()
    t.buildTree(a)
    print(t.PreOrderTraversal())


