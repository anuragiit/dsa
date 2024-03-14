def search_smallest(arr,x):
    low,high=0,len(arr)-1
    ans=None
    while low<=high:
        mid=low+(high-low)//2
        if arr[mid]==x:
            return x
        if arr[mid]>x:
            high=mid-1
        else:
            ans=arr[mid]
            low=mid+1
    if ans==None:
        return -1
    return ans
    
a=[ 3, 4, 6, 9, 10, 12, 14, 15, 17, 19, 21 ] 
for i in range(10):
    x=int(input())
    print(a,search_smallest(a,x),end='\n')
