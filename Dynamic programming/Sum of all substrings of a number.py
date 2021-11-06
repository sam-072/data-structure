# Code by : Sam._.072

# dp[i] = (i+1)*s[i] + 10(dp[i-1])
# and take a extra sum varibale and sum at each steps

def substringSum(s):
    n = len(s)
    a = [int(i) for i in s]
    dp = [0 for i in range(n)]
    dp[0] = a[0]
    c = dp[0]
    for i in range(1,n):
        dp[i] = (i+1)*a[i] + 10*dp[i-1]
        c += dp[i]%1000000007
        
    print(dp)
    return c%10000000007 
        
print(substringSum('9384'))
# print(plus('123', 2))
