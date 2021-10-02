import sys,math

# ------RECURSIVE APPROACH-------
# Time Complexity : O(n Root(n))
# Space complexity : O(n) for stack and O(n) for dp Array
# problem : stack overflow or maximum recursion depth exceeded in comparison


def minNO(n,dp):
    if n==0:
        return 0    
    i=1
    ans=sys.maxsize
    while i*i<=n:
        if dp[n-i*i]==-1:
            currans=1+minNO(n-i*i,dp)
            dp[n-i*i]=currans
        else:
            currans=dp[n-i*i]
        i+=1
        ans=min(ans,currans)
    return ans


# ------ITERATIVE APPROACH-------
# Time comlpexity : O(n Root(n))
# Space complexity : O(n) only for dp array

def MinNoSquare(n):
    dp=[-1 for i in range(n+1)]
    dp[0]=0

    for i in range(1,n+1):
        ans=sys.maxsize
        root=int(math.sqrt(i))
        for j in range(1,root+1):
            currans=1+dp[i-(j**2)]
            ans=min(ans, currans)
        dp[i]=ans
    return dp[n]


n=int(input())
dp=[-1 for i in range(n+1)]

print(MinNoSquare(n))
# print(minNO(n,dp))

