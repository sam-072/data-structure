# implementing stack using linked list
# Sam._.072

# defining class node for creating every new node
class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None
# defining linked list class
class LinkedList:
    def __init__(self):
        self.head=None
    
    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next

# defining stack class which contains all stacks functions
class Stack:
    def __init__(self):
        self.obj=LinkedList()
        self.curr_size=0
    
    # this function return True if stcak is empty otherwise it return False
    def isEmpty(self):
        return self.obj.head==None

    # this function push an element on the stack
    def push(self,value):
        newnode=Node(value)
        self.curr_size+=1
        newnode.next=self.obj.head
        self.obj.head=newnode
    
    # this function pop an element from the stack
    def pop(self):
        if self.isEmpty():
            return -1
        self.curr_size-=1
        nodevalue=self.obj.head.value
        self.obj.head=self.obj.head.next
        return nodevalue
    
    # this function return the top element of the stack
    def peek(self):
        if self.isEmpty():
            return -1
        return self.obj.head.value
    
    # this function delete the whole stack
    def delete(self):
        self.curr_size=0
        self.obj.head=None
    
    # this function return the current size of the stack
    def size(self):
        return self.curr_size

    # this function print the stack
    def printstack(self):
        if self.isEmpty():
            return -1
        temp=self.obj.head
        while temp:
            print(temp.value)
            temp=temp.next
        return 

# main function 
if __name__=='__main__':
    obj=Stack()
    s=input()
    for i in s:
        if i=='(' or i=='{' or i=='[':
            obj.push(i)
        elif i==']':
            print(obj.peek())
            if obj.peek()== ']':
                print("true12")
            while obj.peek() != ']':
                print("shyam")
                break
            print(obj.pop())
    # obj.printstack()
    if obj.size()==0:
        print(True)
    else:
        print(False)






