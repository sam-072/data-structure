# Code by : Sam._.072

# -----RECURSIVE APPROACH-----
# Time Complexity : O(N*M)
# Space Complexity : O(N*M) for dp matrix and O(N*M) for stack

def LCS_R(i, j, s1, s2, dp):
    c=0
    if i >= len(s1) or j >= len(s2):
        return 0

    if s1[i] == s2[j]:
        if dp[i+1][j+1]==-1:
            c1 = LCS_R(i+1, j+1, s1, s2, dp)
            dp[i+1][j+1] = c
        else:
            c1 = dp[i+1][j+1]
        c = c1 + 1
    else:
        if dp[i+1][j] == -1:
            c1 = LCS_R(i+1, j, s1, s2, dp)
            dp[i+1][j] = c1
        else:
            c1 = dp[i+1][j]
        if dp[i][j+1] == -1:
            c2 = LCS_R(i, j+1, s1, s2, dp)
            dp[i][j+1] = c2
        else:
            c2 = dp[i][j+1]

        c = max(c1, c2)

    return c

# -----ITERATIVE APPROACH-----
# Time Complexity : O(N*M)
# Space Complexity : O(N*M) for dp matrix

def LCS(s1, s2):
    dp = [ [0 for j in range(len(s2)+1)] for i in range(len(s1)+1)]
    for i in range(len(s1)-1,-1,-1):
        for j in range(len(s2)-1,-1,-1):
            if s1[i] == s2[j]:
                dp[i][j] = dp[i+1][j+1] + 1
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j+1])
    return dp[0][0]

if __name__=='__main__':
    s1=input()
    s2=input()
    dp = [ [-1 for i in range(len(s2)+1)] for j in range(len(s1)+1)]
    print(LCS_R(0, 0, s1, s2, dp))
    print(LCS(s1, s2))