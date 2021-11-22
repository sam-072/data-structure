# Code by : Sam._.072

# Time Complexity : O(N)
# Space Complexity : O(1)

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def delete(head, n):
    fast = head
    slow = head
    t = n
    while t > 0:
        fast = fast.next
        t -= 1
    if fast is None:
        head = slow.next
        return head
    else:
        fast = fast.next
    while fast != None:
        fast = fast.next 
        slow = slow.next
    slow.next = slow.next.next
    return head

def printLL(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.data, end = " ")
        curr_node = curr_node.next
    print(' ')  

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
head = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
head = delete(head, 3)
printLL(head)