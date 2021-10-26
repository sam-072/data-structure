# Code by : Sam._.072

# You are given N number of books. Every ith book has Ai number of pages.
# You have to allocate contagious books to M number of students. There can be many
# ways or permutations to do so. In each permutation, one of the M students will be
# allocated the maximum number of pages. Out of all these permutations, the task 
# is to find that particular permutation in which the maximum number of pages 
# allocated to a student is minimum of those in all the other permutations and 
# print this minimum value.

# Each book will be allocated to exactly one student. Each student has to be allocated 
# at least one book. Note: Return -1 if a valid assignment is not possible, and 
# allotment should be in contiguous order (see the explanation for better understanding).

import sys

# ------RECURSIVE APPROACH------

def minPages_R(arr, n, k):
    if k == 1:
        return sum(arr)
    elif n == 1:
        return arr[0]
    res = sys.maxsize
    for i in range(1,n):
        res = min(res, max(minPages_R(arr, i, k-1), sum(arr[1:n])))
    return res

# ------ITERATIVE APPROACH------

def minPages(arr, k):
    n = len(arr)
    dp = [[0 for i in range(n+1)] for j in range(k+1)]
    for i in range(1, k+1):
        dp[i][1] = arr[0]
    for i in range(2, n+1):
        dp[1][i] = dp[1][i-1] + arr[i-1]
    for i in range(2, k+1):
        for j in range(2, n+1):
            res = sys.maxsize
            for p in range(1, j):
                res = min(res, max(dp[i-1][p], sum(arr[p:j])))
        dp[i][j] = res
    return dp[k][n]


if __name__=='__main__':
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(minPages_R(arr, n, k))
    print(minPages(arr, k))
    
