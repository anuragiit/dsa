x={'abc':10,'pqr':20,'xyz':15}
y={'ijk':40,'xyz':20,'abc':12}
k1=set(x.keys())
k2=set(y.keys())
k3=k1.union(k2)
k4=list(k3)
k4.sort()
del k1
del k2
del k3
v=list()
for k in k4:
    if k in x and k in y:
        v.append(int(x[k])+int(y[k]))
    elif k in x:
        v.append(int(x[k]))
    else:
        v.append(int(y[k]))

res={k4[i]:v[i] for i in range(0,len(v)) }
print(res)
        
         
        
