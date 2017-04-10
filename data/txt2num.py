import string
import nltk
from nltk.corpus import stopwords
import numpy as np
import pandas as pd
from collections import Counter
import itertools
import json

class txt2num(object):

    def __init__(self,trainpath,testpath):
        self.train = self.clean_train(trainpath)
        self.test = self.clean_test(testpath)
        self.get_word_list()
        self.corpus = self.get_corpus()
        self.idf = self.get_idf()
        numtrain = self.get_features(self.train)
        numtrain.to_csv("num_train.csv",index=False)

    def clean_train(self,trainpath):
        f = open(trainpath,'r')
        lines = f.readlines()
        f.close()
        
        q1 = []
        q2 = []
        y = []
        for line in lines[1:]:
#            line = line.decode('unicode_escape').encode('ascii','ignore')
            line = line.replace('\n','')
            line = line.replace('\r','\n')
            line = line.replace('\\','|')
            line = line.replace(',',";")
            line = line.replace('";','",')
            line = line.replace('"",','"";')
            line = line.replace('""";','""",')
            line = line.replace('",",','","')
            line = line.replace(',"";',',"",')
            items = line[:-1].split(",")
            q1.append("emptyemptyempty "+items[3])
            q2.append("emptyemptyempty "+items[4])
            y.append(int(items[-1][1]))
        return pd.DataFrame({"question1":q1,"question2":q2,"is_duplicate":y})

    def clean_test(self,testpath):
        f = open(testpath,'r')
        lines = f.readlines()
        f.close()

        q1 = []
        q2 = []
        for line in lines[1:]:
            line = line.replace('\n','\r')
            line = line.replace('"\r','"\n')
            line = line.replace('\r',"")
            line = line.replace('\\','|')
            line = line.replace(',',";")
            line = line.replace('";','",')
            line = line.replace('"",','"";')
            line = line.replace('""";','""",')
            line = line.replace('",",','","')
            line = line.replace(',"";',',"",')
            line = line.replace(';',',',1)
            line = line.replace(',"";',',"",')
            line = line.replace(',",',',"')
            line = line.replace('],','];')
            items = line[:-1].split(",")
            q1.append("emptyemptyempty "+items[1])
            q2.append("emptyemptyempty "+items[2])
        return pd.DataFrame({"question1":q1,"question2":q2})

    def get_word_list(self):
        for df in [self.train,self.test]:
            for q in ["question1","question2"]:
                for punct in string.punctuation:
                    df[q] = df[q].apply(lambda x: x.replace(punct," "))
                df[q] = df[q].apply(lambda x: x.lower())
                df[q] = df[q].apply(lambda x: x.decode('unicode_escape').encode('ascii','ignore'))
                df[q] = df[q].apply(lambda x: x.split())
#                df[q] = df[q].apply(nltk.word_tokenize)
                #df[q] = df[q].apply(lambda x: [xx for xx in x if xx not in stopwords.words('english')])

    def get_features(self,df):
        ndf = pd.DataFrame()
        ndf["SWC"] = df.apply(self.shared_word_count,axis=1)
        ndf["SWC_IDF"] = df.apply(self.idf_shared_word_count,axis=1)
        return ndf

    def get_corpus(self):
        se = self.train.question1
        se = se.append(self.train.question2,ignore_index=True)
        se = se.append(self.test.question1,ignore_index=True)
        se = se.append(self.test.question2,ignore_index=True)
        se = se.apply(lambda x: " ".join(x))
        se = se.drop_duplicates().reset_index(drop=True)
        return se.apply(lambda x: list(set(x.split())))

    def get_idf(self):
        idf = {}
        for k,v in Counter(list(itertools.chain(*self.corpus))).items():
            if v>1 and v<len(self.corpus.index):
                idf[k] = np.log(v)
        return idf

    def shared_word_count(self,row):
        set1 = set(row['question1'])
        set2 = set(row['question2'])
        return 1.0*len(set1&set2)/len(set1|set2)

    def idf_shared_word_count(self,row):
        set1 = set(row['question1'])
        set2 = set(row['question2'])
        both = set1|set2
        shared = set1&set2
        if len(shared)==0:
            return 0
        else:
            LL = 0
            for k in both:
                if self.idf.get(k,None):
                    LL += self.idf[k]
            L = 0
            for k in shared:
                if self.idf.get(k,None):
                    L += self.idf[k]
            return L/LL

TN = txt2num("train.csv","test.csv")
