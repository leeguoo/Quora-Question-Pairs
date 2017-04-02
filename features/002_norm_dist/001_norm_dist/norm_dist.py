#!/Users/guoli/anaconda2/bin/python
import numpy as np
import numpy.linalg as LA

def words2vec(words,keys):
    d = dict.fromkeys(keys,0)
    for word in words: 
        d[word] += 1
    return np.array(d.values())

def norm_dist(s1,s2):
    words1 = s1.split()
    words2 = s2.split()
    keys = sorted(list(set(words1+words2)))
    v1 = words2vec(words1,keys)
    v2 = words2vec(words2,keys)
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

def xGenerate(col,in_name,out_name):
    f = open(in_name,"r")
    lines = f.readlines()
    f.close()

    f = open(out_name,"w")
    f.write(col+"\n")
    for line in lines[1:]:
        items = line[:-1].split(",")
        f.write("{0:.5E}\n".format(norm_dist(items[0],items[1])))

in_name = "../../../input/stem_stops_train_clean.csv"
out_name = "train_normdist.csv"
xGenerate("ND",in_name,out_name)
