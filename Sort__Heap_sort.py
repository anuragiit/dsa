def move_up(l,p):
    a=l[p]
    while p!=1:
        if a>l[int(p/2)]:
            l[p]=l[int(p/2)]
            p=int(p/2)
        else:
            break
    l[p]=a

def move_down(l,k):
    a=l[1]
    j=2
    while j<=k:
        if j<k and l[j+1]>l[j]:
            j=j+1
        if l[j]<l[int(j/2)]:
            break
        l[int(j/2)]=l[j]
        j=j*2
          
    l[int(j/2)]=a    
            
n=int(input(" Enter how many numbers you want to sort!\n"))
print("Enter those",n,"numbers")
l=[0]
for p in range(1,n+1):
    q=int(input("Enter "+str(p)+"th number:"))
    l.append(q)
    move_up(l,l.index(q))
print("Numbers in list beore sorting:")
print(l)
print("Numbers in list after sorting:")
for i in range(n,1,-1):
    a=l[1]
    l[1]=l[i]
    l[i]=a
    print("Hello",i)
    move_down(l,i)
print(l)    
