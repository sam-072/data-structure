# In this question we are given an array of length n and a integer k . we have to return a
# list of subsets whose's sum is k 
def subsets_of_sum_k(a,k,si=0):
    if si==len(a):
        if k==0:
            l=[]
            l.append(0)
            return l
        else:
            return []
    t1=subsets_of_sum_k(a, k-a[si],si+1)
    t2=subsets_of_sum_k(a, k,si+1)
    l=[]
    if len(t1)!=0:
        for i in t1:
            l1=[]
            l1.append(a[si])
            for j in i:
                l1.append(j)
            l.append(l1)
    if len(t2)!=0:
        for i in t2:
            l.append(i)
    return l



if __name__=='__main__':
    n,k=map(int,input().split())
    a=list(map(int, input().split()))
    print(subsets_of_sum_k(a,k))