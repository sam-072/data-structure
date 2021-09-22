def printPath(n):
    board= [ [0 for i in range(n)] for j in range(n)]
    return(printPathHelper(0,n,board,[]))

def printPathHelper(row,n,board,l):
    if row==n:
        l=[]
        for i in range(n):
            for j in range(n):
                if board[j][i]==1:
                    l.append(j+1)
                    break
        return l
    
    for col in range(n):
        if isSafe(row,col,n,board):
            board[row][col]=1
            l1=(printPathHelper(row+1,n,board,l))
            if len(l1)==n:
                l.append(l1)
            board[row][col]=0
    return l

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


if __name__=='__main__':
    n=int(input())
    print(printPath(n))