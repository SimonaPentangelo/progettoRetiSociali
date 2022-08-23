from cmath import inf
import graphlib
import random
import time
import snap
from tqdm import tqdm
soglia=5
random.seed(42)
prob=0

thold=[]
media_risultati = 0 
media_tempo = 0
output_file_result = "Prop_nondiff.txt"

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

def caso3(G):
    chiave = -1
    massimo = -1
    for chiavi in G.Nodes():
        temporaneo = thold[chiavi.GetId()]/((chiavi.GetOutDeg())*(chiavi.GetOutDeg()+1))
        if temporaneo>massimo:
            chiave=chiavi.GetId()
            massimo=temporaneo
    return chiave

def targetsetsel(G):
    targetset=[]
    while G.GetNodes() != 0:
        eliminato=None
        for nodo in tqdm(G.Nodes()):
            if thold[nodo.GetId()]==0:
                for vicino in nodo.GetOutEdges():
                    #print("Caso 1, pre nodo: " + str(vicino) + " thold: " +  str(thold[vicino]))
                    thold[vicino]=thold[vicino] - 1 if thold[vicino] - 1 > 0 else 0
                    #print("Caso 1, post nodo: " + str(vicino) + " thold: " +  str(thold[vicino]))
                eliminato=nodo.GetId()
            elif thold[nodo.GetId()] > nodo.GetOutDeg():
                targetset.append(nodo.GetId())
                eliminato=nodo.GetId()
                for vicino in nodo.GetOutEdges():
                    #print("Caso 2, pre nodo: " + str(vicino) + " thold: " + str(thold[vicino]))
                    thold[vicino]=thold[vicino] - 1 if thold[vicino] - 1 > 0 else 0
                    #print("Caso 2, post nodo: " + str(vicino) + " thold: " +  str(thold[vicino]))
        if eliminato == None:
            eliminato=caso3(G)
        G.DelNode(eliminato)
    f = open(output_file_result, 'a')
    f.write("Soglia: ")
    f.write(str(soglia))
    f.write("\n")
    f.write("Lunghezza di Tset: ")
    f.write(str(len(targetset)))
    f.write("\n\n")
    f.close

def iniziathold(G):
    print(len(thold))
    for nodo in G.Nodes():
        thold.append(staticthreshold())

''' TEST NON DIFFERITA'''
for j in range(0, 10):
    (G, Map)= snap.LoadEdgeListStr(snap.TUNGraph, "facebook_combined.txt", 0, 1, True)
    soglia = j+1
    iniziathold(G)
    targetsetsel(G)
    thold = []

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
    

