import sys
import pandas as pd

numbers=[]
for line in sys.stdin:
    numbers.append(int(line.strip()))

num_quant=int(sys.argv[1])

quantiles, bins=pd.qcut(numbers,num_quant, labels=[str(i+1) for i in range(num_quant)], retbins=True)

for i in range(len(numbers)):
    number=numbers[i]
    quant=quantiles[i]
    index=int(quant)-1
    print(str(number)+"\t q"+str(quant)+"\t q"+str(quant)+" ("+str(bins[index])+", "+str(bins[index+1])+"]")

