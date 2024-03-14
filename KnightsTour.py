def isValidMove(board,x,y,move_x,move_y):
    if x+move_x>=a or x+move_x<0:
        return False
    if y+move_y>=a or y+move_y<0:
        return False
    if visited[x+move_x][y+move_y]==True:
        return False
    return True
    


def KnightsTour(board,x,y):
    global count
    if count==int(a**2)-1:
        return True
    for i in range(8):
        if isValidMove(board,x,y,movex[i],movey[i]):
            new_x=x+movex[i]
            new_y=y+movey[i]
            visited[new_x][new_y]=True
            count+=1
            board[new_x][new_y]=count
            if KnightsTour(board,new_x,new_y)==True:
                return True
            visited[new_x][new_y]=False   #three
            count-=1                                    #backtracking
            board[new_x][new_y]=0           #statements
    return False       


movex=[-1,-1,1,1,-2,-2,2,2]
movey=[2,-2,2,-2,-1,1,-1,1]
while True:
    count=0
    a=int(input())
    board=[[0 for i in range(a)] for i in range(a)]
    visited=[[False for i in range(a)] for j in range(a)]
    visited[0][0]=True
    b=KnightsTour(board,0,0)
    if b==False:
        print('Tour cant be completed')
    else:    
        for i in range(a):
            for j in range(a):
                print(board[i][j],'   *  ',end='         ')
            print('\n','************************************************************************************************************')
        for i in range(a):
            for  j in range(a):
                print(visited[i][j],end=' ')
            print('\n')    
