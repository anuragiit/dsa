def heapify(arr,i,size):
    child=2*i+1
    if child+1<=size and arr[child]<arr[child+1]:
        child+=1
    if child<=size and arr[i]<arr[child]:
        arr[child],arr[i]=arr[i],arr[child]
        heapify(arr,child,size)

def heapsort(arr):
    n=len(arr)
    k=n//2-1
    for i in range(k,-1,-1):
        heapify(arr,i,n-1)
    print("heap",arr)    
    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heapify(arr,0,i-1)
    return arr    

arr=[int(i) for i in input().split(' ')]
result=heapsort(arr)
print(result)
        
