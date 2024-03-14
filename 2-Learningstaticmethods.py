class X:
    a=1000
    def __init__(self,a):
        self.a=a
    @staticmethod
    def m1():
        print("In static method of X")
    def m2(self):
        self.a=5000
x1=X(4000)
x1.m2()
print(x1.a)
print(X.a)

        
