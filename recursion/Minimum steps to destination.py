# Code by : Sam._.072
import sys
def dest(x, i, y, dp):
    if x==y:
        return 0
    elif abs(x)>y:
        return sys.maxsize
    else:
        if dp[x+i]==-1:
            ans1 = dest(x+i, i+1, y, dp)
            dp[x+i] = ans1
        else:
            ans1 = dp[x+i]
        if dp[x-i]==-1:
            ans2 = dest(x-i, i+1, y, dp)
            dp[x-i] = ans2
        else:
            ans2 = dp[x-i]
        dp[x] = 1 + min(ans1, ans2)

y=int(input())
dp= [-1 for i in range(2*10000+1)]
dest(0, 1, y, dp)
print(dp)