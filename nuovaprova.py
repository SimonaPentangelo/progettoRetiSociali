from cmath import inf
import graphlib
import random
import time
import snap
from tqdm import tqdm
thold = []
soglia = 0

def staticthreshold():
    return soglia

def targetsetsel(graph, node_threshold_mapping):
    S = set()
    active_ready_set = set()
    while graph.GetNodes() > 0:
        max_node_id = -1
        max_ratio_value = -1
        node_id_to_add_to_ts = None

        for v in graph.Nodes():
            #CASE 1:if exists a node with threshold == 0 it is already active so It influences other nodes in its neighbourhood
            #and then delete it from the network 
            if node_threshold_mapping[v.GetId()] == 0: 
                active_ready_set.add(v.GetId())
            else:
                if v.GetDeg() < node_threshold_mapping[v.GetId()]:
                    #CASE 2:it exists a node that has the degree < of its threshold
                    #so add it to the target set S because having a few link nobody can influence it
                    #and then delete it from the network 
                    node_id_to_add_to_ts = v.GetId()
                else:
                    #CASE 3:pick a nod v with the selected criteria, decrement of 1 its threshold neighborhoods
                    #and then delete it from the network
                    denominator = v.GetDeg()*(v.GetDeg()+1)
                    if denominator == 0: ratio = 0
                    else: ratio = node_threshold_mapping[v.GetId()] / denominator
                    if ratio > max_ratio_value:
                        max_node_id = v.GetId()
                        max_ratio_value = ratio

        #update thresholds and node delete
        if(len(active_ready_set) > 0):
            while(len(active_ready_set) > 0):
                node_id = active_ready_set.pop()
                _,NodeVec = graph.GetNodesAtHop(node_id, 1, False) #get node's neighborhood
                for item in NodeVec:
                    #decrement of 1 the threshold of neighbors nodes still inactive
                    if node_threshold_mapping[item] > 0: node_threshold_mapping[item] -= 1

                graph.DelNode(node_id)

        else:
            if node_id_to_add_to_ts != None:
                S.add(node_id_to_add_to_ts)
                _,NodeVec = graph.GetNodesAtHop(node_id_to_add_to_ts, 1, False) #get node's neighborhood
                for item in NodeVec:
                    #decrement of 1 the threshold of neighbors nodes still inactive
                    if node_threshold_mapping[item] > 0: node_threshold_mapping[item] -= 1

                graph.DelNode(node_id_to_add_to_ts)
            else:
                graph.DelNode(max_node_id)

    return S

def iniziathold(G):
    print(len(thold))
    for nodo in G.Nodes():
        thold.append(staticthreshold())

#for j in range(0, 10):
(G, Map)= snap.LoadEdgeListStr(snap.TUNGraph, "facebook_combined.txt", 0, 1, True)
soglia = 9
iniziathold(G)
S = targetsetsel(G, thold)
print(len(S))
thold = []