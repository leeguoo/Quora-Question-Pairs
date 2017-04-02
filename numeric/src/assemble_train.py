#!/Users/guoli/anaconda2/bin/python
from word_count import shared_word_count
from norm_dist import norm_dist
import pylab as plt
import numpy as np

path = "../../input/"
f = open(path+"train.csv","r")
lines = f.readlines()
f.close()

x1 = []
x2 = []
for line in lines[1:]:
    items = line.split(",")    
    x1.append(shared_word_count(items[3],items[4]))
    x2.append(norm_dist(items[3],items[4]))
df = pd.read_csv(path+"train.csv",usecols=["is_duplicate"])
df["wordcount"] = x1
df["normdist"] = x2
df.to_csv("train_numeric.csv",index=False)

