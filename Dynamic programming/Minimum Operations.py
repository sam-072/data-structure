# Code by : Sam._.072

# Given a number N. Find the minimum number of operations required to reach N
# starting from 0. You have 2 operations available:
# Double the number
# Add one to the number

def MinOperation(n):
    dp=[0 for i in range(n+1)]
    for i in range(1,n+1):
        if i%2==0:
            dp[i]=1+min(dp[i-1], dp[i//2])
        else:
            dp[i]=1+dp[i-1]
    return dp[n]

if __name__=='__main__':
    n=int(input())
    print(MinOperation(n))