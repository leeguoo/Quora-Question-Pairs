#!/Users/guoli/anaconda2/bin/python

def shared_word_count(s1,s2):
    set1 = set([(w1, w2) for w1, w2 in zip(s1.split()[:-1],s1.split()[1:])])
    set2 = set([(w1, w2) for w1, w2 in zip(s2.split()[:-1],s2.split()[1:])])
    L = len(set1|set2)
    if L == 0:
        return 0
    else:
        return 1.0*len(set1&set2)/L
      
def xGenerate(col,in_name,out_name):
    f = open(in_name,"r")
    lines = f.readlines()
    f.close()

    f = open(out_name,"w")
    f.write(col+"\n")
    for line in lines[1:]:
        items = line[:-1].split(",")
        f.write("{0:.5E}\n".format(shared_word_count(items[0],items[1])))

in_name = "../../../input/stem_stops_train_clean.csv"
out_name = "train_bigramcount.csv"
xGenerate("BGC",in_name,out_name)
