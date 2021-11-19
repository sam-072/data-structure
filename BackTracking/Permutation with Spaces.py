# Code by : Sam._.072

def perSpace(index, s, ds, ans):
    if index >= len(s):
        ans.append(ds[:])
        return
    for i in range(index+1,len(s)):
        temp = s[:i]+" "+s[i:]
        ds.append(temp)
        perSpace(i+1,s, ds, ans)
        

ds = []
ans = []
perSpace(0, "ABC", ds, ans)
print(ans)