import sys
import pandas as pd

numbers=[int(line.strip()) for line in sys.stdin]
num_quantiles=int(sys.argv[1])

quantiles, bins=pd.qcut(numbers, num_quantiles, labels=['q' + str(i+1) for i in range(num_quantiles)], retbins=True)

for i in range(len(numbers)):
    number=numbers[i]
    quantile=quantiles[i]
    
    index=quantiles.categories.tolist().index(quantile)
    start=bins[index]
    end=bins[index+1]
    
    print(str(number)+'\t'+str(quantile)+'\t'+str(quantile)+' ('+str(start)+', '+str(end)+']')

