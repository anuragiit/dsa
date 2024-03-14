 #1) Dijkshtra's algorithm fails for negative weight edges of graph
# 2) Time complexity for this SPT calculation is O(V^2) as we are appending one vertex in each
# cycle and in that each cycle we are finding minimum distance value in O(V) time
# 3)For graphs with negative weight edges, Bellman–Ford algorithm can be used
#4)The code is for undirected graph, same dijkstra function can be used for directed graphs also.
#5)Dijkshtra's algorithm is a greedy algorithm
import heapq
import sys
from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
        
    def addEdge(self,u,v,w):
        self.graph[u].append((v,w))
        self.graph[v].append((u,w))                                         
                                                                                                
    def spt(self,source):                                                         
        distance={}
        for i in self.graph:
            distance[i]=sys.maxsize
        heap=[(0,source)]
        distance[source]=0
        while len(heap):
            dist,ele=heapq.heappop(heap)
            if dist>distance[ele]:
                continue
            for neighbour,weight in self.graph[ele]:
                if weight+dist<distance[neighbour]:
                    heapq.heappush(heap,(weight+dist,neighbour))
                    distance[neighbour]=weight+dist
            
        return distance


a=Graph()
a.addEdge(0, 1, 4)
a.addEdge(0, 7, 8)
a.addEdge(1, 2, 8)
a.addEdge(1, 7, 11)
a.addEdge(2, 3, 7)
a.addEdge(2, 8, 2)
a.addEdge(2, 5, 4)
a.addEdge(3, 4, 9)
a.addEdge(3, 5, 14)
a.addEdge(4, 5, 10)
a.addEdge(5, 6, 2)
a.addEdge(6, 7, 1)
a.addEdge(6, 8, 6)
a.addEdge(7, 8, 7)
x=a.spt(0)
print(x)


