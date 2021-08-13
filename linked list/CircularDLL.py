class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None
        self.prev = None

class CircularDLL:
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next
            if node == self.tail.next:
                break
    def size(self):
        c=0
        temp=self.head
        while  temp is not None:
            c+=1
            if temp.next==self.head:
                return c
            temp=temp.next
        return c 

    def insert(self,value,location=-1):
        newNode=Node(value)
        if self.head is None:
            self.tail=newNode
            self.head = newNode
            newNode.prev=newNode
            newNode.next=newNode
        elif location ==1:
            newNode.next=self.head
            newNode.prev=self.tail
            self.head.prev=newNode
            self.head=newNode
            self.tail.next=newNode
        elif location==-1:
            newNode.prev=self.tail
            newNode.next=self.head
            self.head.prev=newNode
            self.tail.next=newNode
            self.tail=newNode
        else:
            temp=self.head
            index=1
            while index <location-1:
                index+=1
                temp=temp.next
            newNode.next=temp.next
            newNode.prev=temp
            newNode.next.prev=newNode
            temp.next=newNode
        
    def pop(self,location=-1):
        if self.head is None or location >CircularDLL.size(self):
            return -1
        elif self.head==self.tail:
            self.head.prev=None
            self.head.next=None
            self.head=None
            self.tail=None
        elif location==1:
            self.head=self.head.next
            self.head.prev=self.tail
            self.tail.next=self.head
        elif location==-1:
            self.tail=self.tail.prev
            self.tail.next=self.head
            self.head.prev=self.tail
        else:
            temp=self.head
            index=1
            while index<location-1:
                index+=1
                temp=temp.next
            nextnode=temp.next
            temp.next=nextnode.next
            nextnode.prev=temp

    def delete(self):
        if self.head is None:
            return -1
        else:
            self.tail.next=None
            temp=self.head
            while temp:
                temp.prev=None
                temp=temp.next
            self.head=None
            self.tail=None

    def search(self,value):
        if self.head is None:
            return -1
        else:
            index=0
            temp=self.head
            while temp:
                index+=1
                if temp.node==value:
                    return index
                if temp==self.tail:
                    break
                temp=temp.next


cdll=CircularDLL()
print(cdll.size())
cdll.insert(12,1)
cdll.insert(13,1)
cdll.insert(15,2)
cdll.insert(14,-1)
print([node.value for node in cdll])
cdll.pop(14)
print([node.value for node in cdll])
print(cdll.size())