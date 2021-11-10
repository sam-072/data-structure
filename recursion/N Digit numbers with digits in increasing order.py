# Code by : Sam._.072

def increasingNumbers(N):
    if N==1:
        return ['0','1','2','3','4','5','6','7','8','9']
    l = increasingNumbers(N-1)
    if l[0]=='0':
        l.pop(0)
    n=len(l)
    ans = []
    for i in range(n):
        x = int(l[i][-1])
        for j in range(x+1,10):
            ans.append(l[i]+str(j))
    return ans
    	        
print(increasingNumbers(3))