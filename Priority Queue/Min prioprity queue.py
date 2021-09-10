class PriorityNode:
    def __init__(self,value,priority):
        self.value=value
        self.priority=priority

class MinPriority:
    def __init__(self):
        self.pl=[0]
    
    def getSize(self):
        return len(self.pl)-1
    
    def isEmpty(self):
        return len(self.pl)==1
    
    def getMin(self):
        if self.isEmpty():
            return None
        return self.pl[1].value
    
    def insert(self,value,priority):
        newNode=PriorityNode(value, priority)
        self.pl.append(newNode)
        self.__HeapifyUp()

    def __HeapifyUp(self):
        C_index=self.getSize()-1
        while C_index>1:
            P_index=C_index//2
            if self.pl[C_index].priority < self.pl[P_index].priority:
                self.pl[C_index],self.pl[P_index]=self.pl[P_index],self.pl[C_index]
                C_index=P_index
            else:
                break
    
    def removeMin(self):
        if self.isEmpty():
            return None

        ele=self.pl[1].value
        self.pl[1]=self.pl[-1]
        self.pl.pop()
        self.__HeapifyDown()
        return ele
    
    def __HeapifyDown(self):
        P_index=1
        left_index = 2*P_index
        right_index = 2*P_index+1
        while left_index < self.getSize():
            min_index=P_index
            if self.pl[min_index].priority > self.pl[left_index].priority:
                min_index=left_index
            
            if right_index < self.getSize() and self.pl[min_index].priority > self.pl[right_index].priority:
                min_index=right_index
            
            if min_index==P_index:
                break

            self.pl[min_index],self.pl[P_index] = self.pl[P_index],self.pl[min_index]
            P_index=min_index
            left_index = 2*P_index
            right_index = 2*P_index+1

            

if __name__=='__main__':
    n=int(input())
    pq=MinPriority()
    print(pq.isEmpty())
    print(pq.getSize())
    for i in range(n):
        inp=list(input().split())
        v=inp[0]
        p=int(inp[1])
        pq.insert(v, p)
    print(pq.getSize())
    print(pq.getMin())
    for i in range(n):
        print(pq.removeMin())

    

        