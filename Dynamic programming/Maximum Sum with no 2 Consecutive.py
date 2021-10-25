# Code by : Sam._.072

# ------RECURSIVE APPROACH------
# Time Complexity : O(2^N)

def maxSum_R(arr, n):
    if n == 1:
        return arr[0]
    elif n == 2:
        return max(arr[0], arr[1])
    return max(maxSum_R(arr,n-1), maxSum_R(arr,n-2)+arr[n-1])

# -------ITERATIVE APPROACH-------
# Time Complexity : O(N)
#  Space Complexity : O(N)

def maxSum(arr):
    n=len(arr)
    dp = [0 for i in range(n+1)]
    dp[1] = arr[0]
    dp[2] = max(arr[0], arr[1])
    for i in range(3,n+1):
        dp[i] = max(dp[i-1], dp[i-2]+arr[i-1])
    return dp[n]

# Time Complexity : O(N)
# Space Complexity : O(1)

def maxSum1(arr):
    n=len(arr)
    prev_prev = arr[0]
    prev = max(arr[0], arr[1])
    for i in range(3,n+1):
        temp = max(prev, arr[i-1]+prev_prev)
        prev_prev = prev
        prev = temp
    return prev

if __name__=='__main__':
    n=int(input())
    arr=list(map(int, input().split()))
    print(maxSum_R(arr, n))
    print(maxSum(arr))
    print(maxSum1(arr))