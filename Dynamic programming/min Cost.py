import sys

# ------RECURSIVE APPROACH------
# T.c = O(n*m)
# S.c = O(n*m) for stack and O(n*m) for dp matrix

def minCost_R(i,j,n,m,cost,dp):

    if i==n-1 and j==m-1:
        return cost[i][j]
    if i>=n or j>=m:
        return sys.maxsize

    if dp[i+1][j]==0:
        ans1 = minCost_R(i+1, j, n, m, cost, dp)
        dp[i+1][j] =  ans1
    else:
        ans1 = dp[i+1][j]

    if dp[i][j+1]==0:
        ans2 = minCost_R(i, j+1, n, m, cost, dp) 
        dp[i][j+1] = ans2
    else:
        ans2 = dp[i][j+1]
    
    if dp[i+1][j+1] == 0:
        ans3 = minCost_R(i+1, j+1, n, m, cost, dp)
        dp[i+1][j+1] = ans3
    else:
        ans3 = dp[i+1][j+1]
    
    return cost[i][j] + min(ans1, ans2, ans3)

# ------ITREATIVE APPROACH------
# T.c = O(n*m)
# S.c = O(n*m) only for dp matrix 

def minCost(n,m,cost):
    dp=[[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(n):
        dp[i][m]=sys.maxsize
    for j in range(m):
        dp[n][j]=sys.maxsize
    for i in range(n-1,-1,-1):
        for j in range(m-1,-1,-1):
            if i==n-1 and j==m-1:
                dp[i][j]=cost[i][j]
            else:
                dp[i][j] = cost[i][j]+min(dp[i+1][j],dp[i][j+1],dp[i+1][j+1])
    return dp[0][0]


if __name__=='__main__':

    n,m=map(int, input().split())
    cost=[]
    dp=[[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(n):
        cost.append(list(map(int,input().split())))
    print(minCost_R(0, 0, n, m, cost, dp))
    print(minCost(n, m, cost))