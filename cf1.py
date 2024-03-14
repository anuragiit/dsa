n=int(input())
arr=list(map(int,input().strip().split(' ')))
three=[]
for i in arr:
    if len(three)>3:
        break
    if i not in three:
        three.append(i)
three.sort()
if len(three)==3 and three[1]-three[0]==three[2]-three[1]:
    print(three[1]-three[0])
elif len(three)==2 and (three[1]-three[0])%2==0:
    print(int((three[1]-three[0])/2))
elif len(three)==2 and (three[1]-three[0])%2:
    print(three[1]-three[0])
elif len(three)==1:
    print(0)
else:
    print(-1)

    
    
    
