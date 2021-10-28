# Code by : Sam._.072

# Given two strings X and Y, and two values costX and costY, the task is to
# find the minimum cost required to make the given two strings identical.
# You can delete characters from both the strings. The cost of deleting a 
# character from string X is costX and from Y is costY. The cost of removing 
# all characters from a string is the same

def minCost(s1,s2,x,y):
    n=len(s1)
    m=len(s2)
    dp = [[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[j-1]==s2[i-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return x*(n-dp[m][n]) + y*(m-dp[m][n])

if __name__=='__main__':
    s1=input()
    s2=input()
    x,y=map(int, input().split())
    print(minCost(s1, s2, x, y))
