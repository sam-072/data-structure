# Code by : Sam._.072

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
# Time Complexity : O(N + M)
# Space Complexity : O(N+M)

def merge(head1, head2):
    if head1 == None:
        return head2
    if head2 == None:
        return head1
    if head1.data<= head2.data:
        head = Node(head1.data)
        head1 = head1.next
    else:
        head = Node(head2.data)
        head2 = head2.next
    temp = head
    while head1 != None and head2 != None:
        if head1.data <= head2.data:
            node = Node(head1.data)
            temp.next = node
            temp = node
            head1 = head1.next
        else:
            node = Node(head2.data)
            temp.next = node
            temp = node
            head2 = head2.next
    while head1 != None:
        node = Node(head1.data)
        temp.next = node
        temp = node
        head1 = head1.next
    while head2 != None:
        node = Node(head2.data)
        temp.next = node
        temp = node
        head2 = head2.next
    return head

# Time Complexity : O(N+M)
# Space Complexity : O(1)

def merge1(head1, head2):
    if head1.data <= head2.data:
        head = Node(head1.data)
        l1 = head1
        l2 = head2
    else:
        head = Node(head2.data)
        l1 = head2
        l2 = head1
    prev = None
    while l1 != None:
        if l1.data <= l2.data:
            prev = l1
            l1 = l1.next
        else:
            temp.next = l2
            l1, l2 = l2, l1
            temp = l1
    temp.next = l2
    return head
