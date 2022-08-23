
from cProfile import label
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure
from matplotlib import pylab


figure(figsize=(10, 20), dpi=80)

valore=[6.6,99.4,222.6,356.9,501.2,652.1,809.5,968.6,1132.2,1293.6]
val_propr_diff=[221.6,54.6,3.8,0.0]

#assex=np.array(range(1,11))
assex=[0.05,0.1,0.15,0.20,0.25,0.30,0.35,0.40,0.45,0.50]
#[520.4,514.3,503.9,496.1,488.3,485.9,477.1,470.1,464.5,459.5] differita maggioranza
#[90.1,68.7,64.4,39.7,35.8,32.5,29.3,26.2,20.1,24.1] proprozionale diff
#[407.0,436.3,464.9,479.0,505.2,536.3,559.4,582.5,605.1,647.1] random diff
#[6.6,99.4,222.6,356.9,501.2,652.1,809.5,968.6,1132.2,1293.6]static diff

#[3, 87, 206, 320, 426, 540, 665, 764, 873, 967] statico non diff

#[0.05,0.1,0.15,0.20,0.25,0.30,0.35,0.40,0.45,0.50] prob
#[385.9, 388.0, 387.6, 387.5, 383.4, 386.1, 388.8, 383.3, 388.3, 387.6]etero non diff
#[404.3,431.8,454.1,489.4,507.8, 529.1, 563.8, 591.5, 609.3, 644.0]etero diff

plt.plot(assex,valore, '--bo', label='Differita Statica')
#plt.xticks([0.05,0.1,0.15,0.20,0.25,0.30,0.35,0.40,0.45,0.50])
plt.xticks(assex)
plt.yticks(valore)
#plt.tick_params(axis='y', direction='out',labelsize=8)
#plt.yticks(rotation=45)
#ax = plt.gca()
#ax.set_ylim([11.0, 97.0])

plt.legend()
plt.show()