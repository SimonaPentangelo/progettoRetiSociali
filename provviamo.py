import snap

(G, Map)= snap.LoadEdgeListStr(snap.TUNGraph, "facebook_combined.txt", 0, 1, True)
labels = {}
for NI in G.Nodes():
    labels[NI.GetId()] = str(NI.GetId())
G.DrawGViz(snap.gvlDot, "output.png", " ", labels)
print("Number of Nodes: %d" % G.GetNodes())
# convert input string to node id
NodeId = Map.GetKeyId("1065")
# convert node id to input string
NodeName = Map.GetKey(NodeId)
print("name", NodeName)
print("id  ", NodeId)
#degrees = G.GetDegSeqV()
#for i in range(0, degrees.Len()):
#    print("Node %s has degree %s" % (i, degrees[i]))

