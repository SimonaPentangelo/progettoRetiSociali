import snap
from random import Random, random
(G, Map)= snap.LoadEdgeListStr(snap.TUNGraph, "facebook_combined.txt", 0, 1, True)
prob=0.7
for i in G.Edges():
    if Random.random < prob:
        G.DelEdge(i.GetSrcNId(),i.GetDstNId())
    
    print(i.GetDstNId())