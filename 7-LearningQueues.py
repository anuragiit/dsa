from pythonds import *
b=Queue()
for x in range(1,11):
    b.enqueue(x)
print(b.items)
b.dequeue()
b.dequeue()
print(b.items)

print(b.__weakref__)
print(b.__dict__)
l=b.items
print(l[b.size()-1]) # for printting element at front
