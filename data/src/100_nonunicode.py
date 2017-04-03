#!/home/guoli/anaconda2/bin/python
import string
import chardet
import re
from nltk.stem.snowball import SnowballStemmer
from collections import Counter

stemmer = SnowballStemmer("english")

def non_ascii(fname):
    f = open(fname,"r")
    lines = f.readlines()
    f.close()

    nasc = []    
    for line in lines:
        words = line[:-1].split(" ")
        for word in words:
            if chardet.detect(word)["encoding"] != 'ascii' and word!='':
                char_list = []
                for char in word:
                    if chardet.detect(char)["encoding"]=='ascii':
                        char_list.append(" ")
                    else:
                        char_list.append(char)
                nasc += "".join(char_list).split()
    return nasc

nascs = non_ascii("depunct_clean_train.csv")
nascs += non_ascii("depunct_clean_test.csv")
for nasc in set(nascs):
    print nasc+","
