from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
        self.cycle=False
        self.parent=defaultdict(int)
    def addedge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.parent[u]=-1
        self.parent[v]=-1
    def representative_of(self,u):
        if self.parent[u]==-1:
            return u
        else:
            return self.representative_of(self.parent[u])
    def take_union_of(self,u,v):
        if self.representative_of(u)!=self.representative_of(v):
            self.parent[self.representative_of(v)]=u
        else:
            self.cycle=True
            

a=Graph()
a.addedge(1,2)
a.addedge(1,3)
a.addedge(2,3)
a.addedge(2,4)
a.addedge(2,5)
a.addedge(3,6)
a.addedge(3,7)
a.addedge(4,8)
a.addedge(4,9)
a.addedge(5,10)
a.addedge(5,11)
for k in a.graph:
    for v in a.graph[k]:
        a.take_union_of(k,v)
if a.cycle:
    print('Graph contains cycle')
else:
    print('Graph doesnot contains cycle')

a=Graph()
a.addedge(1,2)
a.addedge(2,3)
a.addedge(3,4)
a.addedge(4,5)

for k in a.graph:
    for v in a.graph[k]:
        a.take_union_of(k,v)
if a.cycle:
    print('Graph contains cycle')
else:
    print('Graph doesnot contains cycle')


    


    
        
        
