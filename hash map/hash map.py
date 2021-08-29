class hashNode:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None

class HashMap:
    def __init__(self,bucketsize=10):
        self.bucketsize=bucketsize
        self.bucket=(self.bucketsize)*[None]
        self.curr_size=0
    
    def size(self):
        return self.curr_size

    def insert(self,key,value):
        hc=hash(key)
        index=abs(hc) % self.bucketsize
        head=self.bucket[index]
        while head is not None:
            if head.key==key:
                head.value=value
                return
            head=head.next
        head=self.bucket[index]
        newnode=hashNode(key, value)
        newnode.next=head
        self.bucket[index]=newnode
        self.curr_size+=1
        # check for load factor

        loadFactor=self.curr_size/self.bucketsize
        if loadFactor>=0.7:
            self.rehash()
    
    def rehash(self):
        temp=self.bucket
        self.bucket=(2*self.bucketsize)*[None]
        self.bucketsize=2*self.bucketsize
        self.curr_size=0
        for head in temp:
            while head is not None:
                self.insert(head.key, head.value)
                head=head.next
    
    def getValue(self,key):
        hc=hash(key)
        index=abs(hc)%self.bucketsize
        head=self.bucket[index]
        while head is not None:
            if head.key==key:
                return head.value
            head=head.next
        return None
    
    def remove(self,key):
        hc=hash(key)
        index=abs(hc)%self.bucketsize
        head=self.bucket[index]
        prev=None
        while head is not None:
            if head.key==key:
                if prev is None:
                    self.bucket[index]=head.next
                else:
                    prev.next=head.next
                self.curr_size-=1
                return head.value
            prev=head
            head=head.next
        return None


if __name__=='__main__':
    m=HashMap()
    m.insert('abc', 12)
    m.insert('abc1', 121)
    m.insert('abc2', 122)
    m.insert('abc3', 312)
    print(m.size())
    print(m.remove('abc'))
    print(m.getValue('abc3'))
    print(m.getValue('abc'))