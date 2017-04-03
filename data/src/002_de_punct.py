#!/home/guoli/anaconda2/bin/python
from nltk.corpus import stopwords
import string
import nltk

def rm_punct(fname,n1,n2):
    f = open(fname,"r")
    lines = f.readlines()
    f.close()
    
    f = open("depunct_"+fname,"w")
    for line in lines[:]:
        items = line.split(",")
        s1 = items[n1]
        s2 = items[n2]
        for punct in string.punctuation:
            s1 = s1.replace(punct," ")
            s2 = s2.replace(punct," ")
        nline = "{0},{1}\n".format(s1,s2)
        f.write(nline)
    f.close()

#rm_punct("clean_train.csv",3,4)
rm_punct("clean_test.csv",1,2)

