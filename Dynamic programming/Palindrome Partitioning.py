# Code by : Sam._.072

# Given a string str, a partitioning of the string is a palindrome partitioning if
# every sub-string of the partition is a palindrome. Determine the fewest cuts
# needed for palindrome partitioning of given string.

import sys

def isPalindrome(s):
    return s == s[::-1]

#------RECURSIVE APPROACH------

def palPartition(s, i, j):
    if isPalindrome(s[i:j+1]) or i >= j:
        return 0
    res = sys.maxsize
    for k in range(i, j):
        res = min(res, 1+palPartition(s, i, k)+palPartition(s, k+1, j))
    return res

# ------ITERATIVE APPROACH------

def palPart(s):
    n=len(s)
    dp = [[sys.maxsize for i in range(n)] for j in range(n)]
    isPal = [[False for i in range(n)] for j in range(n)]
    for i in range(n):
        dp[i][i] = 0
        isPal[i][i] = True
    for gap in range(1,n):
        for i in range(0,n):
            j = i + gap
            if s[i]==s[j] and (isPal[i+1][j-1] or gap==1):
                dp[i][j] = 0
                isPal[i][j] = True
            else:
                isPal[i][j] = False
                for k in range(i,j):
                    dp[i][j] = min(dp[i][j], 1+dp[i][k]+dp[k+1][j])
    return dp[0][n-1]


if __name__=='__main__':
    s=input()
    print(palPartition(s, 0, len(s)-1))
    print(palPart(s))


