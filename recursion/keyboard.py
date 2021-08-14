# Sam._.072   :)

# Given an integer n  using phone keypad find out all the possible strings that can bemade using digits of input n.
# e.g if n=23 then output is { ad , ae, af, bd, be, bf, cd, ce, cf}
# the mobile keybad looks like:
#  2: abc   3: def    4:ghi
#  5: jkl   6: mno    7:pqrs
#  8: tuv   9: wxyz

# here first we find the soultin for n//10 and then we multiply n%10 with every elements of the solution comes from n//10
#  and we do this recursively

def keypad(n):
    # first we make a dictonary of the digits as key and alphabets it represent as value
    d={2: "abc", 3: "def", 4:"ghi",5: "jkl", 6: "mno",7:"pqrs",8: "tuv", 9: "wxyz"}

    # the base if the digit is single digit i.e if n is greater than 0 and less than 10 , then we return a list of alpabets its represent
    if n>0 and n<10:
        s=d[n]
        l=[]
        for i in s:
            l.append(i)
        return l
    #  we recursively call this function for n//10 and store its result in t
    t=keypad(n//10)
    s=d[n%10]
    # then here we add all the elements of n%10 to all the elements of t
    l=[]
    for i in s:
        for j in t:
            l.append(j+i)
    return l

if __name__=='__main__':
    print(keypad(234))    