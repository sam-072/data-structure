# ------RECURSIVE APPROACH------

def LIS_Recursive(li,i,n,dp):
    if i==n:
        return 0,0
    
    inc_max = 1
    for j in range(i+1,n):
        if li[j] >= li[i]:
            if dp[j]==-1:
                ans = LIS_Recursive(li, j, n, dp)
                dp[j] = ans
                fur_inc_max = ans[0]
            else:
                fur_inc_max = dp[j][0]    
            inc_max = max(inc_max, 1+fur_inc_max)

    if dp[i+1]==-1:
        ans = LIS_Recursive(li, i+1, n, dp)
        dp[i+1] = ans
        exc_max = ans[1]
    else:
        exc_max = dp[i+1][1]

    overall_max = max(inc_max, exc_max)

    return inc_max,overall_max

# ----- ITERATIVE APPROACH------

def LIS(li,n):
    dp = [[0 for i in range(2)] for j in range(n+1)]

    for i in range(n-1,-1,-1):
        inc_max = 1
        for j in range(i+1,n):
            if li[j] > li[i]:
                inc_max = max(inc_max, 1+dp[j][0])
        dp[i][0] = inc_max
        exc_max = dp[i+1][1]
        overall_max = max(inc_max, exc_max)
        dp[i][1] = overall_max
    
    return dp[0][1]

# ------USING BINARY SEARCH------
# Time Complexity : O(N*logN)
# Space Complexity : O(N)

def LIS_BS(arr):
    n = len(arr)
    tail = [arr[0]]
    l = 1
    for i in range(1,n):
        if arr[i] > tail[l-1]:
            tail.append(arr[i])
            l += 1
        else:
            c = ceilIndex(tail, 0, l-1, arr[i])
            tail[c] = arr[i]
    return l

def ceilIndex(tail, l, r, x):
    while r > l:
        m = l + (r-l)//2
        if tail[m] >= x:
            r = m
        else:
            l = m+1
    return r


n=int(input())
li=list(map(int, input().split()))
dp=[-1 for i in range(n+1)]
ans=LIS_Recursive(li, 0, n, dp)[1]
print(ans)
print(LIS(li, n))
print(LIS_BS(li))

    