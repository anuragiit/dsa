def isSafe(row,column,initial):
    for i in range(row):
        if initial[i][column]==1:
            return False
    i,j=row-1,column-1
    while i>=0 and j>=0:
        if initial[i][j]==1:
            return False
        i-=1
        j-=1
    i,j=row-1,column+1    
    while i>=0 and j<a:
        if initial[i][j]==1:
            return False
        i-=1
        j+=1
    return True    

def Nqueen(initial,row):
    if row==a:
        return True
    for i in range(a):
        if isSafe(row,i,initial):
            initial[row][i]=1
            if Nqueen(initial,row+1)==True:
                return True
            initial[row][i]=0
         
    return False    
        
while True:        
    a=int(input())
    initial=[[0 for j in range(a)] for i in range(a)]
    b=Nqueen(initial,0)
    if b==True:
        for i in range(a):
            for j in range(a):
                print(initial[i][j],end='        ')
            print('\n')
    else:
        print('Solution doesnot exist')

