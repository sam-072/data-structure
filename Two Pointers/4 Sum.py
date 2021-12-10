# Code by : Sam._.072

# Time Complexity : O(N^3 * log(N))
# Space Complexity : O()

def QuadSum(arr):
    arr.sort()
    n = len(arr)
    c = 0
    for i in range(n-3):
        for j in range(i+1,n-2):
            for k in range(j+1,n-1):
                x = 0 - arr[i] - arr[j] - arr[k]
                if BinarySearch(k+1, n, arr, x):
                    c += 1
    return c

def BinarySearch(i, j, arr, x):
    while i < j:
        mid = i + (j-i)//2
        if arr[mid] == x:
            return True
        elif arr[mid] > x:
            j = mid -1
        else:
            i = mid + 1
    return False

# Time Complexity : O(N^3)
# Space Complexity : O(1)

def QuadSum1(arr,x):
    n = len(arr)
    arr.sort()
    ans = []
    for i in range(n-3):
        if i == 0 or (i>0 and arr[i] != arr[i-1]):
            for j in range(i+1,n-2):
                if j == i+1 or (j > i+1 and arr[j] != arr[j-1]):
                    l , r = j+1, n-1
                    t = x - arr[i] - arr[j]
                    while l < r:
                        if arr[l] + arr[r] == t:
                            ans.append([arr[i], arr[j], arr[l], arr[r]])
                            l += 1
                            while l < r and arr[l] == arr[l-1]:
                                l += 1
                            r -= 1
                            while l < r and arr[r] == arr[r+1]:
                                r -= 1
                        elif arr[l] + arr[r] < t:
                            l += 1
                        else:
                            r -= 1
    return ans


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    x = int(input())
    print(QuadSum1(arr, x))
