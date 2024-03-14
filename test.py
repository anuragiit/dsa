def func(maze,n,m):
    if maze[n-1][m-1]==-1:
       return 0
    dp=[[0 for j in range(m)] for i in range(n)]
    dp[0][0]=1
    for i in range(1,m):
        if maze[0][i]==0:
            dp[0][i]=dp[0][i-1]
        else:
            dp[0][i]=0
    for i in range(1,n):
        if maze[i][0]==0:
            dp[i][0]=dp[i-1][0] 
        else:
            dp[i][0]=0    
    for i in range(1,n):
        for j in range(1,m):
            if maze[i][j]==-1:
                dp[i][j]=0
            else:
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
    return dp[n-1][m-1]            

t=int(input())
for i in range(t):
    n,m,k=list(map(int,input().strip().split(' ')))
    maze=[[0 for j in range(m)] for i in range(n)]
    blocked=input().strip().split(' ')
    if len(blocked)!=1:
        b=list(map(int,blocked))
        for i in range(0,len(b)-1,2):
            temp1=b[i]-1
            temp2=b[i+1]-1
            maze[temp1][temp2]=-1
    result=func(maze,n,m)
    print(result)
