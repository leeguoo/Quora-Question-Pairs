#!/Users/guoli/anaconda2/bin/python
from norm_dist import norm_dist
import pylab as plt
import numpy as np
import pandas as pd

path = "/Users/guoli/Desktop/kaggle/quora/input/"
train = pd.read_csv(path+"train.csv",nrows=10000)

vnd = np.vectorize(norm_dist)

train["NormDist"] = vnd(train.question1, train.question2)

x0 = train[train.is_duplicate==0].NormDist
x1 = train[train.is_duplicate==1].NormDist

plt.hist(x0,bins=20,alpha=0.5,label='0')
plt.hist(x1,bins=20,alpha=0.5,label='1')
plt.legend()
plt.xlabel('NormDist')
plt.ylabel('PairCount')
plt.savefig('norm_dist_fig.pdf')
#plt.show()
