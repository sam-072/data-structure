def Knapsack(a,n,w):
    a.sort(key=lambda x : x[2],reverse=True)
    c,curr_w=0,w
    for i in range(n):
        if a[i][0] <= curr_w:
            c+=a[i][1]
            curr_w -= a[i][0]
        else:
            c += curr_w * a[i][2]
            return c
        

if __name__=='__main__':
    n,w=map(int, input().split())
    a=[]
    for i in range(n):
        x,y=map(int, input().split())
        a.append([x,y,y/x])
    print(Knapsack(a, n, w))