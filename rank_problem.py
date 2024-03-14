from math import factorial as f
def Co(n,r):
     a=f(n)/(f(r)*f(n-r))
     return a        

def ways(h,v):
    a=Co(h+v,v)
    return a

def func(h,v,n):
    global result
    if h==0:
         result+=(v*'V')
    elif ways(h-1,v)==n:
         result+=('H'+v*'V'+(h-1)*'H')
    elif ways(h-1,v)>n:
         result+='H'
         func(h-1,v,n)
    else:
         result+='V'
         func(h,v-1,n-ways(h-1,v))
         
         
t=int(input())
for i in range(t):
    h,v=list(map(int,input().strip().split(' ')))
    n=int(input())
    result=''
    func(h,v,n)
    print(result)
