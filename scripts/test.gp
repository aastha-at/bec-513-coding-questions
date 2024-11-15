set terminal postscript size 6,6 font 'Arial, 15'
set output "/home/aastha/bec-513-coding-questions/output/big_matrix.eps"

set xrange [0:2000]
set yrange [0:100000]

set palette defined (0 "white", 3 "red")
set cbrange [0:3]

plot '/home/aastha/bec-513-coding-questions/data/clean.tsv'  matrix with pm3d
