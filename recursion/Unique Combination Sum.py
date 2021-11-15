# Code by : Sam._.072

def CombSum(index, a, t, ds, ans):
    if t == 0:
        ans.append(ds[::])
        return 
    for i in range(index,len(a)):
        if i>index and a[i] == a[i-1]:
            continue
        if a[i] > t:
            break
        ds.append(a[i])
        CombSum(i+1, a, t-a[i], ds, ans)
        ds.pop()

if __name__ == '__main__':
    a = [1,1,1,2,2]
    t = 4
    ds, ans = [], []
    CombSum(0, a, t, ds, ans)
    print(ans)
