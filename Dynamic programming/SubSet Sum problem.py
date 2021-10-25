# Code by : Sam._.072

# Given an array of non-negative integers, and a value sum, determine if there is 
# a subset of the given set with sum equal to given sum

# ------RECURSIVE APPROACH------
# Time Complexity : O(2^N)

def countSubset_R(arr,n,s):
    if n==0:
        if s==0:
            return 1
        else:
            return 0
    return countSubset_R(arr, n-1, s) + countSubset_R(arr, n-1, s-arr[n-1])

# ------ITERATIVE APPROACH------
# Time Complexity : O(N*SUM)
# Space Complexity : O(N*SUM)

def countSubsets(arr,s):
    n = len(arr)
    dp = [[0 for i in range(s+1)] for j in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1
    for i in range(1,n+1):
        for j in range(1,s+1):
            if j < arr[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-arr[i-1]]
    return dp[n][s]


if __name__=='__main__':
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))
    print(countSubset_R(arr, n, s))
    print(countSubsets(arr, s))
