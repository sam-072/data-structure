# Code by : Sam._.072

import sys
def MCM(a,s,e,dp):
    if s==e:
        return 0
    ans=sys.maxsize
    for k in range(s,e):
        if dp[s][k]==-1:
            ans1 = MCM(a, s, k, dp)
            dp[s][k] = ans1
        else:
            ans1 = dp[s][k]
        if dp[k+1][e]==-1:
            ans2 = MCM(a, k+1, e, dp)
            dp[k+1][e] = ans2
        else:
            ans2 = dp[k+1][e]

        t=ans1 + ans2 + a[s-1]*a[k]*a[e]
        ans = min(ans,t)
    return ans


if __name__=='__main__':
    n=int(input())
    a=list(map(int, input().split()))
    dp = [[-1 for j in range(n+1)] for i in range(n+1)]
    print(MCM(a, 1, n, dp))
    