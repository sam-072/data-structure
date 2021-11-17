# Code by : Sam._.072

def pal_part(index, s, ds, ans):
    if index >= len(s):
        ans.append(ds[:])
        return
    for i in range(index,len(s)):
        temp = s[index:i+1]
        if temp == temp[::-1]:
            ds.append(temp)
            pal_part(i+1,s, ds, ans)
            ds.pop()

if __name__ == '__main__':
    s = input()
    ds, ans = [], []
    pal_part(0, s, ds, ans)
    print(ans)