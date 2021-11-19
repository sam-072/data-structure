# Code by : Sam._.072

def perSpace(index, s, ans):
    if index >= len(s):
        # ans.append(s)
        return
    for i in range(index+1,len(s)):
        s = s[:i]+" "+s[i:]
        ans.append(s)
        perSpace(i+1,s, ans)
        s = s[:i]+s[i+1:]

if __name__ == '__main__':        
    s=input()
    ans = []
    perSpace(0, s, ans)
    ans.append(s)
    ans.sort()
    print(ans)