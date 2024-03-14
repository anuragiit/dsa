def knapsack(val,w,W,n):
    if n==1 and w[0]<=W:  
        return val[0]
    elif n==1 and w[0]>W:
        return 0
    else:
        a=val[n-1]+knapsack(val,w,W-w[n-1],n-1)
        b=knapsack(val,w,W,n-1)
        if a>b and w[n-1]<=W:
            return a
        else:
              return b
            
val=[10,20,30,40,50,60]
w=[6,8,11,12,13,16]
W=30
a=knapsack(val,w,W,len(w))
print(a)
val=[12,8,17,21,3,22]
w=[6,8,11,12,13,16]
W=30
a=knapsack(val,w,W,len(w))
print(a)


