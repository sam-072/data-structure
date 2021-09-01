def no_of_pairs(a,k):
    d=dict()
    for i in a:
        d[i]=d.get(i,0)+1
    c=0
    for i in d:
        if d.get(k-i,0)>0:
            c+=d[i]*d[k-i]
            d[k-i]=0
            d[i]=0
    return c

if __name__=='__main__':
    a=list(map(int, input().split()))
    b=list(map(int, input().split()))
    # k=int(input())
    print(check(a, b))
