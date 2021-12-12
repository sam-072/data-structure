# Code by : Sam._.072

# Time Complexity : O(N)
# Space Complexity : O(2N)
# Using Prefix and Suffix sum array

def RainWater(arr):
    n = len(arr)
    prefix = [0 for i in range(n)]
    prefix[0] = arr[0]
    for i in range(1,n):
        prefix[i] = prefix[i-1] if prefix[i-1] > arr[i] else arr[i]
    suffix = [0 for i in range(n)]
    suffix[-1] = arr[-1]
    for i in range(n-2,-1,-1):
        suffix[i] = arr[i] if arr[i] > suffix[i+1] else suffix[i+1]
    c = 0
    for i in range(n):
        c += min(prefix[i], suffix[i]) - arr[i]
    return c

# Time Complexity : O(N)
# Space Complexity : O(1)
# Using Two Pointer Method

def TrappingRainwater(arr):
    i, j = 0, len(arr)-1
    leftMax, rightMax = 0, 0
    c = 0
    while i < j:
        if arr[i] <= arr[j]:
            if leftMax < arr[i]:
                leftMax = arr[i]
            else:
                c += leftMax - arr[i]
            i += 1
        else:
            if rightMax < arr[j]:
                rightMax = arr[j]
            else:
                c += rightMax - arr[j]
            j -= 1
    return c


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    print(RainWater(arr))
    print(TrappingRainwater(arr))