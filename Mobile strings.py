def allstrings(arr,n):
    if n==len(arr)-1:
        return hash[arr[n]]
    else:
        l=allstrings(arr,n+1)
        new_l=[]
        for i in hash[arr[n]]:
            temp=l.copy()
            for j in range(len(temp)):
                temp[j]=i+temp[j]
            new_l+=temp
        return new_l    
                
                
hash={2:['a','b','c'],3:['d','e','f'],4:['g','h','i'],5:['j','k','l'],
6:['m','n','o'],7:['p','q','r','s'],8:['t','u','v'],9:['w','x','y','z']}

t=int(input())
for i in range(t):
    n=int(input())
    arr=[int(i) for i in input().strip().split(' ')]
    result=allstrings(arr,0)
    for i in result:
        print(i,end=' ')
