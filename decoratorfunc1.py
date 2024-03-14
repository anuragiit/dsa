def smart_divide(func):
    def inner(a,b):
        print("I am going to divide",a,"and",b)
        
        if(b==0):
            print("sorry can't divide")
        else:
           func(a,b)
    return inner
@smart_divide
def divide(a,b):
    print(a/b)
divide(10,0)
divide(100,50)
        
