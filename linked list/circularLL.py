class Node:
    def __init__(self,value):
        self.value = value
        self.next=None
    # function to set data
    def setValue(self, value):
        self.value = value

    # function to get data of a particular node
    def getValue(self):
        return self.value

    # function to set next node
    def setNext(self, next):
        self.next = next

    # function to get the next node
    def getNext(self):
        return self.next

class CircularLL:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next
            if node==self.tail.next:
                break
    def size(self):
        temp=self.head
        c=0
        while  temp is not None:
            c+=1
            if temp.next==self.head:
                return c
            temp=temp.next
        return c 
    def insert(self,location ,value):
        newnode=Node(value)
        if self.head is None:
            newnode.next=newnode
            self.head=newnode
            self.tail=newnode
        elif location ==1:
            newnode.next=self.head
            self.head=newnode
            self.tail.next=newnode
        elif location == -1 :
            self.tail.next=newnode
            newnode.next=self.head
            self.tail=newnode
        else:
            temp=self.head
            index=1
            while index <location-1:
                temp=temp.next
                index+=1
            nextnode=temp.next
            temp.next=newnode
            newnode.next=nextnode
    
    def pop(self,location=-1):
        if self.head is None or location >CircularLL.size(self):
            return -1
        else:
            if self.head == self.tail:
                self.head.next=None
                self.head=None
                self.tail=None
            elif location ==1:
                self.head=self.head.next
                self.tail.next=self.head
            elif location == -1:
                temp=self.head
                while temp is not None:
                    if temp.next==self.tail:
                        break
                    temp=temp.next
                temp.next=self.head
                self.tail=temp
            else:
                temp=self.head
                index=1
                while index <location-1:
                    temp=temp.next
                    index+=1
                nextnode=temp.next
                temp.next=nextnode.next
            return 1
    def delete(self):
        self.tail.next=None
        self.tail=None
        self.head=None
        return 1
    def search(self,value):
        if self.head is None:
            return -1
        else:
            temp=self.head
            index=1
            while temp:
                if temp.value==value:
                    return index
                temp=temp.next
                if temp==self.tail.next:
                    return -1


csl=CircularLL()
print(csl.size())
csl.insert(12,10)
print(csl.size())
csl.insert(1,11)
print(csl.size())
csl.insert(1,12)
csl.insert(1,112)
csl.insert(1,122)
csl.insert(2,13)
csl.insert(115,14)
print(csl.size())
csl.insert(-1,15)
csl.insert(-1,16)
print(csl.size())
print([node.value for node in csl])
csl.pop()
print([node.value for node in csl])
print(csl.pop(111))
print([node.value for node in csl])
csl.pop(3)
print([node.value for node in csl])
csl.pop(-1)
print([node.value for node in csl])

