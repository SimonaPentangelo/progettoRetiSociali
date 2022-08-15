import snap

(G, Map)= snap.LoadEdgeListStr(snap.TUNGraph, "facebook_combined.txt", 0, 1, True)
informazioni_nodi={}
for i in G.Nodes():
    temporaneo={"vicini":"","degree":"","t":""}
    lista=[]
    for b in range(0,i.GetDeg()):
        lista.append(i.GetNbrNId(b))
    temporaneo["vicini"]=lista
    temporaneo["degree"]=i.GetDeg()
    temporaneo["t"]=0.50
    informazioni_nodi[i.GetId()]=temporaneo
# qua ci vuole un while, dobbiao vvedere come svuotarlo ed iterarlo. 
    if informazioni_nodi[nodo.GetId()]["t"]==0.00: #caso1
        ##se il treshold del nodo è uguale a 0 allora il nodo
        ## può essere attivato solo dai vicini. Dopo può influzneare i vicini non attivi.
        ## per ogni nodo nei vicini del nodo selezionato il treshold dei vicini
        ## è uguale a al massimo di k(u) - 1. 
        ## altrimenti: caso 2
        ### se esiste un nodo il quale degree sia minore del treshold allora
        ### il vertice è aggiunto ad set S poichè non rimangono vicini per attivarlo. 
        ### per ogni nodo vicino del nodo selezionato si abbassa la soglia di 1. 
        ### altrimenti si prende il nodo il cui valore massimo della formula e si rimuove. 
        ###  si dimuinsice di 1 il treshold e si rimuove il nodo. 
 