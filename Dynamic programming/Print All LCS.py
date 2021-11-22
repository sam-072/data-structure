# Code by : Sam._.072

def LCS(i, j, s, t):
    ans = ''
    if len(s)==0 or len(t)==0:
        return ''
    if s[i] == t[j]:
        ans += LCS(i+1, j+1, s, t)
    ans1 = LCS(i+1, j, s, t)
    ans2 = LCS(i, j+1, s, t)
    if len(ans1)>=len(ans2):
        return ans1
    return ans2


if __name__ == '__main__':
    s = input()
    t = input()
    print(LCS(0, 0, s, t))
