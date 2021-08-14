# Sam._.072   :)
# here i am going to discuss the merge sort
# basically merge sort work on the idea of divide and conqurer. here we divide the array in smaller part then 
#  then sort the smaller part and merge these smaller part in sorted way
#  this is most efficient way of sorting an array
# the time complexity of the algorith is O(nlog(n))
# basically we need two function , first one is merge sort which will divide the array into smaller parts and then call 
#  the 2nd function merge which will merge the two sorted parts in sorted order

# the merge fnction basically take 3 arguments first two will the smalller array and the 3rd one is the bigger array

def merge(a1,a2,a):
    i=0   # this variable is for the first array i.e for a1
    j=0   # this variable is for the 2nd array i.e for a2
    k=0   # this is for the bigger array

    while i<len(a1) and j<len(a2):
        if a1[i]<a2[j]:
            a[k]=a1[i]
            i+=1
            k+=1
        else:
            a[k]=a2[j]
            j+=1
            k+=1
# this loop is for copying remaining elements from a1 to a
    while i<len(a1):
        a[k]=a1[i]
        i+=1
        k+=1
# this loop is for copying remaining elemets from a2 to a
    while j<len(a1):
        a[k]=a2[j]
        j+=1
        k+=1

# now the main function merge sort , first we will find the middle index of the given array and we divide the given array into two parts
# a1 will contain the elements from index 0 to middle index -1 and a2 will contians elements from middle to the last 
#  and we recursively call on for the a1 and then for a2
def merge_sort(a):
    # the base case , when the array length is 0 or 1 we have to do nothing simply return because the array of length 1 os sorted
    if len(a)==0 or len(a)==1:
        return
    
    m=len(a)//2
    a1=a[:m]
    a2=a[m:]
    merge_sort(a1)
    merge_sort(a2)
    merge(a1, a2, a)


if __name__=='__main__':
    a=[12,1,4,22,5,3,90]
    merge_sort(a)
    print(a)