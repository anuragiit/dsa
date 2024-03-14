class X:
    def __init__(a,l):  # parameter name is 'a'   here instead of 'self'   then also it is working
        a.v=l
        print(a.v)
        
    def m1(c,b):            # parameter name is 'c' here instead of not only  'self' ,,'a'  also is not here,,   then also it is working!!its WONDER
        print("in m1 of X")
        c.v=b
        print(c.v)

x1=X(123)
x1.m1(456)
x2=X(123)
X.m1(x1,123)
