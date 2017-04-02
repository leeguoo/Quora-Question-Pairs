#!/home/guoli/anaconda2/bin/python
import nltk

def word_count_diff(words,line):
    items = line[:-1].split(",")
    slist1 = items[0].split()
    slist2 = items[1].split()
    diffs = [str(abs(slist1.count(word)-slist2.count(word))) for word in words]
    return ",".join(diffs)

#in_name = "../../input/stem_stops_train_clean.csv"
in_name = "../../input/lower_train_clean.csv"
out_name = "train_WhatDiffCount.csv"


f = open(in_name,"r")
lines = f.readlines()
f.close()

for line in lines[1:20]:
    s = line[:-1].split(",")[0]

#tokens = nltk.word_tokenize(s)
    tagged = nltk.pos_tag(s.split())
#print tokens
    print s
    print tagged
    print [item[0] for item in tagged if item[1] in ["VB","VBG","VBN","VBP","NN","NNS"]]

#f = open(out_name,"w")
#f.write(",".join(["WCD_"+word for word in words])+"\n")
#for line in lines[1:]:
#    f.write(word_count_diff(words,line)+"\n")
#f.close()
