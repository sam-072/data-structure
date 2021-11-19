# Code by : Sam._.072

def maze(x, y, n, m, ds, ans):
    if x == n-1 and y == n-1:
        ans.append(''.join(ds))
        return
    
    m[x][y] = 0   # this is to make previous path 0 so that there will not be infinite recursion

    if x+1<n and m[x+1][y]==1:
        ds.append('D')
        maze(x+1, y, n, m, ds, ans)
        ds.pop()   # backtrack
    
    if x-1<=0 and m[x-1][y]==1:
        ds.append('U')
        maze(x-1, y, n, m, ds, ans)
        ds.pop()
    
    if y+1<n and m[x][y+1]==1:
        ds.append('R')
        maze(x, y+1, n, m, ds, ans)
        ds.pop()
    
    if y-1<=0 and m[x][y-1]==1:
        ds.append('L')
        maze(x, y-1, n, m, ds, ans)
        ds.pop()
    
    m[x][y] = 1 # undoing the changes 

    return


if __name__ == '__main__':
    n=int(input())
    m = []
    for i in range(n):
        m.append(list(map(int,input().split())))
    ans = []
    if m[0][0]==0 or m[n-1][n-1]==0:
        print(ans)
    else:
        ds = []
        maze(0, 0, n, m, ds, ans)
        print(ans)
        

