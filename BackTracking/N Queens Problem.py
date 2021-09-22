def isSafe(row,col,n,board):

    # vertical check
    i = row -1
    while i >=0:
        if board[i][col]==1:
            return False
        i -= 1
    
    # left diagonal check
    i = row -1
    j = col -1
    while i>=0 and j>=0:
        if board[i][j]==1:
            return False
        i-=1
        j-=1
    
    # right diagonal check
    i=row - 1
    j=col + 1
    while i>=0 and j<n:
        if board[i][j]==1:
            return False
        i-=1
        j+=1
    
    return True

def printPathHelper(row,n,board):

    if row == n:
        for i in range(n):
            for j in range(n):
                print(board[i][j],end=" ")
            print()
        print()
        return 1
    c=0
    for col in range(n):
        if isSafe(row,col,n,board) is True:
            board[row][col]=1
            c+=printPathHelper(row+1, n, board)
            board[row][col]=0
    return c

def printPath(n):
    board = [ [0 for i in range(n)] for j in range(n)]
    print(printPathHelper(0,n,board))
    



if __name__=='__main__':
    n=int(input())
    printPath(n)
