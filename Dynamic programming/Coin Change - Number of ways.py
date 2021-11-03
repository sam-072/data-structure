# Code by : Sam._.072

# You have an infinite supply of coins, each having some value.
# Find out the number of ways to use the coins to sum-up to a certain required value.

def noOfWay(coins, n, val):
    dp = [[0 for i in range(n+1)]for j in range(val+1)]
    for i in range(n):
        dp[0][i] = 1
    for i in range(1,val+1):
        for j in range(n+1):
            dp[i][j] = dp[i][j-1]
            if coins[j-1]<=i:
                dp[i][j] += dp[i-coins[j-1]][j]
    return dp[val][n-1]

if __name__ == '__main__':
    # n, val = map(int, input().split())
    # coins = list(map(int, input().split()))
    for i in range(0,16):
        print(noOfWay([1,2,3], 3, i))