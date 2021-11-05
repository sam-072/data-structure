# Code by : Sam._.072

# A frog jumps either 1, 2, or 3 steps to go to the top. In how many ways can it reach the top.
# As the answer will be large find the answer modulo 1000000007

def CountHops(n):
    dp = [0 for i in range(n+1)]
    if n==1:
        return 1
    dp[0], dp[1], dp[2] = 1, 1, 2
    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    return dp[n]

if __name__ == '__main__':
    n = int(input())
    print(CountHops(n))