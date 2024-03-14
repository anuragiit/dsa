def smaller(index,string):
    c=0
    for i in range(index+1,len(string)):
        if string[i]<string[index]:                                        #Never coniser the equal case only count for smaller
            c+=1
    return c
    
    
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
    
def repeated(string,index):
    hash={}
    for i in range(index,len(string)):               #get the repeatition dictionary for the remaining i.e. from that index(including it) to last character
        if string[i] in hash:
            hash[string[i]]+=1
        else:
            hash[string[i]]=1     
    return hash        
        
def func(string):
    l=len(string)
    index=0
    rank=1
    while index<len(string)-1:
        count=smaller(index,string)
        f=fact(l-index-1)
        d=repeated(string,index)
        for i in d.keys():
            f=int(f/d[i])
        rank+=(count*f)
        rank%=1000007
        index+=1
    return rank    
        

t=int(input())
for i in range(t):
   string=input()
   result=func(string)
   print(result)
