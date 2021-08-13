class stack:
    def __init__(self,size=10):
        self.maxsize=size   #this is the max size of our stack
        self.list=[]
        self.curr_size=0       # this will tell the current size of the stack

    # this function is used to print the stack 
    def print_stack(self):
        values=[str(self.list[x]) for x in range(self.curr_size-1,-1,-1)]
        return '\n'.join(values)

    # this funtion is for checking the stack is full or not , if it is full then it return True
    #  otherwise it return False
    def isFull(self):
        return self.size==self.maxsize

    # this function check is stack empty or not , if it is empty the return True otherwise return False
    def isEmpty(self):
        return self.list==[]

    # this function return the xurrent size of the stack
    def size(self):
        return self.curr_size

    # this function is used to push an element in the stack
    def push(self,value):
        if self.isFull():
            return -1
        self.list.append(value)
        self.curr_size+=1

    # this function is used to pop an element from from stcak
    def pop(self):
        if self.isEmpty():
            return -1
        self.curr_size-=1
        return self.list.pop()

    #  this function return the top element of the stack
    def peek(self):
        if self.isEmpty():
            return -1
        return self.list[-1]

    # this function delete the whole stack
    def delete(self):
        self.curr_size=0
        self.list=None


def infixToPrefix(s):
    op={ '+' :1, '-' : 1, '*' : 2, '/' : 2, '^' :3, '(':0,')':-1, '[':0,']':-1, '{':0,'}':-1}
    s1,s2="",""
    obj=stack()
    for i in range(len(s)-1,-1,-1):
        if s[i]==')':
            s2+='('
        elif s[i]=='(':
            s2+=')'
        else:
            s2+=s[i]
    for i in s2:
        if (ord(i)>=48 and ord(i)<=57) or (ord(i)>=65 and ord(i)<=90) or(ord(i)>=97 and ord(i)<=122):
            s1+=i
        else:
            if obj.isEmpty():
                obj.push(i)
            elif op[i]==0:
                obj.push(i)
            elif op[obj.peek()]==0 and op[i]!=-1:
                obj.push(i)
            elif op[i]==-1:
                while op[obj.peek()]!=0:
                    s1+=obj.pop()
                obj.pop()
            elif op[i]>op[obj.peek()]:
                obj.push(i)
            elif op[i]<op[obj.peek()] :
                s1+=obj.pop()
                while obj.isEmpty()!=True and  op[i]<op[obj.peek()] :
                    s1+=obj.pop()
                obj.push(i)
            else:
                obj.push(i)
    while obj.curr_size>0:
        s1+=obj.pop()
    s=""
    for i in range(len(s1)-1,-1,-1):
        s+=s1[i]
    return s

if __name__ =='__main__':
    s=input()
    print(infixToPrefix(s))

            

