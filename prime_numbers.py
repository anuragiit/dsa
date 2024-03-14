import math as m
'''def is_prime(a,l):
    for x in l:
         if a%x==0:
            print('Not a Prime number')
            break
         else:
             i=1
             while i*x<=l[len(l)-1]:
                 l.remove(i*x)
                 i=i+1
             if len(l):      
                is_prime(a,l)
                break
             else:
                 print('Prime Number')
                 break
is_prime(a,l)                
  '''
def is_prime(a,l):
    if a in [2,3]:
        print('Prime number')
        return None
    for x in l:
        if a%x==0:
            print('Not a prime number')
            break
        else:
            l=list(filter(lambda i: i%x!=0,l))
            if len(l):
               is_prime(a,l)
               break
            else:
                print('Prime number')
                break
while True:
    
   a=int(input('Enter any number'))
   l=[x for x in range(2,int(m.sqrt(a))+1)]            
   is_prime(a,l)            
            
            
         




