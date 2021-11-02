# Code by : Sam._.072

def heightBook(a,n,k):
    dp = [0 for i in range(n+1)]
    for i in range(1,n):
        if a[i-1]<=k:
            dp[i] = dp[i-1] + a[i-1]
    return max(dp)


if __name__ == '__main__':
    for _ in range(int(input())):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        print(heightBook(a, n, k))