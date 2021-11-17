# Code by : Sam._.072

# Time Complexity : 2^N

def subsets(index, a, ds, ans):
    ans.append(ds[:])
    for i in range(index,len(a)):
        if i > index and a[i] == a[i-1]:
            continue
        ds.append(a[i])
        subsets(i+1, a, ds, ans)
        ds.pop()


if __name__ == '__main__':
    a = list(map(int, input().split()))
    ds, ans = [], []
    a.sort()
    subsets(0, a, ds, ans)
    print(ans)
