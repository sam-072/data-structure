def restTime(a,n):
    a.sort(key=lambda x:x[1])
    c=0
    for i in range(n-1):
        if a[i+1][0]>a[i][1]:
            c+=a[i+1][0]-a[i][1]
    return c



if __name__=='__main__':
    n=int(input())
    a=[]
    for i in range(n):
        a.append(list(map(int,input().split())))
    print(restTime(a,n))