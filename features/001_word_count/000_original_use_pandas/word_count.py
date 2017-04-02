#!/Users/guoli/anaconda2/bin/python
from nltk.corpus import stopwords
import pandas as pd
import string
from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer("english")

def sentence2set(s,stem=True):
#    s = s.decode('unicode_escape').encode('ascii','ignore')
    words = set(s.translate(None,string.punctuation).lower().split())
    if stem:
        return set([stemmer.stem(word) for word in words if word not in stopwords.words('english')])
    else:
        return set([word for word in words if word not in stopwords.words('english')])
    

def shared_word_count(s1,s2,stem=True):
    """
    Args:
       s1, s2 (str)
    Returns:
       The number of shared words over the total lengh of two sentences.
    """
    set1 = sentence2set(s1,stem)
    set2 = sentence2set(s2,stem)
    L = len(set1|set2)
    if L == 0:
        return 0
    else:
        return 1.0*len(set1&set2)/L
      

