#
# PrefAttach(100000, 3) in Degree. G(100000, 299994). 28500 (0.2850) nodes with in-deg > avg deg (6.0), 7650 (0.0765) with >2*avg.deg (Thu Aug 11 18:17:27 2022)
#

set title "PrefAttach(100000, 3) in Degree. G(100000, 299994). 28500 (0.2850) nodes with in-deg > avg deg (6.0), 7650 (0.0765) with >2*avg.deg"
set key bottom right
set logscale xy 10
set format x "10^{%L}"
set mxtics 10
set format y "10^{%L}"
set mytics 10
set grid
set xlabel "In-degree"
set ylabel "Count"
set tics scale 2
set terminal png font arial 10 size 1000,800
set output 'inDeg.pref-attach.png'
plot 	"inDeg.pref-attach.tab" using 1:2 title "" with linespoints pt 6
