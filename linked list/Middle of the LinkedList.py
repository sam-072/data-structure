# Code by : Sam._.072

# Time Complexity : O()
# Space Complexity : O()

# Code by : Sam._.072

# Time Complexity : O(N//2)
# Space Complexity : O(1)

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def MiddleNode(head):
    slow, fast = head, head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
    return slow.data

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
head = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

print(MiddleNode(head))