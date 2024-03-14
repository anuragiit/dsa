def minThrow(N, arr):
        # code here
        d=dict()
        for i in range(0,len(arr),2):
            d[arr[i]]=arr[i+1]
        queue=[(1,0)]
        visited=[False]*31
        while len(queue):
            print(queue)
            curr=queue.pop(0)
            if curr[0]==30:
                return curr[1]
            visited[curr[0]]=True
            for i in range(curr[0]+1,min(30,curr[0]+6)+1):
                if i in d :
                    val=d[i]
                else:
                    val=i
                if not visited[val]:
                       queue.append((val,curr[1]+1))
                       visited[val]=True
        if visited[30]==False:
            return -1


n=int(input())
arr=[int(i) for i in input().split(' ')]
result=minThrow(n,arr)
print(result)
        
        
