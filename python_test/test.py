import snap
(G, Map)= snap.LoadEdgeListStr(snap.TUNGraph, "facebook_combined.txt", 0, 1, True)
for vicino in G.Nodes():
    for x in (vicino.GetOutEdges()):
        print(x)
        print(vicino.GetOutDeg())
        break
    break
G.DelNode(1)
for vicino in G.Nodes():
    for x in (vicino.GetOutEdges()):
        print(x)
        print(vicino.GetOutDeg())
        break
    break
