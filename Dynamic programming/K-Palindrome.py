# Code by : Sam._.072

def K_pali(s,i,j):
    if i==j:
        return 0
    if i+1==j:
        if s[i]==s[j]:
            return 0
        return 1
    if s[i]==s[j]:
        return K_pali(s, i+1, j-1)
    return 1 + min(K_pali(s, i+1, j), K_pali(s, i, j-1))

def Kpali(s,k):
    n=len(s)
    s1 = s[::-1]
    dp = [[0 for i in range(n+1)]for j in range(n+1)]
    for i in range(n+1):
        for j in range(n+1):
            if i==0:
                dp[i][j] = j
            elif j==0:
                dp[i][j] = i
            elif s[i-1]==s1[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1]) 
    if dp[n][n]<=2*k:
        return 1
    return 0

if __name__ == '__main__':
    k=int(input())
    s=input()
    print(K_pali(s, 0, len(s)-1))
    print(Kpali(s, k))
