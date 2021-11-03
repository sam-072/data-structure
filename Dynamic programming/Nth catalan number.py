# Code by : Sam._.072

def catalanNo(n):
    dp = [0 for i in range(n+1)]
    dp[0] = 1
    for i in range(1,n+1):
        for j in range(i):
            dp[i] += dp[j]*dp[i-1-j]
    return dp[n]

if __name__ == '__main__':
    n = int(input())
    print(catalanNo(n))