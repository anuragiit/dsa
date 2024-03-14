from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
        self.visited=defaultdict(bool)
        self.cycle=False
    def addedge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

def BFS(g,s):
    for k in g.graph.keys():
        g.visited[k]=False
    queue=[]
    queue.append(s)
    g.visited[s]=True
    while queue:
        s=queue.pop(0)
        print(s)
        for i in g.graph[s]:
            if not g.visited[i]:
                queue.append(i)
                g.visited[i]=True

def DFS(g,s):
    for k in g.graph.keys():
        g.visited[k]=False
    stack=[]
    stack.append(s)
    g.visited[s]=True
    while stack:
        s=stack.pop(-1)
        print(s)
        for i in g.graph[s]:
            if not g.visited[i]:
                stack.append(i)
                g.visited[i]=True
            else:
                g.cycle=True
                
def contains_cycle(g):
    if g.cycle==True:
        print('Graph contains cycle')
    else:
        print('Graph doesnot contain any cycle')


def distance(g,u,v):  # function for calculating minimum distance between two vertices in an undirected unweighted graph
    for k in g.graph.keys():
        g.visited[k]=False
    queue=[]
    queue.append((u,0))
    g.visited[u]=True
    while queue:
        s=queue.pop(0)
        for i in g.graph[s[0]]:
            if not g.visited[i]:
                queue.append((i,s[1]+1))
                if i==v:
                    return s[1]+1
                g.visited[i]=True    
        
    
            
            
                
'''g=Graph()
g.addedge(2,1)
g.addedge(2,3)
g.addedge(7,6)
g.addedge(5,6)
g.addedge(1,0)
g.addedge(0,7)
g.addedge(3,4)
g.addedge(5,4)
g.addedge(7,8)
g.addedge(2,5)
g.addedge(8,2)
g.addedge(8,6)
g.addedge(3,5)
DFS(g,1)
contains_cycle(g)
g2=Graph()
g2.addedge(1,2)
g2.addedge(1,3)
g2.addedge(2,4)
g2.addedge(2,5)
g2.addedge(3,6)
g2.addedge(3,7)
DFS(g2,1)
contains_cycle(g2)
'''
g=Graph()
g.addedge(0,1)
g.addedge(1,2)
g.addedge(2,3)
g.addedge(3,4)
g.addedge(4,5)
g.addedge(5,6)
a=distance(g,0,5)
print(a)


    
    
    
        
