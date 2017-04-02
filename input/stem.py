#!/home/guoli/anaconda2/bin/python
import string
from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer("english")

def stem_all(s):
    return " ".join([stemmer.stem(word) for word in s.split()])

def wordstem(fname):
    f = open(fname,"r")
    lines = f.readlines()
    f.close()
    
    f = open("stem_"+fname,"w")
    for line in lines:
        items = line[:-1].split(",")
        nline = "{0},{1}\n".format(stem_all(items[0]),stem_all(items[1]))
        f.write(nline)
    f.close()

wordstem("stops_train_clean.csv")

