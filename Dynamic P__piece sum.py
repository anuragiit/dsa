# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
from math import pow
def mod(a):
    return a%int(10**9+7)
def piece_sum(a):
    if len(a)==1:
        ps[a]=a[0]
        return a[0]
    sum=0
    n=len(a)
    elesum=0
    for i in range(n-1):
        elesum+=a[i]
        if a[i+1:] in ps:
            sum+=(mod(elesum)*(i+1)*mod(int(pow(2,n-i-2)))+ps[a[i+1:]])
            sum=mod(sum)
        else:
            sum+=(mod(elesum)*(i+1)*mod(int(pow(2,n-i-2)))+piece_sum(a[i+1:]))
            sum=mod(sum)
    elesum+=a[-1]
    sum+=mod(elesum*n)
    ps[a]=sum
    return sum%int(pow(10,9)+7)




n=int(input())
b=[int(i) for i in input().split(' ')]
b=tuple(b)
ps=defaultdict(int)
result=piece_sum(b)
print(result)
    
