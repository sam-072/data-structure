# Code by : Sam._.072

n = int(input())
a = [0 for i in range(2*n+1)]
a[n-1]=1
for i in range(1,n):
    for j in range(2*n+1):
        if a[j]!=0:
            print(a[j],end=" ")
        else:
            print(" ",end=" ")
    for j in range(n-i-1,n+i):
        if i%2==j%2:
            a[j] = a[j-1]+a[j+1]
    for j in range(2*n+1):
        if i%2!=j%2:
            a[j]=0
    print()
    

