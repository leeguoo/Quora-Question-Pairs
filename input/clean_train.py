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

path = "/Users/guoli/Desktop/kaggle/quora/input/"
f = open(path+'train.csv','r')
lines = f.readlines()
f.close()

f = open("train.csv","w")
for line in lines:
    line = line.replace('\n','')
    line = line.replace('\r','\n')
    line = line.replace('\\','|')
    line = line.replace(',',";")
    line = line.replace('";','",')
    line = line.replace('"",','"";')
    line = line.replace('""";','""",')
    line = line.replace('",",','","')
    line = line.replace(',"";',',"",')
    line = line.decode('unicode_escape').encode('ascii','ignore')
    f.write(line)
f.close()

f = open("train.csv","r")
lines = f.readlines()
f.close()
for line in lines:
    if line.count(',') != 5:
        print line.count(','), line
