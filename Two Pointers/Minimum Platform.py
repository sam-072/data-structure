# Code by : Sam._.072

# Time Complexity : O(NlogN)
# Space Complexity : O(1)

def minPlatform(arr, dep):
    arr.sort()
    dep.sort()
    i, j = 0, 0
    h, p = 0, 0
    while i < len(arr):
        if arr[i] <= dep[j]:
            p += 1
            if p > h:
                h = p
            i += 1
        else:
            p -= 1
            j += 1
    return h


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    dep = list(map(int, input().split()))
    print(minPlatform(arr, dep))