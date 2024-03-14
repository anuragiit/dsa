#!/bin/python3

import sys

def getWays(n, c):
    # Complete this function
    if n==0 or c[0]==n:
        return 1
    if n in range(1,c[0]) and c[0]!=1:
        return 0
    if len(c)==1 and n/c[0]==int(n/c[0]):
        return 1
    if len(c)==1 and n/c[0]!=int(n/c[0]):
        return 0
    else:
        k=0
        arr=[]
        while(n-c[-1]*k>=0):
           arr.append(n-c[-1]*k)
           k+=1
        sum=0
        for i in arr:
            sum+=getWays(i,c[:-1])
        return sum    
            
n, m = input().split(' ')
n, m = [int(n), int(m)]
c = [int(i) for i in input().split(' ')]
c=sorted(c)

# Print the number of ways of making change for 'n' units using coins having the values given by 'c'
ways = getWays(n, c)
print(ways)
