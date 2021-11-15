# Code by : Sam._.072

def uniquePerms(a, n):
    # code here 
    ans = []
    permutation1(0, a, ans)
    new_data = [list(y) for y in set([tuple(x) for x in ans])]
    # print(ans)
    return new_data
        
def permutation1(index, a, ans):
    if index == len(a):
        t = a[:]
        ans.append(t)
        return
    for i in range(index,len(a)):
        a[i], a[index] = a[index], a[i]
        permutation1(index+1, a, ans)
        a[i], a[index] = a[index], a[i]

a = [2 ,1, 2, 3, 4, 5]
print(uniquePerms(a, 6))