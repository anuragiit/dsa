from pythonds import *
a=Stack()
for x in range(1,11):
    a.push(x)

print(a.items)
a.pop()
print(a.items)
print(a.isEmpty())
help(Stack)
print(a.size())
b=a.peek()
print(b)
print(a.peek())
a.pop()
print(a.items)
print(type(a.items))
print(a.__str__())
print(a)
print(a.__hash__())

