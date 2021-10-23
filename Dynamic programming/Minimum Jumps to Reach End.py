# Code by : Sam._.072

# Given an array of N integers arr[] where each element represents the max number
# of steps that can be made forward from that element. Find the minimum number of
#  jumps to reach the end of the array (starting from the first element). If an 
# element is 0, then you cannot move through that element.
# Note: Return -1 if you can't reach the end of the array.

import sys

# ------RECURSIVE APPROACH------

def minJumps_R(arr,n):
    if n<=1:
        return 0
    res = sys.maxsize
    for i in range(n-1):
        if i + arr[i] >= n-1:
            sub_res = minJumps_R(arr, i+1)
            if sub_res != sys.maxsize:
                res = min(res, sub_res+1) 
    return res

# ------ITERATIVE APPROACH------
# Time Complexity : O(N^2)
# Space Complexity : O(N)

def minJumps(arr):
    n = len(arr)
    dp = [sys.maxsize for i in range(n)]
    dp[0] = 0
    for i in range(1,n):
        for j in range(0,i):
            if arr[j] + j >= i:
                if dp[j] != sys.maxsize:
                    dp[i] = min(dp[j]+1, dp[i])
                    
    if dp[n-1]==sys.maxsize:
        return -1
    return dp[n-1]  

if __name__=='__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(minJumps_R(arr, n))
    print(minJumps(arr))