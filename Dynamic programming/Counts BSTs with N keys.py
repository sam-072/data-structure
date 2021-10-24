# Code by : Sam._.072

# Given an integer. Find how many structurally unique binary search trees are ther
# that stores the values from 1 to that integer (inclusive). 

# ------RECURSIVE APPROACH------
# Time Complexity : O(N*N)
# Space Complexity : O(N)

def countsBSTs(n):
    dp = [ 0 for i in range(n+1)]
    dp[0] = 1
    for i in range(1,n+1):
        for j in range(i):
            dp[i] += dp[j]*dp[i-j-1]
    return dp[n]

if __name__=='__main__':
    n=int(input())
    print(countsBSTs(n))