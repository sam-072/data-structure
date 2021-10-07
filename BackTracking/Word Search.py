def Word(x,y,n,m,l,l1,s,k):
    if k==len(s):
        return True

    if x<0 or y<0 or x>=n or y>=m or k>=len(s) or l1[x][y]==1 or l[x][y]!=s[k]:
        return False

    l1[x][y] = 1
    res = Word(x-1, y, n, m, l, l1, s, k+1) or Word(x+1, y, n, m, l, l1, s, k+1) or Word(x, y-1, n, m, l, l1, s, k+1) or Word(x, y+1, n, m, l, l1, s, k+1)
    l1[x][y] = 0
    return res

def check(l,n,m,s):
    l1=[[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            if l[i][j]==s[0]:
                if Word(i, j, n, m, l, l1, s, 0):
                    return True
                
    return False
                

if __name__=='__main__':
    n,m = map(int, input().split())
    l=[]
    for i in range(n):
        l.append(input())
    s=input()
    print(check(l, n, m, s))
                