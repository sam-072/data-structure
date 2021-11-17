# Code by : Sam._.072

def NQueen(N):
    ds = [[0 for i in range(N)] for j in range(N)]
    ans = []
    Hc = [0 for i in range(N)]
    Dc = [0 for i in range(2*N-1)]
    Uc = [0 for i in range(2*N-1)]
    Queens(0, N, ds, ans, Hc, Dc, Uc)
    res = []
    for i in ans:
        temp =[]
        for j in i:
            temp.append(j.index(1)+1)
        res.append(temp)
    res.sort()
    return res

def Queens(col, N, ds, ans, Hc, Dc, Uc):
    if col == N:
        temp =[ele[:] for ele in ds]
        ans.append(temp)
        return
    
    for row in range(n):
        if Hc[row] == 0 and Dc[row+col] == 0 and Uc[N-1+col-row] == 0:
            ds[row][col] = 1
            Hc[row] = 1
            Dc[row+col] = 1
            Uc[N-1+col-row] = 1
            Queens(col+1, N, ds, ans, Hc, Dc, Uc)
            ds[row][col] = 0
            Hc[row] = 0
            Dc[row+col] = 0
            Uc[N-1+col-row] = 0




if __name__=='__main__':
    n=int(input())
    print(NQueen(n))