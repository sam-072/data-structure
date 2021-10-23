# Code by : Sam._.072

# You are given an array A of size N. The array contains integers and is of even length.
# The elements of the array represent N coin of values V1, V2, ....Vn. You play against
# an opponent in an alternating way.
# In each turn, a player selects either the first or last coin from the row, removes it 
# from the row permanently, and receives the value of the coin.
# You need to determine the maximum possible amount of money you can win if you go first.

# ------RECURSIVE APPROACH------

def maxValue_R(arr, i, j):
    if i+1 == j:
        return max(arr[i], arr[j])
    
    return max(arr[i]+min(maxValue_R(arr, i+2, j),maxValue_R(arr, i+1, j-1)), arr[j]+min(maxValue_R(arr, i+1, j-1),maxValue_R(arr, i, j-2)))

# ------ITERATIVE APPROACH------
# Time Complexity : O(N*N)
# Space Complexity : O(N*N)

def maxValue(arr):
    n=len(arr)
    dp = [[0 for i in range(n)] for j in range(n)]
    for i in range(n-1):
        dp[i][i+1] = max(arr[i], arr[i+1])
    for gap in range(3,n,2):
        i=0
        while i+gap < n:
            j = i+gap
            dp[i][j] = max(arr[i] + min(dp[i+2][j], dp[i+1][j-1]), arr[j] + min(dp[i+1][j-1], dp[i][j-2]) )
            i += 1
    return dp[0][n-1]


if __name__=='__main__':
    arr = list(map(int, input().split()))
    print(maxValue_R(arr, 0, len(arr)-1))
    print(maxValue(arr))

