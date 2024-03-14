X=[0,0,1,1,1,-1,-1,-1]
Y=[1,-1,0,1,-1,0,1,-1]
def isValid(matrix,n,m,x,y,visited):
    if 0<=x<=n-1 and 0<=y<=m-1 and matrix[x][y]==1  and not visited[i][j]:
        return True
    return False
def bfs(matrix,n,m,i,j,visited):
    queue=[(i,j)]
    visited[i][j]=True
    while len(queue):
        temp=queue.pop(0)
        for i in range(8):
            if isValid(matrix,n,m,temp[0]+X[i],temp[1]+Y[i],visited):
                visited[temp[0]+X[i]][temp[1]+Y[i]]=True
                queue.append((temp[0]+X[i],temp[1]+Y[i]))
                
def findIslands(arr, n, m):
    visited=[[False for j in range(m)] for i in range(n)]
    c=0
    for i in range(n):
        for j in range(m):
            if matrix[i][j]==1 and not visited[i][j]:
                bfs(arr,n,m,i,j,visited)
                c+=1
    return c

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(n[1])]for j in range(n[0])]
        c=0
        for i in range(n[0]):
            for j in range(n[1]):
                matrix[i][j] = arr[c]
                c+=1
        print(findIslands(matrix, n[0], n[1]))
