
from cProfile import label
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure
from matplotlib import pylab


figure(figsize=(10, 40), dpi=80)

#nondiffstatic valore=[3,87,206,320,426,540,665,764,873,967]
#nondiff etero valore= [443,432,423,434,442,428,430,402,449,432]
#nondiff prop 
#valore1=[619,291,183,134,100,80,66,56,50,46,37]
#diff prop 
#diffstatic valore1=[11.0, 95.2, 210.3, 320.0, 426.8, 541.6, 652.5, 761.6, 860.6, 956.5] valore2=[18.5, 115.9, 239.1, 358.1, 476.5, 597.3, 718.5, 827.4, 940.1, 1044.2] valore3=[27.2, 134.9, 268.1, 396.1, 520.7, 654.4, 783.7, 896.8, 1023.3, 1135.5] valore4=[36.1, 164.0, 297.3, 435.9, 574.2, 704.8, 844.7, 971.8, 1090.1, 1207.6] valore5=[44.3, 182.2, 322.2, 479.3, 622.2, 769.6, 905.0, 1044.5, 1167.2, 1294.6]
#diffetero valore1=[439.2,433.0,441.3,438.8,434.1,431.3,428.4,434.2,436.1,438.2] valore2=[480.9,489.6,483.2,485.5,486.2,498.1,487.6,480.4,485.3,478.0]valore3=[535.5,534.2,535.1,539.1,534.4,539.8,530.9,530.6,531.9,539.9]valore4=[582.3,593.5,593.0,582.0,584.3,587.6,588.2,581.7,582.2,576.4]valore5=[643.2,638.8,631.5,641.0,639.6,633.6,638.5,640.0,633.2,642.5]
assex= range(1,12)

'''Proporzionale differito'''
valore1=[536.1,250.2,157.3,113.5,84.0,67.8,56.6,48.0,41.3,35.9,32.3]
valore2=[522.9,240.1,151.4,105.4,79.2,62.8,51.7,43.9,38.4,33.3,31.8]
valore3=[509.9,233.0,142.3,100.5,75.9,59.7,49.0,40.9,35.6,32.0,30.1]
valore4=[497.0,223.4,139.2,94.3,71.2,57.2,47.1,39.6,34.3,29.9,26.5]
valore5=[493.5,215.6,136.8,94.8,68.8,54.0,43.8,37.6,34.0,30.1,25.9]

plt.plot(assex,valore1, '--bo', label='Probabilità a 0.1')
plt.plot(assex,valore2, '--ro', label='Probabilità a 0.2')
plt.plot(assex,valore3, '--go', label='Probabilità a 0.3')
plt.plot(assex,valore4, '--o',color="orange", label='Probabilità a 0.4')
plt.plot(assex,valore5, '--o',color="purple", label='Probabilità a 0.5')
plt.legend(bbox_to_anchor=(0.65, 0.80))


#plt.xticks([0.05,0.1,0.15,0.20,0.25,0.30,0.35,0.40,0.45,0.50])
plt.xticks(assex)
#plt.yticks(valore1)
plt.yticks([50,100,150,200,300,400,500,600])
#plt.tick_params(axis='y', direction='out',labelsize=8)
#plt.yticks(rotation=45)
#ax = plt.gca()
#ax.set_ylim([11.0, 97.0])

plt.legend()
plt.savefig("propdiff.png")
plt.show()
