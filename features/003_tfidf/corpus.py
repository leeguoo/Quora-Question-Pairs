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
    s = s.replace('\\','.').decode('unicode_escape').encode('ascii','ignore')
    words = s.translate(None,string.punctuation).lower().split()
    if stem:
        return [stemmer.stem(word) for word in words if word not in stopwords.words('english')]
    else:
        return [word for word in words if word not in stopwords.words('english')]

path = "/Users/guoli/Desktop/kaggle/quora/input/"
train = pd.read_csv(path+"train.csv",sep='",')

vs2l = np.vectorize(sentence2list)

corpus = []
print '--'
#corpus += train.question1.apply(vs2l).apply(lambda x: list(x)).tolist()
print '=='
corpus += train.question2.apply(vs2l).apply(lambda x: list(x)).tolist()
print '**'
corpus = list(itertools.chain(*corpus))
print '>>'
corpus_dict = Counter(corpus)

f = open("corpus_allwords_stem_stops.json","w")
json.dump(corpus_dict,f)
f.close()
