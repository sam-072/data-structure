# Code by : Sam._.072

# ------RECURSIVE SOLUTION------

def getCoins_R(coins,n,s):
    if s==0:
        return 1
    if n==0:
        return 0
    res=getCoins_R(coins, n-1, s)
    if coins[n-1]<=s:
        res = res + getCoins_R(coins, n, s-coins[n-1])
    return res

# ------ITERATIVE SOLUTION------

def getCoins(coins,s):
    n=len(coins)
    dp = [[0 for j in range(n)] for i in range(s+1)]
    for i in range(n):
        dp[0][i] = 1
    for i in range(1,s+1):
        for j in range(n):
            dp[i][j] = dp[i][j-1]
            if coins[j-1]<=i:
                dp[i][j] += dp[i-coins[j-1]][j]
    return dp[s][n-1]


if __name__=='__main__':
    n,s=map(int, input().split())
    coins=list(map(int, input().split()))
    print(getCoins_R(coins, n, s))
    print(getCoins(coins, s))