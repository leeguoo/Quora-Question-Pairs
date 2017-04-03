#!/home/guoli/anaconda2/bin/python
from nltk.corpus import stopwords
import string

def rm_stops(fname):
    f = open(fname,"r")
    lines = f.readlines()
    f.close()

    fname = "destop_"+fname
    f = open(fname,"w")    
    for line in lines:
        nline = " ".join([word for word in line[:-1].split() 
                          if word not in stopwords.words('english')])+"\n"
        f.write(nline)
    f.close()

#rm_stops("depunct_clean_train.csv")
rm_stops("depunct_clean_test.csv")
