#!/home/guoli/anaconda2/bin/python
from word_count import shared_word_count
from norm_dist import norm_dist
import pylab as plt
import numpy as np

path = "../../input/"
f = open(path+"test.csv","r")
lines = f.readlines()
f.close()

x1 = []
x2 = []
for line in lines[1:]:
    items = line.split(",")    
    x1.append(shared_word_count(items[1],items[2]))
    x2.append(norm_dist(items[1],items[2]))

f = open("test_numeric.csv","w")
f.write("wordcount,normdist\n")
for xx1, xx2 in zip(x1,x2):
    f.write("{0},{1}\n".format(xx1,xx2))
f.close()
