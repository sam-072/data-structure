# implementation of queue using linked list
# Sam._.072

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
        self.curr_size=0
    
    def isEmpty(self):
        if self.obj.head==None:
            return True
        return False
    
    def enqueue(self,value):
        newnode=Node(value)
        self.curr_size+=1
        if self.obj.head==None:
            self.obj.head=newnode
            self.obj.tail=newnode
        else:
            self.obj.tail.next=newnode
            self.obj.tail=newnode
    
    def dequeue(self):
        if self.isEmpty():
            return -1
        self.curr_size-=1
        tempnode=self.obj.head.value
        if self.obj.head==self.obj.tail:
            self.obj.head=None
            self.obj.tail=None
        else:
            self.obj.head=self.obj.head.next
        return tempnode

    def peek(self):
        if self.isEmpty():
            return -1
        return self.obj.head.value
    
    def delete(self):
        self.curr_size=0
        self.obj.head=None
        self.obj.tail=None
    
    def size(self):
        return self.curr_size
    
    def print_queue(self):
        temp=self.obj.head
        while temp:
            print(temp.value,end=" ")
            temp=temp.next
        print()

if __name__=="__main__":
    obj=Queue()
    print(obj.isEmpty())
    obj.enqueue(11)
    obj.enqueue(12)
    obj.enqueue(13)
    obj.enqueue(14)
    obj.print_queue()
    print(obj.peek())
    print(obj.size())
    print(obj.dequeue())
    print(obj.dequeue())
    print(obj.dequeue())
    obj.print_queue()
    print(obj.size())
    obj.delete()
    print(obj.size())
