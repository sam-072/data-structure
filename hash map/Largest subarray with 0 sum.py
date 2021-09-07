# problem name : Largest subarray with 0 sum
# problem link : https://practice.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1/?category[]=Hash&category[]=Hash&problemStatus=unsolved&difficulty[]=0&difficulty[]=1&page=1&query=category[]HashproblemStatusunsolveddifficulty[]0difficulty[]1page1category[]Hash

# Given an array having both positive and negative integers. The task is to compute the length of the largest subarray with sum 0.

# Example 1:

# Input:
# N = 8
# A[] = {15,-2,2,-8,1,7,10,23}
# Output: 5

def largestsubarray(n,a):
    h=0
    d=dict()
    d[a[0]]=0
    for i in range(1,n):
        a[i]=a[i-1]+a[i]
        if d.get(a[i],-1)==-1:
            d[a[i]]=i
        else:
            if h< i-d[a[i]]:
                h=i-d[a[i]]
        if a[i]==0:
            if h< i+1:
                h=i+1
    return h

if __name__=='__main__':
    n=int(input())
    a=list(map(int, input().split()))
    print(largestsubarray(n, a))