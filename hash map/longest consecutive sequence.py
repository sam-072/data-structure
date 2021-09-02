def longestsequence(a):
    length=0
    startpoint=0
    d=dict()
    for i in a:
        d[i]=d.get(i,True)
    for i in d:
        if d[i]:
            c=1
            j=i+1
            while d.get(j,False):
                d[j]=False
                c+=1
                j+=1
            j=i-1
            while d.get(j,False):
                c+=1
                d[j]=False
                j-=1
            if c>length:
                length=c
                startpoint=j+1

    # if we have to return the starting and ending point
    # return startpoint,startpoint+length-1
    
    # if we to return the length 
    return length

if __name__=='__main__':
    a=list(map(int, input().split()))
    print(longestsequence(a))

             
