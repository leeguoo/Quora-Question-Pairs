import string
import nltk
from nltk.corpus import stopwords
import numpy as np
import pandas as pd
from collections import Counter
import itertools
import numpy.linalg as LA
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer("english")

class txt2num(object):

    def __init__(self,trainpath,testpath):
        self.train = self.clean_train(trainpath)
        self.test = self.clean_test(testpath)
        self.get_word_list()
        self.corpus = self.get_corpus()

        numtrain = pd.DataFrame()
        numtrain["is_duplicate"] = self.train.is_duplicate
        for i in range(3):
            numtrain = numtrain.join(self.get_features(self.train,i+1),how="outer")
        numtrain.to_csv("num_train.csv",index=False)

        numtest = pd.DataFrame()
        for i in range(3):
            numtest = numtest.join(self.get_features(self.test,i+1),how="outer")
        numtest.to_csv("num_test.csv",index=False)

    def clean_train(self,trainpath):
        f = open(trainpath,'r')
        lines = f.readlines()
        f.close()
        
        q1 = []
        q2 = []
        y = []
        for line in lines[1:]:
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
            q1.append(items[3])
            q2.append(items[4])
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
            q1.append(items[1])
            q2.append(items[2])
        return pd.DataFrame({"question1":q1,"question2":q2})

    def get_word_list(self):
        for df in [self.train,self.test]:
            for q in ["question1","question2"]:
                for punct in string.punctuation:
                    df[q] = df[q].apply(lambda x: x.replace(punct," "))
                df[q] = df[q].apply(lambda x: x.lower())
                df[q] = df[q].apply(lambda x: x.decode('unicode_escape').encode('ascii','ignore'))
                df[q] = df[q].apply(lambda x: x.split())
                df[q] = df[q].apply(lambda x: [stemmer.stem(xx) for xx in x 
                                               if xx not in stopwords.words("english")])

    def get_features(self,df,n):
        self.idf = self.get_idf(n)
        ndf = pd.DataFrame()
        ndf[str(n)+"_SWC"] = df.apply(lambda x: self.shared_word_count(x,n),axis=1)
        ndf[str(n)+"_SWC_IDF"] = df.apply(lambda x: self.idf_shared_word_count(x,n),axis=1)
        ndf[str(n)+"_ND"] = df.apply(lambda x: self.norm_dist(x,n),axis=1)
        ndf[str(n)+"_ND_IDF"] = df.apply(lambda x: self.idf_norm_dist(x,n),axis=1)
        return ndf

    def get_corpus(self):
        se = self.train.question1
        se = se.append(self.train.question2,ignore_index=True)
        se = se.append(self.test.question1,ignore_index=True)
        se = se.append(self.test.question2,ignore_index=True)
        se = se.apply(lambda x: " ".join(x))
        se = se.drop_duplicates().reset_index(drop=True)
        return se.apply(lambda x: list(set(x.split())))

    def ngrams(self,s,n):
        return zip(*[s[i:len(s)-i-1] for i in range(n)])

    def get_idf(self,n):
        if n == 1:
            corpus = self.corpus
        elif n>1:
            corpus = self.corpus.apply(lambda x: self.ngrams(x,n))
        idf = {}
        for k,v in Counter(list(itertools.chain(*corpus))).items():
            if v>1 and v<len(self.corpus.index):
                idf[k] = np.log(v)
        return idf

    def shared_word_count(self,row,n):
        if n==1:
            set1 = set(row['question1'])
            set2 = set(row['question2'])
        elif n>1:
            set1 = set(self.ngrams(row['question1'],n))
            set2 = set(self.ngrams(row['question2'],n))
        if len(set1|set2)==0:
            return -9
        else:
            return 1.0*len(set1&set2)/len(set1|set2)

    def idf_shared_word_count(self,row,n):
        if n==1:
            set1 = set(row['question1'])
            set2 = set(row['question2'])
        elif n>1:
            set1 = set(self.ngrams(row['question1'],n))
            set2 = set(self.ngrams(row['question2'],n))
        both = set1|set2
        shared = set1&set2
        LL = 0
        for k in both:
            if self.idf.get(k,None):
                LL += self.idf[k]
        if LL == 0:
            return -9
        else:
            L = 0
            for k in shared:
                if self.idf.get(k,None):
                    L += self.idf[k]
            return L/LL

    def words2vec(self,words,keys):
        d = dict.fromkeys(keys,0)
        for word in words:
            d[word] += 1
        return np.array(d.values())

    def norm_dist(self,row,n):
        if n==1:
            words1 = row['question1']
            words2 = row['question2']
        elif n>1:
            words1 = self.ngrams(row['question1'],n)
            words2 = self.ngrams(row['question2'],n)
        keys = sorted(list(set(words1+words2)))
        v1 = self.words2vec(words1,keys)
        v2 = self.words2vec(words2,keys)
        n1 = LA.norm(v1)
        n2 = LA.norm(v2)
        if n1==0 and n2==0:
            return 0
        elif n1==0:
            return LA.norm(v2/n2)
        elif n2==0:
            return LA.norm(v1/n1)
        else:
            return LA.norm(v1/n1-v2/n2)

    def idf_words2vec(self,words,keys):
        d = dict.fromkeys(keys,0)
        for word in words:
            if self.idf.get(word,None):
                d[word] += self.idf[word]
        return np.array(d.values())

    def idf_norm_dist(self,row,n):
        if n==1:
            words1 = row['question1']
            words2 = row['question2']
        elif n>1:
            words1 = self.ngrams(row['question1'],n)
            words2 = self.ngrams(row['question2'],n)
        keys = sorted(list(set(words1+words2)))
        v1 = self.idf_words2vec(words1,keys)
        v2 = self.idf_words2vec(words2,keys)
        n1 = LA.norm(v1)
        n2 = LA.norm(v2)
        if n1==0 and n2==0:
            return 0
        elif n1==0:
            return LA.norm(v2/n2)
        elif n2==0:
            return LA.norm(v1/n1)
        else:
            return LA.norm(v1/n1-v2/n2)

TN = txt2num("train.csv","test.csv")
