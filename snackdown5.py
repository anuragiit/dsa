import sys
X=[1,1,-1,-1,2,2,-2,-2]
Y=[2,-2,2,-2,1,-1,1,-1]

def isValid(n,x,y,moveX,moveY,visited):
    if 0<=x+moveX<=n-1 and 0<=y+moveY<=n-1 and not visited[x+moveX][y+moveY]:
        return True
    return False    
def func(n,startX,startY,endX,endY,visited):
    if startX==endX and startY==endY:
        return 0
    queue=[(startX,startY,0)]
    visited[startX][startY]=True
    c=0
    while len(queue):
        temp=queue.pop(0)
        for i in range(8):
            if isValid(n,temp[0],temp[1],X[i],Y[i],visited):
                queue.append((temp[0]+X[i],temp[1]+Y[i],temp[2]+1))
                visited[temp[0]+X[i]][temp[1]+Y[i]]=True
            if temp[0]+X[i]==endX and temp[1]+Y[i]==endY:
                return temp[2]+1
                
t=int(input())
for i in range(t):
    n=int(input())
    startX,startY=list(map(int,input().strip().split(' ')))
    endX,endY=list(map(int,input().strip().split(' ')))
    visited=[[False for j in range(n)] for i in range(n)]
    result=func(n,startX-1,startY-1,endX-1,endY-1,visited)
    print(result)
        
