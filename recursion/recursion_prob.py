import sys
sys.setrecursionlimit(2000)
# this will increase the recursion limit of your computer

def fac(n):
    if n==1:
        return 1
    return n*fac(n-1)

def power(x,y):
    if y==0:
        return 1
    else:
        return x*power(x,y-1)
def fibonacci(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)
def sumarray(a,i=0):
    if len(a)==i:
        return 0
    return a[i]+sumarray(a,i+1)

def isSorted(a,i=0):
    if len(a)==i or i==len(a)-1:
        return True
    if a[i]>a[i+1]:
        return False
    return isSorted(a,i+1)

def indexf(a,x):
    if len(a)==0:
        return -1
    if a[0]==x:
        return 0
    t=indexf(a[1:],x)
    if t==-1:
        return -1
    return 1+t

def indexv2(a,x,i=0):
    if len(a)==0 or i==len(a)-1:
        return -1
    if a[i]==x:
        return i
    return indexv2(a,x,i+1)

def lastIndex(a,x):
    if len(a)==0:
        return -1
    t=lastIndex(a[1:],x)
    if t!=-1:
        return t+1
    else:
        if a[0]==x:
            return 0
        else:
            return -1

def replace_char(s,a,b):
    if len(s)==0:
        return s
    t=replace_char(s[1:], a, b)
    if s[0]==a:
        return b+t
    else:
        return s[0]+t

def remove_char(s,a):
    if len(s)==0:
        return s
    t=remove_char(s[1:], a)
    if s[0]==a:
        return t
    else:
        return s[0]+t
    
def replace_pi(s):
    if len(s)==0 or len(s)==1:
        return s
    
    if s[0]=='p' and s[1]=='i':
        t=replace_pi(s[2:])
        return "3.14"+t
    else:
        t=replace_pi(s[1:])
        return s[0]+t

# write a program which reomove consecutive dublictes from given string
# e.g : if given string is xxxyyxwwzz then output should be xyzwz
def remove_dub(s):
    if len(s)==1:
        return s
    t=remove_dub(s[1:])
    if s[0]==t[0]:
        return t
    else:
        return s[0]+t

def binarySearch(a,l,r,x):
    if r<l:
        return -1
    m=(r+l)//2
    if a[m]==x:
        return m
    elif a[m]>x:
        return binarySearch(a, l, m-1, x)
    else:
        return binarySearch(a, m+1, r, x)


# print(fac(1900))
print(power(2,4))
print(fibonacci(6))
print(sumarray([1,22,3,14,5]))
# print(replace_char("abcdedd", 'c', 'x'))
print(remove_char("a", 'x'))
print(replace_pi("pippisxy"))
print(remove_dub("xxx"))
print(binarySearch([1,2,3,4,5,6], 0, 5, 11))