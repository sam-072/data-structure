# Code by : Sam._.072

def rem(s):
    i,n=0,len(s)
    ans = ''
    while i<n:
        if i<n-1 and s[i]==s[i+1]:
            while i<n-1 and s[i]==s[i+1]:
                i+=1
            i+=1
        else:
            ans+=s[i]
            i+=1
    return ans
def remove(s):
    ans,temp=s,''
    while len(temp)!=len(ans):
        temp=ans
        ans=rem(ans)
    return ans
s='geeksforgeek'
print(remove(s))
# print(s)


