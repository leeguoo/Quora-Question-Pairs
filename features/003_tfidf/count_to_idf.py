#!/Users/guoli/anaconda2/bin/python
import string
import pylab as plt
import numpy as np
import pandas as pd
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
from collections import Counter
import itertools
import json

f = open("corpus_allwords_stem_stops.json","r")
data = json.load(f)
f.close()

ndata = {}
for k in data.keys():
    if data[k]>1:
        ndata[k] = 1/np.log(data[k])

f = open("idf_allwords_stem_stops.json","w")
json.dump(ndata,f)
