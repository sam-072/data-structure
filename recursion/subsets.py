# Code by : Sam._.072

def subsets(a):
    if len(a)==0:
        return [[]]
    l = subsets(a[1:])
    ans = []
    ans.extend(l)
    for i in l:
        t = i[:]
        t.append(a[0])
        ans.append(t)
    return ans

print(subsets([2,4]))