# Code by : Sam._.072

# Time Complexity : O(N logN)
# Space Complexity : O(N)
# Using set approach

def removeDuplicate(a):
    s = set()
    for i in a:
        s.add(i)
    j = 0
    for i in s:
        a[j] = i
        j += 1
    return len(s)

# Time Complexity : O(N)
# Space Complexity : O(1)
# Two Pointer Approach

def removeDup(a):
    i = 0
    for j in range(1,len(a)):
        if a[i] != a[j]:
            i += 1
            a[i] = a[j]
    return i + 1

if __name__ == '__main__':
    a = list(map(int, input().split()))
    print(removeDuplicate(a))
    print(removeDup(a))

