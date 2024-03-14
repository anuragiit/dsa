n=int(input(" Enter how many names you want to sort!\n"))# sorting for strings
print("Enter those",n,"names")
l=list()
for p in range(n):
    q=(input("Enter "+str(p+1)+"th name:"))
    l.append(q)
print("Names in list beore sorting:")
print(l)
print("Names in list after sorting:")
for p in range(n-1):
    for i in range(n-p-1):
        if l[i]>l[i+1]:
            a=l[i]  # used variable 'a' for sorting alphabets only otherwise for numbers addition method of sorting is always better
            l[i]=l[i+1]
            l[i+1]=a

print(l)
#Now for sorting numbers
n=int(input(" Enter how many numbers you want to sort!\n"))
print("Enter those",n,"numbers")
l=list()
for p in range(n):
    q=int(input("Enter "+str(p+1)+"th number:"))
    l.append(q)
print("Nunbers in list beore sorting:")
print(l)
print("Numbers in list after sorting:")
for p in range(n-1):
    for i in range(n-p-1):
        if l[i]>l[i+1]:
            a=l[i]
            l[i]=l[i+1]
            l[i+1]=a
print(l)            

