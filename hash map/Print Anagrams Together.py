# problem name : Print Anagrams Together
# problem link : https://practice.geeksforgeeks.org/problems/print-anagrams-together/1/?category[]=Hash&category[]=Hash&problemStatus=unsolved&page=1&query=category[]HashproblemStatusunsolvedpage1category[]Hash


def hash(s):
    c=0
    for i in s:
        c+=ord(i)
    return c
