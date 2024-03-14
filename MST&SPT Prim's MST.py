import sys
from collections import defaultdict
import time
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
        
    def addEdge(self,u,v,w):
        self.graph[u].append((v,w))
        self.graph[v].append((u,w))                                         
                                                                                                
    def mst(self,source):                                                         
        distance={}
        mstset={}
        parent={}
        minspantree=[]
        for i in self.graph:
            distance[i]=sys.maxsize
        distance[source]=0
        parent[source]=-1
        while len(distance):
            min_key=None
            min_value=1000
            for i in distance:
                if distance[i]<=min_value:
                    min_key=i
                    min_value=distance[i]
            distance.pop(min_key)
            mstset[min_key]=min_value
            for k in self.graph[min_key]:
                if k[0] in distance and distance[k[0]]>k[1]:
                    distance[k[0]]=k[1]
                    parent[k[0]]=min_key
        for i in self.graph:
            if parent[i]!=-1:
                minspantree.append((i,parent[i]))
        return minspantree


a=Graph()
a.addEdge(0,1,4)
a.addEdge(0,7,8)
a.addEdge(1,2,8)
a.addEdge(2,3,7)
a.addEdge(3,4,9)
a.addEdge(4,5,10)
a.addEdge(5,6,2)
a.addEdge(6,7,1)
a.addEdge(7,1,11)
a.addEdge(3,5,14)
a.addEdge(2,8,2)
a.addEdge(8,6,6)
a.addEdge(2,5,4)
a.addEdge(7,8,7)
x=a.mst(0)
print('Minimum spanning Tree contains following edges \n',x)
