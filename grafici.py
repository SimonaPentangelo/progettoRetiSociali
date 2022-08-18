
from cProfile import label
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure
from matplotlib import pylab


figure(figsize=(10, 20), dpi=80)

valore=[385.9, 388.0, 387.6, 387.5, 383.4, 386.1, 388.8, 383.3, 388.3, 387.6]
assex=np.array(range(1,11))
#[513.0, 506.7, 505.8, 499.5, 486.9, 481.5, 476.1, 471.6, 468.0, 453.6] differita maggioranza
#[96.3,91.8,39.6,33.3,32.4,34.2,30.6,31.5,11.7,27.9] proprozionale diff
#[3, 87, 206, 320, 426, 540, 665, 764, 873, 967] statico non diff
#[0.05,0.1,0.15,0.20,0.25,0.30,0.35,0.40,0.45,0.50] prob
#[385.9, 388.0, 387.6, 387.5, 383.4, 386.1, 388.8, 383.3, 388.3, 387.6]etero

plt.plot(assex,valore, '--bo', label='funzione di treshold eterogenea, grafi non differiti')
#plt.xticks([0.05,0.1,0.15,0.20,0.25,0.30,0.35,0.40,0.45,0.50])
plt.xticks(assex)
plt.yticks(valore)
#plt.tick_params(axis='y', direction='out',labelsize=8)
#plt.yticks(rotation=45)
#ax = plt.gca()
#ax.set_ylim([11.0, 97.0])

plt.legend()
plt.show()