#!/home/guoli/anaconda2/bin/python
import string
import chardet
import re
from nltk.stem.snowball import SnowballStemmer
from collections import Counter
import json

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

nasc_dict = Counter(nascs)
for k in nasc_dict.keys():
    print k, nasc_dict[k]
#f = open("non_ascii.json","w")
#json.dump(nasc_dict,f)
#f.close()
#
#f = open("non_ascii.json","r")
#data = json.load(f)
#for k in data.keys():
#    print k, data[k]
