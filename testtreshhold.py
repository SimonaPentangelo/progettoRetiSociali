from cmath import inf
import time
import snap




def caso3(dizionario):
    chiave = list(dizionario.keys())[0]
    massimo= dizionario[chiave]["t"]/((dizionario[chiave]["degree"])*((dizionario[chiave]["degree"])+1))
    for chiavi in dizionario.keys():
        temporaneo= dizionario[chiavi]["t"]/((dizionario[chiavi]["degree"])*((dizionario[chiavi]["degree"])+1))
        if temporaneo>massimo:
            chiave=chiavi
            massimo=temporaneo
    return chiave



(G, Map)= snap.LoadEdgeListStr(snap.TUNGraph, "facebook_combined.txt", 0, 1, True)
informazioni_nodi={}
TSet=[]
flag_case1=False
flag_case2=False
eliminato=None
start_time = time.time()
for i in G.Nodes():
    temporaneo={"vicini":"","degree":"","t":""}
    lista=[]
    for b in range(0,i.GetDeg()):
        lista.append(i.GetNbrNId(b))
    temporaneo["vicini"]=lista
    temporaneo["degree"]=i.GetDeg()
    temporaneo["t"]=5
    informazioni_nodi[i.GetId()]=temporaneo

while len(informazioni_nodi.keys())!=0:
    for nodo in informazioni_nodi.keys():
        if (informazioni_nodi[nodo]["t"] == 0):
            flag_case1=True
            eliminato=nodo
            for vicino in informazioni_nodi[nodo]["vicini"]:
                informazioni_nodi[vicino]["t"]=informazioni_nodi[vicino]["t"] - 1 if informazioni_nodi[vicino]["t"] - 1 > 0 else 0
            break
    if not flag_case1:
        for nodo in informazioni_nodi.keys():
            if informazioni_nodi[nodo]["degree"] < informazioni_nodi[nodo]["t"]:
                eliminato=nodo
                flag_case2=True
                TSet.append(nodo)
                for vicino in informazioni_nodi[nodo]["vicini"]:
                    informazioni_nodi[vicino]["t"]=informazioni_nodi[vicino]["t"] - 1

                break
        if not flag_case2:
            eliminato=caso3(informazioni_nodi)

    for nodo in informazioni_nodi[eliminato]["vicini"]:
        
        informazioni_nodi[nodo]["degree"]=informazioni_nodi[nodo]["degree"]-1
        
        informazioni_nodi[nodo]["vicini"].remove(eliminato)
        
    
    informazioni_nodi.pop(eliminato)
    flag_case1=False
    flag_case2=False
print("--- %s seconds ---" % (time.time() - start_time))

print("insieme di Tset:{}".format(TSet))
print("lunghezza di Tset:{}".format(len(TSet)))





    

          
    
# qua ci vuole un while, dobbiao vvedere come svuotarlo ed iterarlo. 
    #if informazioni_nodi[nodo.GetId()]["t"]==0: #caso1
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
 