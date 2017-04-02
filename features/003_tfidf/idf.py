#!/Users/guoli/anaconda2/bin/python
import json
import numpy as np

f = open("corpus_allwords_stem_stops.json","r")
data = json.load(f)
f.close()

idf = {}
for k in data.keys():
    if data[k]>1:
        idf[k] = 1.0/np.log(data[k])
    else:
        idf[k] = 0.0

f = open("idf_allwords_stem_stops.json","w")
json.dump(idf,f)
f.close()
