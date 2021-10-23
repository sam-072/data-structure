# Code by : Sam._.072

# A thief robbing a store can carry a maximal weight of W into his knapsack.
# There are N items, and i-th item weigh 'Wi' and the value being 'Vi.' 
# What would be the maximum value V, that the thief can steal?


# -----RECURSIVE APPROACH------

def Knapsack_R(W, wt, vl, i):

    if i==len(wt):
        return 0
    if wt[i]<=W:
        # includeing the current weight
        ans1 = vl[i] + Knapsack_R(W-vl[i], wt, vl, i+1)

        #exculding the current weight
        ans2 = Knapsack_R(W, wt, vl, i+1)

        ans = max(ans1, ans2)
    else:
        ans = Knapsack_R(W, wt, vl, i+1)

    return ans

# ------ITERATIVE APPROACH-----
# Time Complexity : O(W*N)
# Space Complexity : O(W*N)

def Knapsack(W, wt, vl):
    n = len(wt)
    dp = [[0 for w in range(W+1)] for i in range(n+1)]
    for i in range(n-1,-1,-1):
        for j in range(W+1):
            if wt[i] <= j:
                ans1 = dp[i+1][j]
                ans2 = vl[i] + dp[i+1][j-wt[i]]
                ans = max(ans1, ans2)
            else:
                ans = dp[i+1][j]
            dp[i][j] = ans
    return dp[0][W]


if __name__=='__main__':
    wt = list(map(int, input().split()))
    vl = list(map(int, input().split()))
    W = int(input())
    print(Knapsack(W, wt, vl))