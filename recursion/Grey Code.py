# Code by : Sam._.072

def GreyCode(n):
    if n==1:
        return ['0', '1']
    l = GreyCode(n-1)
    l1 = l[::-1]
    for i in range(len(l)):
        l[i] = '0' + l[i]
        l1[i] = '1' + l1[i]
    l.extend(l1)
    return l

print(GreyCode(1)) 

    