# Given an array of integers, sort the array according to frequency of elements.
#  That is elements that have higher frequency come first. 
# If frequencies of two elements are same, then smaller number comes first.

def sortedArray(a,n):
    d=dict()
    for i in a:
        d[i]=d.get(i,0)+1
    d=dict(sorted(d.items(),key=lambda x:(x[1],-x[0]),reverse=True))
    # print(d)
    l=[]
    for i in d:
        for j in range(d[i]):
            l.append(i)
    return l
    

if __name__=='__main__':
    n=int(input())
    a=list(map(int, input().split()))
    print(sortedArray(a, n))

