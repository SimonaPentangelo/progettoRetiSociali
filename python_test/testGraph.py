from cProfile import label
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure
from matplotlib import pylab


fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True,figsize=(10,10),dpi=80,gridspec_kw={'height_ratios':[1,10]})
fig.subplots_adjust(hspace=0.1)

value=[619,291,183,134,100,80,66,56,50,46,37]
x= range(1,12)

ax1.plot(x,value, '--bo', label='Proporzionale non differito')
ax2.plot(x,value, '--bo', label='Proporzionale non differito')
ax1.set_yticks(value)

ax2.set_yticks(value)
ax1.set_xticks(x)
ax1.set_ylim(600,640)  # outliers only
ax2.set_ylim(10,300)

ax1.spines.bottom.set_visible(False)
ax2.spines.top.set_visible(False)
ax1.xaxis.tick_top()
ax1.tick_params(labeltop=False)  # don't put tick labels at the top
ax2.xaxis.tick_bottom()
d = .5  # proportion of vertical to horizontal extent of the slanted line
kwargs = dict(marker=[(-1, -d), (1, d)], markersize=12,
              linestyle="none", color='k', mec='k', mew=1, clip_on=False)
ax1.plot([0, 1], [0, 0], transform=ax1.transAxes)
ax2.plot([0, 1], [1, 1], transform=ax2.transAxes)
plt.show()