# Code by : Sam._.072

# Polycarpus has a ribbon, its length is n. He wants to cut the ribbon in a way that fulfils the following two conditions:
# After the cutting each ribbon piece should have length a, b or c.
# After the cutting the number of ribbon pieces should be maximum.
# Help Polycarpus and find the number of ribbon pieces after the required cutting.

# ------RECURSIVE APPROACH------
# Time complexity : 3^n

def maxCuts_R(n,a,b,c):
    if n<0:
        return -1
    if n==0:
        return 0
    res = max(maxCuts_R(n-a, a, b, c),maxCuts_R(n-b, a, b, c), maxCuts_R(n-c, a, b, c))
    if res==-1:
        return res
    else:
        return res+1


# ------ITERATIVE APPROACH------
# Time Complexity : O(N)
# space Complexity : O(N)

def maxCuts(n,a,b,c):
    dp= [0 for i in range(n+1)]
    for i in range(1,n+1):
        dp[i] =-1
        if i-a>=0:
            dp[i]=max(dp[i], dp[i-a])
        if i-b>=0:
            dp[i]=max(dp[i], dp[i-b])
        if i-c>=0:
            dp[i]=max(dp[i], dp[i-c])
        if dp[i]!=-1:
            dp[i]+=1
    return dp[n]

if __name__=='__main__':
    n,a,b,c=map(int, input().split())
    print(maxCuts(n, a, b, c))