# problem name : Zero Sum Subarrays
# problem link : https://practice.geeksforgeeks.org/problems/zero-sum-subarrays1825/0/?track=md-hashing&batchId=144
# topic : hashing

def Subarrays(a,n):
    l=[]
    c=0
    z=z1=0
    for i in range(n):
        if a[i]==0:
            c+=1
        z+=a[i]
        l.append(z)
        if a[i]<0:
            z1=-1
    print(l)
    if z1==-1:
        d=dict()
        for i in l:
            d[i]=d.get(i,0)+1
        print(d)
        for i in d:
            c+=(d[i]*(d[i]-1))//2
        return c
    else:
        d=dict()
        for i in l:
            d[i]=d.get(i,0)+1
        for i in d:
            if i==0:
                c+=(d[i]*(d[i]-1))//2
            else:
                c+=(d[i]-2)*(d[i]-1)//2
        return c
n=int(input())
a=list(map(int, input().split()))
print(Subarrays(a, n))

