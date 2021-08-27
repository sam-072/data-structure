def transform(sentence):
    l=list(sentence.split(" "))
    l1=[]
    for i in l:
        s=i[0]
        for j in range(1,len(i)):
            if ord(i[j])==ord(i[j-1]) or abs(ord(i[j])-ord(i[j-1]))==32:
                s+=i[j]
            elif i[j-1]<i[j] and ord(i[j])>=97 and ord(i[j])<=122:
                s+=chr(ord(i[j])-32)
            elif i[j-1]>i[j] and ord(i[j])>=65 and ord(i[j])<=90:
                s+=chr(ord(i[j])+32)
            else:
                s+=i[j]
        l1.append(s)
    return ' '.join(l1)

print(transform("a Blue MOON"))

x,y=5,7
y,x=x,y
print(x,y)