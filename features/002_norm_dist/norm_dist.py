#!/Users/guoli/anaconda2/bin/python
from nltk.corpus import stopwords
import pandas as pd
import string
import numpy as np
import numpy.linalg as LA
from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer("english")

def sentence2list(s,stem=True):
    s = s.decode('unicode_escape').encode('ascii','ignore')
    words = s.translate(None,string.punctuation).lower().split()
    if stem:
        return [stemmer.stem(word) for word in words if word not in stopwords.words('english')]
    else:
        return [word for word in words if word not in stopwords.words('english')]

def words2vec(words,keys):
    d = dict.fromkeys(keys,0)
    for word in words: 
        d[word] += 1
    return np.array(d.values())

def norm_dist(s1,s2,stem=True):
    """
    """
    words1 = sentence2list(s1,stem)
    words2 = sentence2list(s2,stem)
    keys = sorted(list(set(words1+words2)))
    v1 = words2vec(words1,keys)
    v2 = words2vec(words2,keys)
    return LA.norm(v1/LA.norm(v1)-v2/LA.norm(v2))
