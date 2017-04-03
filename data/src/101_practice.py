#!/home/guoli/anaconda2/bin/python
import string
import chardet
from nltk.stem.snowball import SnowballStemmer
from nltk import stem

LMMZ = stem.WordNetLemmatizer()

stemmer = SnowballStemmer("english")

#def stem_all(s):
#    words = []
#    for word in s.split():
#        if chardet.detect(word)["encoding"] == 'ascii':
#            words.append(stemmer.stem(word))
#            print word, stemmer.stem(word), LMMZ.lemmatize(word)
##        else:
##            words.append(word)
#    print words
#    return " ".join(words)
#
#def wordstem(fname):
#    f = open(fname,"r")
#    lines = f.readlines()
#    f.close()
#    
#    f = open("stem_"+fname,"w")
#    for line in lines[:20]:
#        items = line[:-1].split(",")
#        nline = "{0},{1}\n".format(stem_all(items[0]),stem_all(items[1]))
#        f.write(nline)
#    f.close()
#
#wordstem("destop_depunct_clean_train.csv")
