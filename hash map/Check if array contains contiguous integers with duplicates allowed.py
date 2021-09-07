# problem name : Check if array contains contiguous integers with duplicates allowed
# problem link : https://practice.geeksforgeeks.org/problems/check-if-array-contains-contiguous-integers-with-duplicates-allowed2046/1/?category[]=Hash&category[]=Hash&problemStatus=unsolved&difficulty[]=0&difficulty[]=1&page=1&query=category[]HashproblemStatusunsolveddifficulty[]0difficulty[]1page1category[]Hash

# Given an array of n integers(duplicates allowed). Print “Yes” if it is a set of contiguous integers else print “No”.

# Example 1:
# Input : arr[ ] = {5, 2, 3, 6, 4, 4, 6, 6}
# Output : Yes


def check(a):
    d=dict()
    l,h=1000000,0
    for i in a:
        d[i]=d.get(i,1)
        if i<l:
            l=i
        if i>h:
            h=i
    for i in range(l,h+1):
        if d[i]!=1:
            return False
    return True

if __name__=='__main__':
    a=list(map(int, input().split()))
    print(check(a))
    