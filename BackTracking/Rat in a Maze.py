def printPath(maze,n):
    solution = [[0 for i in range(n)] for j in range(n)]
    printPathHelper(n,0,0,maze,solution)

def printPathHelper(n,x,y,maze,solution):

    if x==n-1 and y==n-1:
        solution[x][y]=1
        print(solution)
        return
    
    if x<0 or y<0 or x>=n or y>=n or maze[x][y]==0 or solution[x][y]==1:
        return 
    
    solution[x][y]=1
    printPathHelper(n, x+1, y, maze, solution)
    printPathHelper(n, x, y+1, maze, solution)
    printPathHelper(n, x-1, y, maze, solution)
    printPathHelper(n, x, y-1, maze, solution)
    solution[x][y]=0
    return
    

if __name__=='__main__':
    n=int(input())
    maze=[]
    for i in range(n):
        maze.append(list(map(int,input().split())))
    printPath(maze,n)