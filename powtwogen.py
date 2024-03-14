def powtwogen(max=0):
    n=0
    while(n<=max):
      yield 2**n
      n=n+1
for a in powtwogen(5):
    print(a)
