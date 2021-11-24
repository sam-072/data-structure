# Code by : Sam._.072

# Time Complexity : O(2M)
# Space Complexity : O(1)

# Optimal Solution 1

def Intersection(head1, head2):
    l1, l2 =0, 0
    temp = head1
    while temp != None:
        l1 += 1
        temp = temp.next
    temp = head2
    while temp != None:
        l2 += 1
        temp = temp.next
    if l1 > l2:
        temp1 = head1
        temp2 = head2
    else:
        temp1 = head2
        temp2 = head1
    d = abs(l1-l2)
    while d > 0:
        d -= 1
        temp1 = temp1.next
    while temp1 != None and temp2 != None:
        if temp1 == temp2:
            return temp1
        temp1 = temp1.next
        temp2 = temp2.next

    return None

# Optimal Solution 2

def Intersection1(head1, head2):
    l1 = head1
    l2 = head2
    while l1 != None and l2 != None:
        if l1 == l2:
            return l1
        if l1.next == None:
            l1 = head2
        else:
            l1 = l1.next
        if l2.next == None:
            l2 = head1
        else:
            l2 = l2.next
    return None
