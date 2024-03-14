n=int(input(" Enter how many numbers you want to sort!\n"))
print("Enter those",n,"numbers")
l=list()
for p in range(n):
    p=int(input("Enter "+str(p+1)+"th number:"))
    l.append(p)
print("Nunbers in list beore sorting:")
print(l)
print("Numbers in list after sorting:")
for p in range(n-1):
    for i in range(p+1,n):
        if l[p]>l[i]:
            a=l[p]
            l[p]=l[i]
            l[i]=a
print(l)            
