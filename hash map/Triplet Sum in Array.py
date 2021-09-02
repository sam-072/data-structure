# Given an array arr of size n and an integer X. Find if there's a triplet in the array which sums up to the given integer X.
# t.c = O(n^2)


def find3Numbers(A, n, x):
        # Your Code Here
        d=dict()
        for i in A:
            d[i]=d.get(i,0)+1
        for i in range(n):
            for j in range(i+1,n):
                if d.get(x-A[i]-A[j],0)>0 and x-A[i]-A[j]!=A[i] and x-A[i]-A[j]!=A[j]:
                    return True
        return False

if __name__=='__main__':
    n,x=map(int, input().split())
    a=list(map(int, input().split()))
    print(find3Numbers(a, n, x))