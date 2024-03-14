hash={'a':'2','b':'22','c':'222','d':'3','e':'33','f':'333','g':'4','h':'44','i':'444','j':'5','k':'55','l':'555','m':'6','n':'66','o':'666','p':'7','q':'77','r':'777','s':'7777','t':'8','u':'88','v':'888','w':'9','x':'99','y':'999','z':'9999'}
def convert(message):
    string=''
    for i in message:
        string+=hash[i]
    print(string)    
    return string

def ways(c,i):
   if c==1:
       return 1
   if c==2:
       return 2
   if c==3:
       return 4
   if i==4 and c==4:
       return 8
   if i==3:
       dp=[1 for i in range(c)]
       dp[0],dp[1],dp[2]=(1,2,4)
       for i in range(3,c):
           dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
       print(dp)    
       return dp[c-1]
   else:
       dp=[0 for i in range(c)]
       dp[0],dp[1],dp[2],dp[3]=(1,2,4,8)
       for i in range(4,c):
           dp[i]=dp[i-1]+dp[i-2]+dp[i-3]+dp[i-4]
       print(dp)     
       return dp[c-1]
        
def func(numbers):
    if len(numbers)==1:
        return 1
    mul=1
    c=1
    top=numbers[0]
    for i in range(1,len(numbers)):
        if numbers[i]==top:
            c+=1
        else:
             if numbers[i]=='7' or numbers[i]=='9':
               mul*=ways(c,4)
               c=1
               top=numbers[i]
             else:
                mul*=ways(c,3)
                c=1
                top=numbers[i]
    if top=='7' or top=='9':            
          mul*=ways(c,4)
    else:
        mul*=ways(c,3)
        
    return mul
        
t=int(input())
for i in range(t):
    message=input()
    numbers=convert(message)
    result=func(numbers)
    print(result)
