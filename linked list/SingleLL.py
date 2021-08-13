class Node(object):
    # Each node has its data and a pointer that points to next node in the Linked List
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

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

class SingleLL:

    #construction of this class
    def __init__(self):
        self.head = None
        self.tail = None

    #method to print the element of this class
    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next
    #print method to print element of this class
    def printLL(self):
        head=self.head
        if head is None:
            print(' ')
            return
        curr_node = head
        while curr_node:
            print(curr_node.value, end = " ")
            curr_node = curr_node.next
        print(' ')         

    #find the size of linked list
    def size(self):
        temp=self.head
        c=0
        while temp is not None:
            c+=1
            temp=temp.next
        return c

    #insertation method
    def insert(self,value,location=-1):
        newnode=Node(value)
        if self.head==None:
            self.head=newnode
            self.tail=newnode
            return 0
        elif location > SingleLL.size(self):
            return -1
        else:
            if location==1:
                newnode.next=self.head
                self.head=newnode
            elif location ==-1:
                self.tail.next=newnode
                self.tail=newnode
            else:
                temp=self.head
                index=1
                while index <location-1:
                    temp=temp.next
                    index+=1
                newnode.next=temp.next
                temp.next=newnode
            return 0
    
    #deletion methods
    def pop(self,location=-1):
        if self.head==None or location> SingleLL.size(self):
            return -1
        elif self.head==self.tail:
            self.head=None
            self.tail=None
            return 0
        else:
            if location==1:
                self.head=self.head.next
            elif location ==-1:
                temp=self.head
                while temp is not None:
                    if temp.next==self.tail:
                        break
                    temp=temp.next
                temp.next=None
                self.tail=temp
            else:
                temp=self.head
                index=1
                while index <location-1:
                    temp=temp.next
                    index+=1
                temp.next=temp.next.next
        return 0
    
    #deleting the whole linked list
    def delete(self):
        self.head=None
        self.tail=None
        return 0

    # seach method
    def search(self,value):
        if self.head is None:
            return -1
        else:
            index=0
            temp=self.head
            while temp is not None:
                index+=1
                if temp.value == value:
                    return index
                temp=temp.next
            return -1

    # reversing the linked list
    def reversed(self):
        previous = None
        current = self.head
        while(current != None):
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        self.head = previous

    # function to detect loop in linked list            
    def loop(self):
        s=list()
        temp=self.head
        while temp:
            if temp in s:
                return True
            s.add(temp)
            temp=temp.next
        return False

# sort method which return the head of sorted linked list and which take head as argument
    def sortedMerge(self, a, b):
        result = None
         
        # Base cases
        if a == None:
            return b
        if b == None:
            return a
             
        # pick either a or b and recur..
        if a.value <= b.value:
            result = a
            result.next = self.sortedMerge(a.next, b)
        else:
            result = b
            result.next = self.sortedMerge(a, b.next)
        return result
     
    def sort(self, h):
         
        # Base case if head is None
        if h == None or h.next == None:
            return h
 
        # get the middle of the list
        middle = self.getMiddle(h)
        nexttomiddle = middle.next
 
        # set the next of middle node to None
        middle.next = None
 
        # Apply mergeSort on left list
        left = self.sort(h)
         
        # Apply mergeSort on right list
        right = self.sort(nexttomiddle)
 
        # Merge the left and right lists
        sortedlist = self.sortedMerge(left, right)
        return sortedlist
     
    # Utility function to get the middll of the linked list
    def getMiddle(self, head):
        if (head == None):
            return head
 
        slow = head
        fast = head
 
        while (fast.next != None and fast.next.next != None):
            slow = slow.next
            fast = fast.next.next
             
        return slow

    
               



sl=SingleLL()
sl.insert(10,1)
sl.insert(11,2)
sl.insert(12,1)
sl.insert(13,1)
sl.insert(14,-1)
sl.insert(15,-1)
print([node.value for node in sl])
sl.reversed()
print([node.value for node in sl])
sl.head = sl.sort(sl.head)
print([node.value for node in sl])


