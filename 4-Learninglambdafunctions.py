def cube(a,func):
    return a*func()
def sqr(a):
    return a*a
print(cube(10,lambda x:x*x))
