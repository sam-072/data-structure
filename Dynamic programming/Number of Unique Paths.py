# Code by : Sam._.072

# Given a A X B matrix with your initial position at the top-left cell, 
# find the number of possible unique paths to reach the bottom-right cell 
# of the matrix from the initial position.

# Note: Possible moves can be either down or right at any point in time, 
# i.e., we can move to matrix[i+1][j] or matrix[i][j+1] from matrix[i][j]

def no_path(n, m):
    dp = [[0 for j in range(m)] for i in range(n)]
    for i in range(m):
        dp[n-1][i] = 1
    for i in range(n):
        dp[i][m-1] = 1
    for i in range(n-2,-1,-1):
        for j in range(m-2,-1,-1):
            dp[i][j] = dp[i+1][j] + dp[i][j+1]

    return dp[0][0]

if __name__=='__main__':
    n,m=map(int, input().split())
    print(no_path(n, m))
