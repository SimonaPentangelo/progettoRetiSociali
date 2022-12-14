from cmath import inf
import random
import time
import snap
from tqdm import tqdm
soglia=5
random.seed(42)
prob=0
media_risultati = 0 
media_tempo = 0
output_file_result = "Prop_nondiff.txt"
(G, Map)= snap.LoadEdgeListStr(snap.TUNGraph, "facebook_combined.txt", 0, 1, True)

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
    return round(degree * (1/(2+staticthreshold())))

def randomthreshold():
    return random.randint(1,10)

'''def caso3(dizionario):
    chiave = list(dizionario.keys())[0]
    massimo= dizionario[chiave]["t"]/((dizionario[chiave]["degree"])*((dizionario[chiave]["degree"])+1))
    for chiavi in dizionario.keys():
        temporaneo= dizionario[chiavi]["t"]/((dizionario[chiavi]["degree"])*((dizionario[chiavi]["degree"])+1))
        if temporaneo>massimo:
            chiave=chiavi
            massimo=temporaneo
    return chiave'''

def caso3(G, dizionario):
    chiave = -1
    massimo = -1
    for chiavi in G.Nodes():
        temporaneo = dizionario[chiavi.GetId()]["t"]/((dizionario[chiavi.GetId()]["degree"])*((dizionario[chiavi.GetId()]["degree"])+1))
        if temporaneo>massimo:
            chiave=chiavi.GetId()
            massimo=temporaneo
    return chiave

def compute(G,j):
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
        temporaneo["t"]=proportionalthreshold(i.GetDeg())
        informazioni_nodi[i.GetId()]=temporaneo

    while G.GetNodes() !=0:
        for nodo in tqdm(G.Nodes()):
            if (informazioni_nodi[nodo.GetId()]["t"] == 0):
                flag_case1=True
                eliminato=nodo.GetId()
                for vicino in informazioni_nodi[nodo.GetId()]["vicini"]:
                    informazioni_nodi[vicino]["t"]=informazioni_nodi[vicino]["t"] - 1 if informazioni_nodi[vicino]["t"] - 1 > 0 else 0
                for nodo in informazioni_nodi[eliminato]["vicini"]:
                    informazioni_nodi[nodo]["degree"]=informazioni_nodi[nodo]["degree"]-1
                    informazioni_nodi[nodo]["vicini"].remove(eliminato)
                informazioni_nodi.pop(eliminato)
                G.DelNode(eliminato)

            if not flag_case1:
                if informazioni_nodi[nodo.GetId()]["degree"] < informazioni_nodi[nodo.GetId()]["t"]:
                    eliminato=nodo.GetId()
                    TSet.append(nodo.GetId())
                    for vicino in informazioni_nodi[nodo.GetId()]["vicini"]:
                        informazioni_nodi[vicino]["t"]=informazioni_nodi[vicino]["t"] - 1
                    for nodo in informazioni_nodi[eliminato]["vicini"]:
                        informazioni_nodi[nodo]["degree"]=informazioni_nodi[nodo]["degree"]-1
                        informazioni_nodi[nodo]["vicini"].remove(eliminato)
                    informazioni_nodi.pop(eliminato)
                    G.DelNode(eliminato)

            flag_case1=False      
      
        eliminato = caso3(G, informazioni_nodi)

        for nodo in informazioni_nodi[eliminato]["vicini"]:
            informazioni_nodi[nodo]["degree"]=informazioni_nodi[nodo]["degree"]-1
            informazioni_nodi[nodo]["vicini"].remove(eliminato)
            
        informazioni_nodi.pop(eliminato)
        G.DelNode(eliminato)
        flag_case1=False

    '''while len(informazioni_nodi.keys())!=0:
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
        flag_case2=False'''
    if j == 9:
        f = open(output_file_result, 'a')
        f.write("Soglia: ")
        f.write(str(soglia))
        f.write("\n")
        f.write("Probabilit??: ")
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
        print_globvar()
    if j == -1:
        f = open(output_file_result, 'a')
        f.write("Soglia: ")
        f.write(str(soglia))
        f.write("\n")
        f.write("Tempo: ")
        f.write(str(time.time() - start_time))
        f.write("\n")
        f.write("Lunghezza di Tset: ")
        f.write(str(len(TSet)))
        f.write("\n\n")
        f.close
    else:
        #print(len(TSet))
        update_globvar(len(TSet), time.time() - start_time)
        print_globvar()

''' TEST NON DIFFERITA'''
for j in range(0, 10):
    soglia = j+1
    compute(G,-1)

''' TEST DIFFERITA
for i in range(1, 11):
        prob += 0.05
        prob = round(prob, 2)
        for j in range(0, 10):
            soglia = j+1
            for k in range (0,10):
                differita(G)
                compute(G,k)
'''



    