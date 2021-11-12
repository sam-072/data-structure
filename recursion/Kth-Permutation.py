# Code by : Sam._.072

# Time Complexity : O(N*N)
# Space Complexity : O(N)

import math
def KthPermutation(n, a, k, ans):
    if n == 1:
        ans.append(a[0])
        return
    x = math.factorial(n-1) 
    ans.append(a[k//x])
    a.remove(a[k//x])
    KthPermutation(n-1, a, k%x, ans)

if __name__ == '__main__':
    n = int(input())
    a = list(map(int,input().split()))
    k = int(input())
    ans = []
    KthPermutation(n, a, k-1, ans)
    print(ans)
