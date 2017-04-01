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

stemmer = SnowballStemmer("english")
def sentence2list(s,stem=True):
#    s = s.decode('unicode_escape').encode('ascii','ignore')
    words = s.translate(None,string.punctuation).lower().split()
    if stem:
        return [stemmer.stem(word) for word in words if word not in stopwords.words('english')]
    else:
        return [word for word in words if word not in stopwords.words('english')]

f = open("../../input/train.csv","r")
lines = f.readlines()
f.close()

corpus = []
for line in lines[1:]:
    items = line.split(',')
    corpus += sentence2list(items[3])
    corpus += sentence2list(items[4])

f = open("../../input/test.csv","r")
lines = f.readlines()
f.close()
for line in lines[1:]:
    items = line.split(',')
    corpus += sentence2list(items[1])
    corpus += sentence2list(items[2])

corpus_dict = Counter(corpus)

f = open("corpus_allwords_stem_stops.json","w")
json.dump(corpus_dict,f)
f.close()
