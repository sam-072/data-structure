#  Sam._.072  :)
# BINARY SEARCH using RECURSION
# so the first prerequesity is that the given array should be sorted 
# and we will provide the sorted array and the target element to be search as function argument
 

def binarySearch(a,x,l,r):
    #  the base case : if right is smaller than the left then the element is not present the given array
    # you shhould return -1
    if r<l:
        return -1
    
    # find the middle elements of the array i.e (l+r)//2
    m=(l+r)//2

    #now check if the middle element is our target element , if yes then return the middle i.e the index of middle element
    if a[m]==x:
        return m
    
    # if not , then check is middle element greater than the target element , then we have to recursively call 
    # binary search on the left side of the middle element
    #  left will be same but right will be middle -1 and return because we are returning the index of target element
    elif a[m]>x:
        return binarySearch(a, x, l, m-1)
    
    # if middle element is less than the target element then we have to recursively call binary search on right side of middle element
    # here left is changed to middle + 1 and right is as it  is

    else:
        return binarySearch(a, x, m+1, r)


if __name__=='__main__':
    a=[1,2,3,4,5,12]

    # whenever your are callig binary search left index will be 0 and right index will length -1

    print(binarySearch(a, 2, 0, 5))

