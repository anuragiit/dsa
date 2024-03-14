from pythonds import *
c=Deque()
print(c.isEmpty())
for x in range(1,6):
    c.addRear(x)
print(c.items)
for x in range(6,11):
    c.addFront(x)
print(c.items)
c.removeFront()
print(c.items)
c.removeFront()
print(c.items)
c.removeRear()
print(c.items)
c.removeRear()
print(c.items)
print(c.isEmpty())
print(c.size())
