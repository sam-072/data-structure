# queue implementation without without size limit
class Queue:
    # construction of the queue class 
    def __init__(self):
        self.list=[]
        self.curr_size=0

    def isEmpty(self):
        return self.list==[]
    
    def enqueue(self,value):
        self.list.append(value)
        self.curr_size+=1
    
    def dequeue(self):
        if self.isEmpty():
            return -1
        self.curr_size-=1
        return self.list.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return -1
        return self.list[0]
    
    def delete(self):
        self.list=None
        self.curr_size=0

    def size(self):
        return self.curr_size
    
    def print_Queue(self):
        print(*self.list)
        return 
    
if __name__ == '__main__':
    obj=Queue()
    print(obj.isEmpty())
    print(obj.size())
    obj.enqueue(1)
    obj.enqueue(12)
    obj.enqueue(11)
    print(obj.peek())
    print(obj.size())
    obj.print_Queue()
    print(obj.dequeue())
    print(obj.dequeue())
    print(obj.dequeue())
    
