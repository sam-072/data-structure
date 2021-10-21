# Code by : Sam._.072

# ------RECURSIVE APPROACH------

def distance_R(s1,s2,n,m):
    if n==0:
        return m
    if m==0:
        return n
    
    if s1[n-1]==s2[m-1]:
        return distance_R(s1, s2, n-1, m-1)
    
    return 1 + min(distance_R(s1, s2, n, m-1), distance_R(s1, s2, n-1, m),distance_R(s1, s2, n-1, m-1))

# ------ITERATIVE APPROACH------

def distance(s1,s2):
    n=len(s1)
    m=len(s2)
    dp = [ [0 for i in range(n+1)] for j in range(m+1)]
    for i in range(n+1):
        dp[0][i]=i
    for j in range(m+1):
        dp[j][0] = j
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[j-1]==s2[i-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])
    return dp[m][n]

if __name__=='__main__':
    s1=input()
    s2=input()
    print(distance(s1, s2))