# Sam._.072
# here we will discuss the recursive method to find subsequence
#  a subsquence may or may nt be continous
# if we look a single charater may or may not be part of subsequence , so fist we find the subsequence of n-1 charater and then take a empty
#  list ,first copy the subsequence of n-1 charater and then add single charater to each subsequence
# e.g if subseqnece is {"", a,b,ab} and the left charater is c then first copy the list as it is {a,b,ab} and then add left charater to each 
# subsequence {"",a,b,ab,c,ac,cb,cab}

def subsequence(s):
    # the base case ,if the length of string is 0 then we have to return a list having a single element and that element is an empty string
    if len(s)==0:
        l1=[]
        l1.append("")
        return l1
    # first we have to find the susequence of n-1 characters
    t=subsequence(s[1:])
    l=[]
    #  and then add the subseqence of n-1 charaters to the new list
    l.extend(t)
    # and then add left characters with the all elements of list
    for i in t:
        l.append(s[0]+i)
    return l

if __name__=='__main__':
    print(subsequence("abcd"))