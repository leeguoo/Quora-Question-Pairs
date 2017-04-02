#!/home/guoli/anaconda2/bin/python
from nltk.corpus import stopwords
import string

def sentence2list(s):
    s = s.decode('unicode_escape').encode('ascii','ignore')
    words = s.translate(None,string.punctuation).lower().split()
    return [word for word in words if word not in stopwords.words('english')]

def removestops(fname,n1,n2):
    f = open(fname,"r")
    lines = f.readlines()
    f.close()
    
    f = open("stops_"+fname,"w")
    for line in lines:
        items = line.split(",")
        nline = "{0},{1}\n".format(" ".join(sentence2list(items[n1]))," ".join(sentence2list(items[n2])))
        f.write(nline)
    f.close()

#removestops("train_clean.csv",3,4)
#removestops("test_clean.csv",1,2)
removestops("test_clean2.csv",1,2)
