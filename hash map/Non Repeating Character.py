# Given a string S consisting of lowercase Latin Letters. Find the first non-repeating character in S.


def nonrepeatingCharacter(s):
        #code here
        d=dict()
        for i in s:
            d[i]=d.get(i,0)+1
        print(d)
        for i in s:
            if d[i]==1:
                return i
        return '$'

s=input()
print(nonrepeatingCharacter(s))
