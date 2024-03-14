def func(a):
    print('inside1',l,id(l))
    l[0]=23
    print('inside2',l,id(l))
l=[1,2,3]
func(l)
print('outside1',l,id(l))
print('outside2',l,id(l))

'''c=10
def func(a):
    global c
    if c==0:
        return 0
    else:    
     print(id(a))
     c-=1
     a=a+func(a)
     print(id(a),a)
     return a
    

a=19
print(a,id(a))
r=func(a)
print(r)     
'''
