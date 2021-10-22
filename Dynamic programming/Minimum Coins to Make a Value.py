# Code by : Sam._.072

import sys

# ------RECURSIVE APPROACH------

def minCoins_R(coins,val):
    if val==0:
        return 0
    res = sys.maxsize
    for i in coins:
        if i <= val:
            sub_res = minCoins_R(coins, val-i)
            if sub_res!=sys.maxsize:
                res= min(sub_res+1, res)
    return res

# ------ITERATIVE APPROACH------
# Time Complexity : O(val*(size(coins)))
# Space Complexity : O(val)

def minCoins(coins,val):
    dp = [sys.maxsize for i in range(val+1)]
    dp[0] = 0
    for i in range(1,val+1):
        for j in coins:
            if j <= i:
                sub_res = dp[i-j]
                if sub_res != sys.maxsize:
                    dp[i] = min(dp[i], sub_res+1)

    return dp[val]

if __name__=='__main__':
    val=int(input())
    coins=list(map(int, input().split()))
    print(minCoins(coins, val))