# Code by : Sam._.072

def check(n, a, l, h):
    for i in range(1, n-1):
        if a[i]>l[i] and a[i]>h[i] and h[i]>l[i]:
            return True
    return False

n = int(input())
a = list(map(int, input().split()))
l = [-1 for i in range(n)]
x = a[0]
for i in range(1,n):
    if x<a[i]:
        l[i] = x
    else:
        x = a[i]

h = [-1 for i in range(n)]
x = a[-1]
for i in range(n-2,-1,-1):
    if x < a[i]:
        h[i]=x
    else:
        x = a[i]
print(l)
print(h)
print(check(n, a, l, h))



