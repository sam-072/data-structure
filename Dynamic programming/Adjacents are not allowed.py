# Code by : Sam._.072

def AdjMax(a,n):
    if n == 1:
        return max(a[0][0], a[1][0])
    if n == 2:
        return max(a[0][0],a[0][1],a[1][0],a[1][1])
    dp = [0 for i in range(n+1)]
    dp[1] = max(a[0][0], a[1][0])
    dp[2] = max(a[0][0],a[0][1],a[1][0],a[1][1])
    for i in range(3,n+1):
        dp[i] = max(dp[i-1], max(a[0][i-1],a[1][i-1])+dp[i-2])
    return dp[n]

    

if __name__ == '__main__':
    n = int(input())
    a = []
    a.append(list(map(int,input().split())))
    a.append(list(map(int,input().split())))
    print(AdjMax(a, n))

