n=input()
l=[]
d={'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
for i in d[n[0]]:
    l.append(i)
for i in range(1,len(n)):
    x=[]
    for j in d[n[i]]:
        for k in range(len(l)):
            x.append(l[k]+j)
    l=x[:]
print(l)
