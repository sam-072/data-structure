# Code by : Sam._.072 

# Utility Function to Check If Cell is safe for any queen or Not
# Time Complexity : O(N)
def Fill(row, col, ds, N):
    # Left Row Check
    i = col -1
    while i>=0:
        if ds[row][i] == 'Q':
            return False
        i -= 1

    # Lower Diagnal Check
    i ,j = row+1, col-1
    while i < N and j>=0:
        if ds[i][j] == 'Q':
            return False
        i += 1
        j -= 1
    
    # Upper Diagonal Check
    i, j = row - 1, col - 1
    while i>=0 and j>=0:
        if ds[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    return True




# Time Complexity : O(N^2)

def NQueens(col, N, ds, ans, c, Hc, Dc, Uc):
    if col == N:
        temp = [ele[:] for ele in ds]
        ans.append(temp)
        c[0] +=1
        return 
    for row in range(N):
        # if Fill(row, col, ds, N): this will take O(N) Time. 

        if Hc[row] == 0 and Dc[row+col] == 0 and Uc[N-1+col-row] == 0:  # this will take O(1) time 
            ds[row][col] = 'Q'
            Hc[row] = 1
            Dc[row+col] = 1
            Uc[N-1+col-row] = 1

            NQueens(col+1, N, ds, ans, c, Hc, Dc, Uc)
        # Backtracking
            ds[row][col] = 0
            Hc[row] = 0
            Dc[row+col] = 0
            Uc[N-1+col-row] = 0




if __name__=='__main__':

    n=int(input())
    ds = [[0 for i in range(n)] for j in range(n)]
    ans = []
    c = [0]  # this is for returning the no of all possible N queen patterns

    # This is for Left Row check
    Hc = [0 for i in range(n)]  

    # This is for Lowwer Diagonal Check 
    Dc = [0 for i in range(2*n-1)]

    # This is for Upper Diagonal Check
    Uc = [0 for i in range(2*n-1)]

    NQueens(0, n, ds, ans, c, Hc, Dc, Uc)

    print(c[0])

    for i in range(c[0]):
        for j in range(n):
            for k in range(n):
                print(ans[i][j][k],end=" ")
            print()
        print()
