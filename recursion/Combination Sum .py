# Code by : Sam._.072

# Time Complexity : 2^N * K

def CombSum(si, n, a, t, ds, ans):
    if t == 0:
        ans.append(ds[:])
        # print(ans)
        return 
    if si >= n:
        return

    # pick the element
    if si < n and t >= a[si]:
        ds.append(a[si])
        CombSum(si, n, a, t-a[si], ds, ans)
        ds.pop()
    
    # Don't Pick
    CombSum(si+1, n, a, t, ds, ans)
      

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    t = int(input())
    ds,ans = [], []
    CombSum(0, n, a, t, ds, ans)
    print(ans)