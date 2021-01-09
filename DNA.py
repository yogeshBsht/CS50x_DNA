# DNA
import pandas as pd

data = pd.read_csv("large.csv")
STRS = data.columns.values[1:]

dna = open("19.txt", "r")
seq = dna.readline()
dna.close()

str_list = []
for strs in STRS:
    i = max_count = count = 0
    while i<len(seq):
        if strs == seq[i:len(strs)+i]:
            count += 1
            i += len(strs)
        else:
            max_count = max(count, max_count)
            count = 0
            i += 1
    str_list.append(max_count)        

match = None
for i in range(0, data.shape[0]):
    if all(data.iloc[i,1:].values - str_list == 0):
        match = data.iloc[i,0]
        break
                 
if match:
    print(match)
else:
    print("No match")