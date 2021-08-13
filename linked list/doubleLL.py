class Node:
    def __init__(self,value=None):
        self.value=value
        self.prev=None
        self.next=None

class DoubleLL:

    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        node =self.head
        while node:
            yield node
            node=node.next

    def size(self):
        c=0
        temp=self.head
        while temp:
            c+=1
            temp=temp.next
        return c
    
    def insert(self,value,location=-1):
        newnode=Node(value)
        if self.head is None:
            newnode.prev=None 
            newnode.next=None 
            self.head=newnode
            self.tail=newnode
            return 1
        elif location==1:
            newnode.prev=None
            newnode.next=self.head
            self.head.prev=newnode
            self.head=newnode
            return 1
        #elif location>=DoubleLL.size(self):
         #   return -1
        elif location==-1:
            newnode.next=None
            newnode.prev=self.tail
            self.tail.next=newnode
            self.tail=newnode
        else:
            temp=self.head
            index=1
            while index < location-1:
                temp=temp.next
                index+=1
            newnode.next=temp.next
            newnode.prev=temp
            temp.next.prev=newnode
            temp.next=newnode
        return 1

    def pop(self,location=-1):
        if self.head is None or location >DoubleLL.size(self):
            return -1
        elif self.head==self.tail:
            self.head=None
            self.tai=None
        elif location==1:
            self.head=self.head.next
            self.head.prev=None
        elif location==-1:
            self.tail=self.tail.prev
            self.tail.next=None
        else:
            temp=self.head
            index=1
            while index<location-1:
                temp=temp.next
                index+=1
            nextnode=temp.next
            temp.next=nextnode.next
            nextnode.next=temp
        return 1

    def delete(self):
        if self.head is None:
            return -1
        else:
            temp=self.head
            while temp:
                temp.prev=None
                temp=temp.next
            self.head=None
            self.tail=None
            return 1

    def search(self,value):
        if self.head is None:
            return -1
        else:
            index=0
            temp = self.head
            while temp:
                index+=1
                if temp.value == value:
                    return index
                temp = temp.next
            return -1
    # merge short which take head as argument and return head of sorted linked list n*log(n)
    def merge(self, first, second):
         
        # If first linked list is empty
        if first is None:
            return second
         
        # If secon linked list is empty
        if second is None:
            return first
 
        # Pick the smaller value
        if first.value < second.value:
            first.next = self.merge(first.next, second)
            first.next.prev = first
            first.prev = None  
            return first
        else:
            second.next = self.merge(first, second.next)
            second.next.prev = second
            second.prev = None
            return second
 
    # Function to do merge sort
    def sort(self, tempHead):
        if tempHead is None:
            return tempHead
        if tempHead.next is None:
            return tempHead
         
        second = self.split(tempHead)
         
        # Recur for left and righ halves
        tempHead = self.sort(tempHead)
        second = self.sort(second)
 
        # Merge the two sorted halves
        return self.merge(tempHead, second)
 
    # Split the doubly linked list (DLL) into two DLLs
    # of half sizes
    def split(self, tempHead):
        fast = slow =  tempHead
        while(True):
            if fast.next is None:
                break
            if fast.next.next is None:
                break
            fast = fast.next.next
            slow = slow.next
             
        temp = slow.next
        slow.next = None
        return temp
         
    #reverse function
    def reverse(self):
        temp = None
        current = self.head
        # Swap next and prev for all nodes of doubly linked list
        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        # Before changing head, check for the cases like empty list and list with only one node
        if temp is not None:
            self.head = temp.prev

dll=DoubleLL()
dll.insert(11 ,1)
dll.insert(12,1)
dll.insert(13,1)
dll.insert(14,2)
dll.insert(15,3)
print([node.value for node in dll])
dll.head=dll.sort(dll.head)
print([node.value for node in dll])
dll.reverse()
print([node.value for node in dll])
