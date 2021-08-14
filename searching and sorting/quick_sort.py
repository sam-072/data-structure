# Sam._.072   :)
#  here i will discuss about the quick sort algorithm 
#  this algorithm is also based on divide and conqurer algorithm 
#  In this algorithm first we find the right postion for the first element and then array the array in such a manner that the elements 
# smaller than the pivot element is to the left of pivot and elements greater than the pivot element are to the right of the pivot
#  and we repeat the above process for every left and right of pivot
# for this we need a partation function which will do 2 things first find the correct index for the piviot and then rearrange the elements

def partation(a,l,r):
    # we will count the no of elements which are lower than the pivot element and swap the pivot or first elements with l+c index 
    c=0
    for i in range(l,r+1):
        if a[i]<a[l]:
            c+=1
    a[c+l],a[l]=a[l],a[c+l]
    i=l
    j=r
    while i<j:
        if a[i]<a[c+l]:
            i+=1
        elif a[j]>=a[c+l]:
            j-=1
        else:
            a[i],a[j]=a[j],a[i]
            i+=1
            j-=1
    # here we return the index of the pivot elemet after rearraning the array
    return c+l

def quick_sort(a,l,r):
    #  the base when left is greater than the right
    if l>=r:
        return
    # first we will store the pivot index in p
    p=partation(a, l, r)
    # then call qucik sort the left of pivot and call merge sort on the right of pivot
    quick_sort(a, l, p-1)
    quick_sort(a, p+1, r)

if __name__=='__main__':    
    a=[10,2,3,12,9,16,2]    
    quick_sort(a, 0, 6)   # the qucik sort take 3 arguments first is an array , 2nd  is initial size i.e 0 and 3rd is right index i.e len(A)-1
    print(a)