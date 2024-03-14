def isPossible(ele,arr,k):
    count=1
    pos=arr[0]
    for i in range(1,len(arr)):
        if arr[i]-pos>=ele:
            pos=arr[i]
            count+=1
        if count==k:
            return True
    return False
            
def func(arr,n,k):
    result=-1
    low=0
    high=arr[n-1]-arr[0]
    while low<=high:
        mid=int((low+high)/2)
        if isPossible(mid,arr,k):
            result=mid
            low=mid+1
        else:
            high=mid-1
    return result        

t=int(input())
for i in range(t):
    n,k=list(map(int,input().strip().split(' ')))
    arr=list(map(int,input().strip().split(' ')))
    result=func(arr,n,k)
    print(result)
