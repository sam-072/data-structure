# this fibonacci series program is done using dynamic programming 
# time complexity : O(n)
# space complexity : O(n) for stack and O(n) for dp = O(n)

def fibo(n,dp):
    if n==0 or n==1:
        return n
    
    if dp[n-1] == -1:
        ans1 = fibo(n-1, dp)
        dp[n-1] = ans1
    else:
        ans1 = dp[n-1]
    
    if dp[n-2] == -1:
        ans2 = fibo(n-2, dp)
        dp[n-2] = ans2
    else:
        ans2 = dp[n-2]
    
    return ans1 + ans2

if __name__=='__main__':
    n=int(input())
    dp = [ -1 for i in range(n+1)]
    print(fibo(n, dp))

