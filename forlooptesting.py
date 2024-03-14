l=[x for x in range(2,21)]
print(l)
for x in l:
    print(x)
    for p in range(x,21,x):
        l.remove(p)
    print(l)
    
