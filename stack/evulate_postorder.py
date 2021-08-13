import operator
def evulate(s):
    ops = { '+' : operator.add,'-' : operator.sub,'*' : operator.mul,'/' : operator.truediv,  '%' : operator.mod,'^' : operator.xor}
    l=[]
    for i in s:
        if ord(i)>=48 and ord(i)<=57:
            l.append(i)
        else:
            a=int(l.pop())
            b=int(l.pop())
            l.append(ops[i](b,a))
    return l[0]
print(evulate(input()))


