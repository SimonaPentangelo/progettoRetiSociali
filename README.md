# **Target Set Selection Problem**
Progetto di corso per l'esame di **Reti sociali 2021/22**.

- Studenti: **Gaetano Casillo**, **Simona Pentangelo**, **Gabriele Pisapia**
- Data di consegna: **-**  
___
## Sommario
- [**Target Set Seceltion**](#target-set-selection)
  - [Sommario](#sommario)
  - [Introduzione](#introduzione)
  - [Studio effettuato](#studio-effettuato)
  - [Dettagli implementativi](#dettagli-implementativi)
    - [Inizializzazione dei threshold](#inizializzazione-dei-threshdold)
    - [Principio di decisione differita](#principio-di-decisione-differita)
    - [Algoritmo di Target Set Selection](#algoritmo-di-target-set-selection)
  - [Risultati](#risultati)
    - [Threshold costante](#threshold-costante)
    - [Threshold eterogeneo](#threshold-eterogeneo)
    - [Threshold a maggioranza](#threshold-a-maggioranza)
    - [Threshold proporzionale al grado](#threshold-proporzionale-al-grado)
  - [Conclusioni](#conclusioni)
___
## Introduzione
Il problema del **Target Set Selection (TSS)** consiste nel trovare, all'interno dei nodi di una rete, il più piccolo insieme di nodi i quali permettano di condizionare l'intera rete. Formalmente, dato un grafo G=(V, E), in cui per ogni vertice v, *d(v)* indica il grado del vertice e *t(v)* indica il threshold associato al vertice (ovvero, il numero minimo di adiacenti attivi di v necessari per influenzare v), il suo target set S è un insieme di nodi tali che attiveranno l'intera rete, ovvero, per il quale si verifica Influenced[S, ℓ]=V, per qualche ℓ ≥ 0.

Il lavoro da noi svolto ha l'obiettivo di confrontare le dimensioni dei target set ottenuti sul dataset formato dalle [friend-list su Facebook](http://snap.stanford.edu/data/ego-Facebook.html) ed utilizzando l'algoritmo descritto nel paper [*Discovering Small Target Sets in Social Networks: A Fast and Effective Algorithm*](https://arxiv.org/abs/1610.03721).
___
## Studio effettuato
Abbiamo deciso di confrontare i target set ottenuti con diverse modalità di inizializzazione dei threshold:

 - *Costante (omogeneo)*
 - *Eterogeneo*
 - *A maggioranza*
 - *Proporzionale al grado*

Per ogni modalità, abbiamo eseguito prima l'algoritmo sul grafo originario, poi l'abbiamo eseguito sul grafo ottenuto utilizzando il *principio di decisione differita*, ovvero: per ogni arco del grafo viene generato un numero pseudocasuale compreso tra 0 e 1. 
Se il numero generato è minore della probabilità presente sull'arco (cioè il nodo infetta con una probabilità inferiore rispetto a quella richiesta), l'arco viene rimosso.
Il grafo così ottenuto viene dato in input all'algoritmo scelto, che calcola
l’insieme soluzione e lo restituisce in output.
___
## Dettagli implementativi 

Per lavorare con il dataset disponibile su [SNAP](http://snap.stanford.edu/index.html), abbiamo utilizzato il linguaggio **Python** e il modulo [Snap.py](https://snap.stanford.edu/snappy/doc/reference/index-ref.html), il quale ci ha permesso non solo di caricare il grafo, ma anche di accedere alle varie informazioni utili ai fini dell'algoritmo, come il degree dei nodi ed il neighborhood di un nodo.

```python
(G, Map) = snap.LoadEdgeListStr(snap.TUNGraph, "facebook_combined.txt", 0, 1, True)
```

### Inizializzazione dei threshold

Abbiamo deciso di eseguire l'algoritmo utilizzando diverse configurazioni per i threshold:
  + Senza principio di decisione differita
    - Threshold deterministico: soglie da 1 a 10
    - Threshold eterogeneo: seed = 42
    - Threshold a maggioranza: gradi originali dei nodi
    - Threshold proporzionale al grado: gradi originali dei nodi e con frazioni da 1/3 ad 1/11
  + Con principio di decisione differita: probabilità da 0.1 a 0.5
    - Threshold deterministico: soglie da 1 a 10
    - Threshold eterogeneo: seed = 42
    - Threshold a maggioranza: gradi del nuovo grafo
    - Threshold proporzionale al grado: gradi del nuovo grafo e con frazioni da 1/3 ad 1/11

Per quelli con principio di decisione differita, abbiamo eseguito 10 volte l'update del grafo e l'esecuzione dell'algoritmo. Una volta completate le 10 esecuzioni, è stata calcolata la relativa alla taglia del target set. Qui abbiamo riportato il codice utilizzato per invocare le funzioni per il TSS.

```python
''' TEST NON DIFFERITA'''
for j in range(0, 10):
    (G, Map)= snap.LoadEdgeListStr(snap.TUNGraph, "facebook_combined.txt", 0, 1, True)
    soglia = 1
    iniziathold(G) #Inizializzazione dei threshold
    targetsetsel(G)
    thold = []

''' TEST DIFFERITA'''
for i in range(0, 5):
        prob += 0.1
        prob = round(prob, 2)
        for j in range(0, 10):
            soglia = j + 1
            for k in range (0,10):
                differita(G) #Applicazione del principio di decisione differita
                iniziathold(G) #Inizializzazione dei threshold
                targetsetseldiff(G,k)
                thold = []

```

Qui di seguito è stata riportata la funzione utilizzata per salvare il threshold per ognuno dei nodi del grafo:

```python
def iniziathold(G):
    for nodo in G.Nodes():
        #Salvataggio della soglia per il nodo corrente
        thold.append('''chiamata a funzione di threshold di interesse''')
```

Tale funzione, effettua la chiamata ad una specifica funzione di threshold per ottenere il valore di soglia per il nodo corrente. 

 - Threshold deterministico
    
    La variabile `soglia` è globale, viene modificata ad ogni iterazione e la funzione restituisce il valore dell'iterazione corrente.
    ```python
    def staticthreshold():
        return soglia #variabile globale
    ```
- Threshold eterogeneo
    
    Il seed utilizzato è 42.
    ```python
    def randomthreshold():
        return random.randint(1,10) #seed a 42
    ```

- Threshold a maggioranza

    ```python
    def maggioranzathreshold(degree):
        return round(degree * (1/2))
    ```

- Threshold proporzionale al grado

    ```python
    def proportionalthreshold(degree):
        return round(degree * (1/(2+staticthreshold()))) #da 1/3 ad 1/11
    ```

### Principio di decisione differita

Qui di seguito, l'algoritmo che abbiamo utilizzato per eliminare gli archi dal grafo tramite il principio di decisione differita: 

```python
def differita(G):
    for i in G.Edges():
      #Se all'i-esima iterazione il valore ottenuto è < prob
        if random.random() < prob:
          #l'arco i-esimo viene rimosso del grafo
            G.DelEdge(i.GetSrcNId(),i.GetDstNId())
```
La probabilità `prob` è una variabile globale che viene modificata prima delle 10 esecuzioni per ogni funzione di threshold. Inizialmente è 0.1, viene incrementata di 0.1 ogni volta fino a 0.5.

### Algoritmo di Target Set Selection 

Le funzioni `tergetsetsel(G)` e `tergetsetseldiff(G, k)` implementano l'algoritmo TSS. Una volta caricato il grafo, viene chiamata una delle due funzioni (la seconda nel caso in cui venga applicato il principio di decisione differita) e si itera per ogni nodo del grafo.

- Senza principio di decisione differita

    ```python
    def targetsetsel(G):
                targetset=[]
                while G.GetNodes() != 0:
                    eliminato = None
                    for nodo in tqdm(G.Nodes()):
                        if thold[nodo.GetId()] == 0: #CASO 1
                            for vicino in nodo.GetOutEdges():
                                thold[vicino] = thold[vicino] - 1 if thold[vicino] - 1 > 0 else 0 #Update delle soglie
                            eliminato = nodo.GetId()
                            G.DelNode(eliminato) #Eliminazione del nodo dal grafo
                        else:
                            if thold[nodo.GetId()] > nodo.GetOutDeg(): #CASO 2
                                targetset.append(nodo.GetId()) #Salvataggio nel target set
                                eliminato = nodo.GetId()
                                for vicino in nodo.GetOutEdges():
                                    thold[vicino] = thold[vicino] - 1 if thold[vicino] - 1 > 0 else 0 #Update delle soglie
                                G.DelNode(eliminato) #Eliminazione del nodo dal grafo
                    if eliminato == None:
                        eliminato = caso3(G)
                        G.DelNode(eliminato)
                #Salvataggio dei risultati
                f = open(output_file_result, 'a')
                f.write("Soglia: ")
                f.write(str(soglia))
                f.write("\n")
                f.write("Lunghezza di Tset: ")
                f.write(str(len(targetset)))
                f.write("\n\n")
                f.close
    ```

- Con principio di decisione differita

    ```python     
            def targetsetseldiff(G, k):
                targetset=[]
                while G.GetNodes() != 0:
                    eliminato = None
                    for nodo in tqdm(G.Nodes()):
                        if thold[nodo.GetId()] == 0: #CASO 1
                            for vicino in nodo.GetOutEdges():
                                thold[vicino] = thold[vicino] - 1 if thold[vicino] - 1 > 0 else 0 #Update delle soglie
                            eliminato = nodo.GetId()
                            G.DelNode(eliminato) #Eliminazione del nodo dal grafo
                        else:
                            if thold[nodo.GetId()] > nodo.GetOutDeg(): #CASO 2
                                targetset.append(nodo.GetId()) #Salvataggio nel target set
                                eliminato = nodo.GetId()
                                for vicino in nodo.GetOutEdges():
                                    thold[vicino] = thold[vicino] - 1 if thold[vicino] - 1 > 0 else 0 #Update delle soglie
                                G.DelNode(eliminato) #Eliminazione del nodo dal grafo
                    if eliminato == None:
                        eliminato = caso3(G) #CASO 3 (funzione apposita)
                        G.DelNode(eliminato) #Eliminazione del nodo dal grafo
                if k == 9: #Salvataggio dei risultati (dopo 10 iterazioni)
                    f = open(output_file_result, 'a')
                    f.write("Soglia: ")
                    f.write(str(soglia))
                    f.write("\n")
                    f.write("Prob: ")
                    f.write(str(prob))
                    f.write("\n")
                    f.write("Lunghezza di Tset (media): ")
                    f.write(str(media_risultati/10) #Calcolo della media
                    f.write("\n\n")
                    f.close
                else: #Salvataggio per calcolare la media (non ho ancora finito le 10 iterazioni)
                    update_globvar(len(targetset))
                    print_globvar()
    ```       

Nel caso 1, se il nodo corrente nel grafo ha soglia 0, la variabile `eliminato` viene aggiornata con il nodo selezionato, i vicini del nodo selezionato avranno il threshold decrementato di 1, se la soglia aggiornata dovesse essere negativa, viene impostata a 0 e infine il nodo `eliminato` viene cancellato dal grafo.
Nel caso 2, se il nodo corrente nel grafo **non** ha soglia 0 e proprio degree è minore del proprio threshold, la variabile `eliminato` viene aggiornata con il nodo selezionato. Tale nodo viene aggiunto al `targetset`, i vicini del nodo selezionato avranno il threshold decrementato di 1, se la soglia aggiornata dovesse essere negativa, viene impostata a 0 e infine il nodo `eliminato` viene cancellato dal grafo.

Per il caso 3, abbiamo utilizzato una funzione:

```python
def caso3(G):
    chiave = -1
    massimo = -1
    for chiavi in G.Nodes():
        #threshold / [ grado del nodo corrente * (grado del nodo corrente + 1) ]
        temporaneo = thold[chiavi.GetId()]/(chiavi.GetOutDeg() * (chiavi.GetOutDeg() + 1))
        if temporaneo > massimo: #Sostituzione del massimo
            chiave = chiavi.GetId()
            massimo = temporaneo
    return chiave #Restituzione del massimo
```

Una volta inizializzate le variabili `chiave` e `massimo`, itera per tutti i nodi presenti nel grafo, aggiornando le variabili qualora un nodo ottenga un valore maggiore come risultato della funzione *threshold/[degree\*(degree+1)*. Una volta completato il ciclo, viene restituito il nodo che ha ottenuto il risultato maggiore. 

Nel caso in cui utilizziamo il principio di decisione differita, è necessario fare le medie dei risultati ottenuti su 10 grafi diversi e poi scrivere i risultati su file.
Senza principio di decisione differita, i risultati ottenuti ad ogni singola iterazioni vengono scritti sul file.
___ 

## Risultati

### Threshold costante

*Senza principio di decisione differita*             |  *Con principio di decisione differita*
:-------------------------:|:-------------------------:
![nonDifferito](risultati/threshold_statica_nondifferiti.png)  |  ![differito](risultati/Differita_Statica.png)

| Soglie | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| Grafo non differito | 3 | 87 | 206 | 320 | 426 | 540 | 665 | 764 | 873 | 967 |

| Probabilità | 0.05 | 0.10 | 0.15 | 0.20 | 0.25 | 0.30 | 0.35 | 0.40 | 0.45 | 0.50 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Grafo differito | 7 | 99 | 223 | 357 | 501 | 652 | 810 | 969 | 1132 | 1294 |  

### Threshold eterogeneo

*Senza principio di decisione differita*             |  *Con principio di decisione differita*
:-------------------------:|:-------------------------:
![nonDifferito](risultati/treshold_eterogenea_nondifferiti.png)  |  ![differito](risultati/Differita_Random.png)

### Threshold a maggioranza

*Con principio di decisione differita* |
| :------------------------- |
![differito](risultati/Differita_Maggioranza.png) |

### Threshold proporzionale al grado

*Con principio di decisione differita* |
| :------------------------- |
![differito](risultati/Differita-Proporzionale.png) |

___  

## Conclusioni  


___