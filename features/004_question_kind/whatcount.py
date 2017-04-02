#!/Users/guoli/anaconda2/bin/python

def word_count_diff(words,line):
    items = line[:-1].split(",")
    slist1 = items[0].split()
    slist2 = items[1].split()
    diffs = [str(abs(slist1.count(word)-slist2.count(word))) for word in words]
    return ",".join(diffs)

in_name = "../../input/lower_train_clean.csv"
out_name = "train_WhatDiffCount.csv"

words = ["what","how","when","who","where","why"]

f = open(in_name,"r")
lines = f.readlines()
f.close()

f = open(out_name,"w")
f.write(",".join(["WCD_"+word for word in words])+"\n")
for line in lines[1:]:
    f.write(word_count_diff(words,line)+"\n")
f.close()
