def findEmpty(a):
    for i in range(9):
        for j in range(9):
            if a[i][j]==0:
                return i,j
    return None

def isValid(a,x,y,num):
    # row validation
    for i in range(9):
        if a[x][i]==num and i!=y:
            return False
    
    # column validation
    for i in range(9):
        if a[i][y]==num and i!=x:
            return False
    
    # box validation
    box_x=x//3
    box_y=y//3
    for i in range(box_x*3,box_x*3+3):
        for j in range(box_y*3,box_y*3+3):
            if a[i][j]==num and i!=x and j!=y:
                return False
    
    return True

def sudoku(a):
    find=findEmpty(a)
    if not find:
        return True
    x,y=find
    for i in range(1,10):
        if isValid(a, x, y, i):
            a[x][y]=i

            if sudoku(a):
                return True
            
            a[x][y]=0

    return False

def printSudoku(a):
    for i in range(9):
        if i%3==0 and i!=0:
            print("_ _ _ _ _ _ _ _ _ _")
        for j in range(9):
            if j%3==0 and j!=0:
                print("|",end=" ")
            print(a[i][j],end=" ")
        print()



if __name__=='__main__':
    a=[]
    for i in range(9):
        a.append(list(map(int,input().split())))

    if sudoku(a):
        printSudoku(a)
    else:
        print(-1)
    
