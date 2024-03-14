from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
        self.cycle=False
        self.representative=defaultdict(int)
    def addedge(self,u,v,w):
        self.graph[u].append((v,w))
        self.representative[u]=-1
        self.representative[v]=-1
    def representative_of(self,u):
        if self.representative[u]==-1:
            return u
        else:
            return self.representative_of(self.representative[u])
    def take_union_of(self,u,v):
        if self.representative_of(u)!=self.representative_of(v):
            self.representative[self.representative_of(v)]=u
        else:
            self.cycle=True
def min_spanning_tree(a):
    b=Graph()
    l=list()
    spanned_edges=[]
    for u in a.graph:
        for v in a.graph[u]:
            l.append((v[1],v[0],u))
    sorted_edges=sorted(l)
    for t in sorted_edges:
        temp=a.representative[t[1]]
        a.take_union_of(t[2],t[1])
        if not a.cycle:
            b.graph[t[2]].append(t[1])
        else:
            a.representative[t[1]]=temp
            a.cycle=False
    for u in b.graph:
        for v in b.graph[u]:
            spanned_edges.append((u,v))
    return spanned_edges        
            
a=Graph()
a.addedge(0,1,4)
a.addedge(0,7,8)
a.addedge(4,3,9)
a.addedge(4,5,10)
a.addedge(8,2,2)
a.addedge(8,6,6)
a.addedge(3,5,14)
a.addedge(2,5,4)
a.addedge(8,7,7)
a.addedge(2,1,8)
a.addedge(2,3,7)
a.addedge(6,7,1)
a.addedge(6,5,2)
mst=min_spanning_tree(a)
print('Spanned tree contains following edges:')
print(mst)


