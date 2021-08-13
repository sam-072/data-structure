import operator
def evulate(s):
    ops = { '+' : operator.add,'-' : operator.sub,'*' : operator.mul,'/' : operator.truediv,  '%' : operator.mod,'^' : operator.xor,}
    l=[]
    for i in range(len(s)-1,-1,-1):
        if ord(s[i])>=48 and ord(s[i])<=57:
            l.append(i)
        else:
            a=int(l.pop())
            b=int(l.pop())
            l.append(ops[s[i]](a,b))
    return l[0]
s=input()
print(evulate(s))