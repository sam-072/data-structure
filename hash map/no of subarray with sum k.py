# we will do this using hashing. so your logic will be , we will maintain 
# current sum variable which will store the sum from starting index to till
# that index and also maintain a dictionary which will count the current sum frequency 
#  if the sum is euqal to the desired sum then we will increment your count and 
# and then check if current sum - desired sum is present in your dictinoary or not, if present
# then add that count i.e d[current sum - desired sum] to your  result 

def noOfSubarray(a,k):
    d=dict()
    p,c=0,0
    for i in a:
        p+=i
        d[p]=d.get(p,0)+1
        if p==k:
            c+=1
        if d.get(p-k,0)>0:
            c+=d[p-k]
    # print(d)
    return c

if __name__=='__main__':
    n,k=map(int,input().split())
    a=list(map(int, input().split()))
    print(noOfSubarray(a, k))
