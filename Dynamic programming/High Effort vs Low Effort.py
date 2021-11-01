# Code by : Sam._.072

def Effort(n,hi,li,i,k):
    if i==n:
        return 0
    ans = 0
    if k==0:
        ans += max(0+Effort(n, hi, li, i+1, 0), li[i]+Effort(n, hi, li, i+1, 1), hi[i]+Effort(n, hi, li, i+1, 2))
    elif k==1 or k==2:
        ans += max(0+Effort(n, hi, li, i+1, 0), li[i]+Effort(n, hi, li, i+1, 1))
    return ans

def EffortHigh(n,hi,li):
    dp = [[0]for i in range(n+1)]
    dp[0],dp[1] = 0, hi[0]
    for i in range(2,n+1):
        dp[i] = max(hi[i-1]+dp[i-2], li[i-1]+dp[i-1])
    # print(dp)
    return dp[n]


if __name__ == '__main__':
    n = int(input())
    hi = list(map(int,input().split()))
    li = list(map(int,input().split()))
    print(Effort(n, hi, li, 0, 0)) 
    print(EffortHigh(n, hi, li))