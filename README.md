# Question 1
The list of patterns that need to be pulled are stored in a set for easy lookups. 
I read the q1_data.tsv.gz as standard input and if the current line has any pattern present in the set, the line is printed to the output.
Note: I checked the entire line as the pattern is not restricted to only the 2nd column.
```
zcat  ../data/q1_data.tsv.gz | python code1.py > ../output/lines.tsv
```

# Question 2
The aim was to plot x and y for different categories. The file was read as standard input and column names were assigned (x, y and group). ggplot2 was used to plot the lines with different color representing the different categories depending on the "group". Using the labels and titles as arguments allows us to customise the ouput.
```
cat ../data/q2_data.tsv | Rscript code2.R "../output/different_clusters.png" "Relative from center [bp]" "Enrichment over Mean" "MNase fragment profile"
```

# Question 3
This R script takes a list of file paths as standard input. It reads the first file and stores it in final. Then, it goes through the other files one by one and combines them with final based on the first column. The final merged file is printed.
Note: Update the path in the list_q3.tsv as per your system.
```
Rscript code3.R ../data/list_q3.tsv > ../output/join_output.tsv
```
# Question 4
The aim of this code was to convert a numerical data into a categorial one. The list of numbers is read as standard input and the qcut function directly callculates the distribution of quantiles depending on the number of quantiles provided as argument and the range of numbers in standard input the retbins provides us with both labels and edges (interval). For each number in the input, the number, quantile and its range is printed.
```
cat ../data/q4_data.tsv | python code4.py 4 > ../output/quantiles.tsv
```

# Question 5
The aim of this question was to plot a heatmap of bigdata. As the 1st column was an identifier, I cleaned the input file to remove this column.
```
zcat big_data.tsv.gz | cut -f2- > clean.tsv
```
Now this file is compatible with gnuplot and a heatmap was generated with color palette ranging from 0 (white) to 3 (red) having dimensions 100000*2000.
```
gnuplot code5.gp
```
The output was saved as an postscript file (eps format). To convert it into pdf format we used ps2pdf.
```
ps2pdf big_matrix.eps
```
