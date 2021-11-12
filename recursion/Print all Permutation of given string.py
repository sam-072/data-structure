# Code by : Sam._.072

def permutation(s, d, ans, res):
    if len(ans) == len(s):
        res.append(''.join(ans))
        # return
    for i in range(len(s)):
        if d[i] is False:
            ans.append(s[i])
            d[i] = True
            permutation(s, d, ans, res)
            ans.pop()
            d[i] = False

if __name__ == '__main__':
    s=input()
    d = dict()
    for i in range(len(s)):
        d[i] = False
    ans = []
    res = list()
    permutation(s, d, ans, res)
    print(res)