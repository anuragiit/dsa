from collections import defaultdict
def f2(b):   #using defaultdict
    s=defaultdict(int)
    for i in b:
        s[i]+=1
    return dict(s)

def f3(b):   #using dict simple code
    s=defaultdict(int)
    for i in b:
        if i in s:
          s[i]+=1
        else:
           s[i]=1
    return dict(s)   
    
b=input()
print(f3(b))
