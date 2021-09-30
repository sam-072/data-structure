# time complexity : O(n)
# space complexity : O(n)

import sys
def minStep(n,dp):
    k=1
    for i in range(2,n+1):
        ans1,ans2,ans3=sys.maxsize,sys.maxsize,sys.maxsize
        if i%3==0:
            ans1=dp[i//3]+1
        if i%2==0:
            ans2=dp[i//2]+1
        ans3=dp[i-1]+1

        dp[i]=min(ans1,ans2, ans3)

    return dp[n]
                

if __name__=='__main__':
    n=int(input())
    dp=[0 for i in range(n+1)]
    print(minStep(n, dp))