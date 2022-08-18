from cmath import inf
import random
import time
import snap
soglia=5
random.seed(42)
prob=0
media_risultati = 0 
media_tempo = 0
output_file_result = "differita_eterogenea_threshold.txt"

def update_globvar(input1, input2):
    global media_risultati    
    media_risultati += input1
    global media_tempo
    media_tempo += input2

def reset_globvar():
    global media_risultati    
    media_risultati = 0
    global media_tempo
    media_tempo = 0

def print_globvar():
    print(media_risultati)
    print(media_tempo)

def differita(G):
    for i in G.Edges():
        if random.random() < prob:
            G.DelEdge(i.GetSrcNId(),i.GetDstNId())

def staticthreshold():
    return soglia

def maggioranzathreshold(degree):
    return round(degree * (1/2))

def proportionalthreshold(degree):
    return round(degree * (1/5))

def randomthreshold():
    return random.randint(1,10)

def caso3(dizionario):
    chiave = list(dizionario.keys())[0]
    massimo= dizionario[chiave]["t"]/((dizionario[chiave]["degree"])*((dizionario[chiave]["degree"])+1))
    for chiavi in dizionario.keys():
        temporaneo= dizionario[chiavi]["t"]/((dizionario[chiavi]["degree"])*((dizionario[chiavi]["degree"])+1))
        if temporaneo>massimo:
            chiave=chiavi
            massimo=temporaneo
    return chiave

def compute(j, G):
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
        temporaneo["t"]=randomthreshold()
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
    if j == 9:
        f = open(output_file_result, 'a')
        f.write("Soglia: ")
        f.write(str(soglia))
        f.write("\n")
        f.write("Probabilità: ")
        f.write(str(prob))
        f.write("\n")
        f.write("Tempo (media): ")
        f.write(str(media_tempo/10))
        f.write("\n")
        f.write("Lunghezza di Tset (media): ")
        f.write(str(media_risultati/10))
        f.write("\n\n")
        f.close
        reset_globvar()
    else:
        update_globvar(len(TSet), time.time() - start_time)

for i in range(1, 11):
        soglia = i
        prob +=0.05
        #random.seed(i)
        (G, Map)= snap.LoadEdgeListStr(snap.TUNGraph, "facebook_combined.txt", 0, 1, True)
        differita(G)
        prob = round(prob, 2)
        for j in range(0, 10):
            compute(j, G)


    