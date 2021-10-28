# Code by : Sam._.072

def StringSub(s1, s2, k):
    if k>=len(s2):
        return 0
    res = 0
    for i in range(k,len(s2)):
        if s2[k] == s1[i]:
            res = res + StringSub(s1, s2, k+1)
    return res

s1 = "ggksggks"
s2 = 'gks'
print(StringSub(s1, s2, 0))