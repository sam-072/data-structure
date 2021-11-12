# Code by : Sam._.072

# Time Complexity : O(N! * N)
# Space Complexity : O(N) for map + O(N) for data structure

def permutation(s, d, ans, res):
    if len(ans) == len(s):
        res.append(''.join(ans))
        return
    for i in range(len(s)):
        if d[i] is False:
            ans.append(s[i])
            d[i] = True
            permutation(s, d, ans, res)
            ans.pop()
            d[i] = False

## Time Complexity : O(N! * N)
# Space Complexity : O(1)

def permutation1(index, a):
    if index == len(a):
        print(a)
        return
    for i in range(index,len(a)):
        a[i], a[index] = a[index], a[i]
        permutation1(index+1, a)
        a[i], a[index] = a[index], a[i]


if __name__ == '__main__':
    # s=input()
    a = list(map(int, input().split()))
    d = dict()
    # for i in range(len(s)):
        # d[i] = False
    ans = []
    res = list()
    # permutation(s, d, ans, res)
    # print(res)
    permutation1(0, a)