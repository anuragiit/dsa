n=int(input(" Enter how many numbers you want to sort!\n"))
print("Enter those",n,"numbers")
l=list()
for p in range(n):
    p=int(input("Enter "+str(p+1)+"th number:"))
    l.append(p)
print("Nunbers in list beore sorting:")
print(l)
print("Numbers in list after sorting:")
for p in range(1,n):
    q=p-1
    a=l[p]
    while q>=0 and a<l[q]:
        l[q+1]=l[q]
        q=q-1
    l[q+1]=a
print(l)    
        
