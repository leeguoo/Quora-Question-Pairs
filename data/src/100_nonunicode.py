#!/home/guoli/anaconda2/bin/python
import string
import chardet
from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer("english")

def wordstem(fname):
    f = open(fname,"r")
    lines = f.readlines()
    f.close()
    
    for line in lines[:50]:
        words = line[:-1].split(" ")
        for word in words:
            if chardet.detect(word)["encoding"] != 'ascii':
                print word, [ord(c) for c in word] #chardet.detect(word)["encoding"], word.decode(chardet.detect(word)["encoding"]).encode('ascii')
wordstem("destop_depunct_clean_train.csv")
