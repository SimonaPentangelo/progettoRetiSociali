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
    - [Informazioni dei nodi](#informazioni-dei-nodi)
    - [Inizializzazione dei threshold](#inizializzazione-dei-threshdold)
    - [Principio di decisione differita](#principio-di-decisione-differita)
    - [Algoritmo di Target Set Selection](#algoritmo-di-target-set-selection)
  - [Istruzioni per l'esecuzione](#istruzioni-per-lesecuzione)
  - [Risultati](#risultati)
    - [Threshold costante](#threshold-costante)
    - [Threshold eterogeneo](#threshold-eterogeneo)
    - [Threshold a maggioranza](#threshold-a-maggioranza)
    - [Threshold proporzionale al grado](#threshold-proporzionale-al-grado)
  - [Conclusioni](#conclusioni)
___
## Introduzione
Il problema del **Target Tes Selection (TSS)** consiste nel trovare, all'interno dei nodi di una rete, il più piccolo insieme di nodi i quali permettano di condizionare l'intera rete. Formalmente, dato un grafo G=(V, E), in cui per ogni vertice v, *d(v)* indica il grado del vertice e *t(v)* indica il threshold associato al vertice (ovvero, il numero minimo di adiacenti attivi di v necessari per attivare v), il suo target set S è un insieme di nodi tali che attiveranno l'intera rete, ovvero, per il quale si verifica Influenced[S, ℓ]=V, per qualche ℓ ≥ 0.

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

Per lavorare con il dataset disponibile su [SNAP](http://snap.stanford.edu/index.html), abbiamo utilizzato il linguaggio **Python** e il modulo [Snap.py](https://snap.stanford.edu/snappy/doc/reference/index-ref.html).

```python
(G, Map)= snap.LoadEdgeListStr(snap.TUNGraph, "facebook_combined.txt", 0, 1, True)
```

### Informazioni dei nodi 

Tramite il modulo **Snap.py**, abbiamo raccolto tutte le informazioni dei nodi. Abbiamo deciso di utilizzare un dizionario per poter accedere facilmente al grado, al threshold e all'insieme dei vicini di un determinato nodo. 

Per poter ottenere le informazioni desiderate, basta utilizzare il nodo di interesse come chiave.

```python
#Per ogni nodo del grafo
for i in G.Nodes():
        #dizionario con le informazioni dei nodi
        temporaneo={"vicini":"","degree":"","t":""}
        lista=[]
        #per ogni vicino del nodo corrente
        for b in range(0,i.GetDeg()):
            #crea la lista dei nodi adiacenti
            lista.append(i.GetNbrNId(b))
        temporaneo["vicini"]=lista
        temporaneo["degree"]=i.GetDeg()
        temporaneo["t"]=#inserire qui la funzione di threshold
        informazioni_nodi[i.GetId()]=temporaneo
```

### Inizializzazione dei threshold

Abbiamo deciso di utilizzare 10 configurazioni diverse:
  + Senza principio di decisione differita
    - Threshold deterministico: soglie da 1 a 10
    - Threshold eterogeneo: seed da 1 a 10
    - Threshold a maggioranza: gradi originali dei nodi
    - Threshold proporzionale al grado: gradi originali dei nodi
  + Con principio di decisione differita: probabilità da 0.05 a 0.5
    - Threshold deterministico: soglie da 1 a 10
    - Threshold eterogeneo: seed da 1 a 10
    - Threshold a maggioranza: gradi originali dei nodi
    - Threshold proporzionale al grado: gradi originali dei nodi

Per ogni configurazione, abbiamo fatto 10 esecuzioni dell'algoritmo e calcolato le medie dei risultati (tempo di esecuzione e dimensione del target set).

```python
for i in range(1, 11):
        soglia = i #da 1 a 10
        prob +=0.05 #da 0.05 a 0.5, incrementando di 0.05 alla volta
        #random.seed(i) da 1 a 10 in caso di threshold eterogeneo, altrimenti uguale a 42
        (G, Map)= snap.LoadEdgeListStr(snap.TUNGraph, "facebook_combined.txt", 0, 1, True)
        differita(G)
        prob = round(prob, 2)
        for j in range(0, 10):
            compute(j, G)
```

Qui di seguito sono state riportate tutte le funzioni utilizzate per inizializzare i threshold:

 - Threshold deterministico

    ```python
    def staticthreshold():
        return soglia #variabile globale
    ```
- Threshold eterogeneo

    ```python
    def randomthreshold():
        return random.randint(1,10)
    ```

- Threshold a maggioranza

    ```python
    def maggioranzathreshold(degree):
        return round(degree * (1/2))
    ```

- Threshold proporzionale al grado

    ```python
    def proportionalthreshold(degree):
        return round(degree * (1/5))
    ```

### Principio di decisione differita

### Algoritmo di Target Set Selection 

___
## Istruzioni per l'esecuzione  

Durante l'esecuzione, verrà generato un file nel formato **[numeroBodies]inFile.txt** per visualizzare i body generati, mentre al termine verrà stampato il tempo impegato per le iterazioni sui body e verrà generato un file  **[numeroBodies]outFile.txt** per visualizzare i valori aggiornati dei bodies.
___   

### Risultati

*File di input - np = 1*             |  *File di output - np = 1*
:-------------------------:|:-------------------------:
![inFile](risultati/10infile1proc.png)  |  ![outFile](risultati/10outfile1proc.png)

*File di input - np = 2*             |  *File di output - np = 2*
:-------------------------:|:-------------------------:
![inFile](risultati/10infile2proc.png)  |  ![outFile](risultati/10outfile2proc.png)

*File di input - np = 5*             |  *File di output - np = 5*
:-------------------------:|:-------------------------:
![inFile](risultati/10infile5proc.png)  |  ![outFile](risultati/10outfile5proc.png)


___  

## Benchmarks  

Per osservare strong e weak scaling dell'algoritmo parallelo, è stato utilizzato un cluster di **t2.xlarge**.  
Per valutare lo strong scaling, sono state utilizzate fino a 4 istanze (utilizzando quindi da 1 a 16 core) e sono stati fatti due test utilizzando un numero di elementi differenti (20000 e 30000).  
Per valutare il weak scaling, sono state usate 4 istanze, facendo in modo che ogni core dovesse lavorare su 2000 bodies (quindi partendo da un core con 2000 elementi fino a 16 core con 32000 body).

### Strong Scaling con 20000 body  

| vCPUs | 1 | 2 | 4 | 6 | 8 | 10 | 12 | 14 | 16 |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| Tempo | 78,53 | 39,28 | 19,65 | 14,66 | 11,19 | 8,93 | 7,51 | 6,42 | 5,67 |
| Efficienza | 100,00% | 99,92% | 99,84% | 89,04% | 89,30% | 88,47% | 89,04% | 85,79% | 87,00% |  

*Tempo medio di esecuzione (in secondi)*           |  *Efficienza (in percentuale)*
:-------------------------:|:-------------------------:
![StrongScaling](grafici/strongScaling20000.png)  |  ![StrongScaling](grafici/strongScaling20000(1).png)  

  
 ### Strong Scaling con 30000 body  

| vCPUs | 1 | 2 | 4 | 6 | 8 | 10 | 12 | 14 | 16 |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| Tempo | 176,70 | 88,42 | 44,24 | 33,08 | 24,73 | 19,97 | 16,76 | 14,71 | 12,69 |
| Efficienza | 100,00% | 99,92% | 99,84% | 89,04% | 89,30% | 88,47% | 89,04% | 85,79% | 87,00% |  

*Tempo medio di esecuzione (in secondi)*           |  *Efficienza (in percentuale)*
:-------------------------:|:-------------------------:
![StrongScaling](grafici/strongScaling30000.png)  |  ![StrongScaling](grafici/strongScaling30000(1).png) 
  

### Weak Scaling  

| vCPUs | 1 | 2 | 4 | 6 | 8 | 10 | 12 | 14 | 16 |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| Tempo | 0,79 | 1,57 | 3,15 | 4,75 | 6,34 | 7,94 | 9,53 | 11,10 | 12,70 |
| Efficienza | 100,00% | 50,03% | 24,97% | 16,58% | 12,42% | 9,91% | 8,26% | 7,09% | 6,19% |
  

*Tempo medio di esecuzione (in secondi)*           |  *Efficienza (in percentuale)*
:-------------------------:|:-------------------------:
![WeakScaling](grafici/weakscaling1.png)  |  ![WeakScaling](grafici/weakscaling2.png) 
___  

## Conclusioni  

Come è possibile osservare dai grafici e dai valori ottenuti, l'algoritmo presenta buoni valori in termini di efficienza, mantenendosi circa sul 99% per due e quattro vCPUs e scendendo solo fino all'85% circa con quattordici core,  e di tempo di esecuzione,  ottenendo una buona riduzione nel tempo di esecuzione nel momento in cui vengono utilizzati 2 core e mostrando un continuo decremento al crescere delle vCPUs (seppur man mano sempre minore), per quanto riguarda la strong scalability.
Per quanto riguarda invece la weak scalability, i risultati non sono molto soddisfacenti, in quanto vi è una crescita costante in termini di tempo di esecuzione e un calo delle performance non indifferente: nel passare a 2 vCPUs con 40000 bodies, il calo è del 50% circa, mentre al crescere dei core (e dei bodies di conseguenza) la distanza tra le percentuali ottenute risulta essere sempre minore.
___