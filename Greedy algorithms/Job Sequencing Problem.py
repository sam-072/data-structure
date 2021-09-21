def JobSecq(a,n):
    a.sort(key=lambda x : x[1],reverse=True)
    h=0
    for i in range(n):
        if a[i][0] > h:
            h=a[i][0]

    l=[0 for i in range(h)]
    c,res = 0,0
    for i in range(n):
        for j in range(a[i][0]-1,-1,-1):
            if l[j]==0:
                c += 1
                l[j]=a[i][1]
                res += a[i][1]
                break
    return c,res


if __name__=='__main__':
    n=int(input())
    a=[]
    for i in range(n):
        a.append(list(map(int, input().split())))
    print(JobSecq(a, n))
