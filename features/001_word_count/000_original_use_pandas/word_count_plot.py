#!/Users/guoli/anaconda2/bin/python
from word_count import shared_word_count
import pylab as plt
import numpy as np
import pandas as pd

path = "/Users/guoli/Desktop/kaggle/quora/input/"
train = pd.read_csv(path+"train.csv",nrows=10000)

vswc = np.vectorize(shared_word_count)

train["WordCount"] = vswc(train.question1, train.question2)

x0 = train[train.is_duplicate==0].WordCount
x1 = train[train.is_duplicate==1].WordCount

plt.hist(x0,bins=20,alpha=0.5,label='0')
plt.hist(x1,bins=20,alpha=0.5,label='1')
plt.legend()
plt.xlabel('WordCount')
plt.ylabel('PairCount')
plt.savefig('word_count_fig.pdf')
#plt.show()
