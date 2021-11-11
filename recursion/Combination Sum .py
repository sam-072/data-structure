# Code by : Sam._.072

def CombSum(si, n, a, t, ds, ans):
    if t == 0:
        ans.append(list(ds))
        # print(ans)
        return 
    # pick the element
    for i in range(si,n):
        if t>=a[i]:
            ds.append(a[i])
            CombSum(i, n, a, t-a[i], ds, ans)
            ds.remove(a[i])
      

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    t = int(input())
    a.sort()
    ds,ans = [], []
    CombSum(0, n, a, t, ds, ans)
    print(ans)