# Code by : Sam._.072

n, m = map(int, input().split())
if m <= n:
    print(n-m)
else:
    c=0
    while m>n:
        if m%2==0:
            m=m//2
        else:
            m+=1
        c+=1
    print(n-m+c)