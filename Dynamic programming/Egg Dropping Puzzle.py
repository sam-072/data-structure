# Code by : Sam._.072

# You are given E identical eggs and you have access to a F-floored building from 1 to F.
# There exists a floor f where 0 <= f <= F such that any egg dropped at a floor higher than f will break, and any egg dropped at or below floor f will not break.
# There are few rules given below. 
# An egg that survives a fall can be used again.
# A broken egg must be discarded.
# The effect of a fall is the same for all eggs.
# If the egg doesn't break at a certain floor, it will not break at any floor below.
# If the eggs breaks at a certain floor, it will break at any floor above.
# Return the minimum number of moves that you need to determine with certainty what the value of f is.

import sys

# ------RECURSIVE APPROACH------

def Result_R(f, e):
    if e == 1:
        return f
    if f == 1:
        return 1
    if f == 0:
        return 0
    ans = sys.maxsize
    for x in range(1,f+1):
        sub_ans = max(Result_R(x-1, e-1), Result_R(f-x, e))
        if sub_ans != sys.maxsize:
            ans = min(sub_ans+1, ans)
    return ans

# -------ITERATIVE APPROACH-------
# Time Complexity : O(F*F*E)
# Space Complexity : O(F*E)

def Result(f, e):
    dp = [[0 for j in range(e+1)] for i in range(f+1)]
    for i in range(1,e+1):
        dp[1][i] = 1
    for i in range(2,f+1):
        dp[i][1] = i
    for i in range(2,f+1):
        for j in range(2,e+1):
            dp[i][j] = sys.maxsize
            for x in range(1,i+1):
                dp[i][j] = min(dp[i][j],1 + max(dp[x-1][j-1], dp[i-x][j]))
    return dp[f][e]


if __name__=='__main__':
    f,e = map(int, input().split())
    print(Result(f, e))
