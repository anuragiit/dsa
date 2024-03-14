def func(arr,n):
    c=0
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if arr[i]*arr[j]==arr[k] or arr[k]*arr[j]==arr[i] or arr[i]*arr[k]==arr[j]:
                    c+=1
    return c                
                


t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().strip().split(' ')))
    result=func(arr,n)
    print('Case #'+str(i+1)+': '+str(result))
