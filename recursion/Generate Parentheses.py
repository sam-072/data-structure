# Code by : Sam._.072

def Parentheses(n):
    if n==1:
        return ['()']
    l = Parentheses(n-1)
    s=set()
    for i in l:
        s.add('()'+i)
        s.add(i+'()')
        s.add('('+i+')')
    return list(s)

l=Parentheses(4)
# l.sort()
for i in l:
    print(i)