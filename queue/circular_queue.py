# implementing Queue using python list with size limit

class Queue:
    def __init__(self,maxsize=20):   #default size is 20
        self.list=maxsize*[None]
        self.maxsize=maxsize
        self.curr_size=0
        self.front=-1 
        self.end=-1

    def isEmpty(self):
        return self.front==-1

    def isFull(self):
        if (self.front==0 and self.end+1==self.maxsize) or self.end+1==self.front:
            return True
        return False
    
    def size(self):
        return self.curr_size

    def enqueue(self,value):
        if self.isFull():
            return -1
        else:
            if self.end+1==self.maxsize:
                self.end=0
            else:
                self.end+=1
                if self.front==-1:
                    self.front=0
            self.list[self.end]=value
            self.curr_size+=1
            return 1
    
    def dequeue(self):
        if self.isEmpty():
            return -1
        first_element=self.list[self.front]
        start=self.front
        if self.front==self.end:
            self.front=-1
            self.end=-1
        elif self.front+1==self.maxsize:
            self.front=0
        else:
            self.front+=1
        self.list[start]=None
        self.curr_size-=1
        return first_element
    
    def peek(self):
        if  self.isEmpty():
            return -1
        return self.list[self.front]
    
    def delete(self):
        self.list=self.maxsize*[None]
        self.front=-1
        self.end=-1
        self.curr_size=0

    def print_queue(self):
        i=self.front
        while self.list[i]!= None:
            print(self.list[i],end=" ")
            if i+1==self.maxsize:
                i=0
            else:
                i+=1
            if i==self.front or (self.front==0 and i==self.maxsize):
                break
        print()
        return

if __name__ == '__main__':
    obj=Queue(4)
    print(obj.isEmpty()) 
    print(obj.size()) 
    print(obj.enqueue(11)) 
    print(obj.enqueue(12)) 
    print(obj.enqueue(13))
    print(obj.isFull()) 
    print(obj.enqueue(14))
    print(obj.isFull())
    obj.print_queue()
    print(obj.dequeue())
    print(obj.dequeue())
    print(obj.dequeue())
    print(obj.enqueue(22))
    obj.print_queue()
    print(obj.dequeue())
    print(obj.dequeue())
    print(obj.size())
    print(obj.enqueue(15))
    print(obj.isFull()) 
    print(obj.size())
    print(obj.dequeue())
    print(obj.dequeue())